

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime
import pandas as pd
import re

# Optional Brotli support
try:
    import brotlicffi as _brotli
except Exception:
    try:
        import brotli as _brotli  # type: ignore
    except Exception:
        _brotli = None

from config import REQUEST_HEADERS, ERROR_MESSAGES

def scrape_website(url, options, user_agent, timeout, verify_ssl, follow_redirects):
    
    try:
        # Ensure URL has http:// or https:// prefix
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        headers = REQUEST_HEADERS.copy()
        headers['User-Agent'] = user_agent
        # Let requests negotiate encoding unless Brotli is supported
        if _brotli is None and 'Accept-Encoding' in headers:
            # Remove br to avoid servers sending Brotli we can't decode
            headers['Accept-Encoding'] = 'gzip, deflate'
        headers['Cache-Control'] = 'no-cache'
        headers['Pragma'] = 'no-cache'
        
        response = requests.get(
            url,
            headers=headers,
            timeout=timeout,
            verify=verify_ssl,
            allow_redirects=follow_redirects
        )
        response.raise_for_status()
        
        # If server sent Brotli but Python env lacks decoder, retry without br
        content_encoding = (response.headers.get('Content-Encoding') or '').lower()
        if 'br' in content_encoding and _brotli is None:
            # Retry request without br to get gzip/deflate or identity
            retry_headers = headers.copy()
            retry_headers['Accept-Encoding'] = 'gzip, deflate'
            response = requests.get(
                url,
                headers=retry_headers,
                timeout=timeout,
                verify=verify_ssl,
                allow_redirects=follow_redirects
            )
            response.raise_for_status()
            content_encoding = (response.headers.get('Content-Encoding') or '').lower()

        # If Brotli is present and server responded with br, manually decode to be safe
        if 'br' in content_encoding and _brotli is not None:
            try:
                decoded_bytes = _brotli.decompress(response.content)
                # Use declared encoding or fallback to utf-8
                enc = response.encoding or 'utf-8'
                content = decoded_bytes.decode(enc, errors='replace')
            except Exception:
                # Fallback to requests' best-effort text decoding
                content = response.text
        else:
            # Let requests handle gzip/deflate and text decoding
            if response.encoding == 'ISO-8859-1':
                response.encoding = response.apparent_encoding or 'utf-8'
            content = response.text

        # Reject obviously non-HTML content
        content_type = (response.headers.get('Content-Type') or '').lower()
        if content_type and not any(t in content_type for t in ['text/html', 'application/xhtml+xml']):
            return None, (
                f"Unsupported content type: {content_type}. The URL may not be an HTML page."
            )

        # Check if content is actually readable text
        if len(content) > 1000 and content.count('\x00') > len(content) * 0.1:
            # Content appears to be binary or heavily encoded
            return None, "Website returned binary/encoded content that cannot be parsed as text. This often happens with JavaScript-heavy sites like YouTube."
        
        # Parse HTML with fallbacks
        soup = None
        parse_errors = []
        for parser in ['html.parser', 'lxml', 'html5lib']:
            try:
                soup = BeautifulSoup(content, parser)
                if soup and soup.find():
                    break
            except Exception as pe:
                parse_errors.append(f"{parser}: {pe}")
        if soup is None:
            return None, (
                "❌ Unexpected Error: The markup was rejected by the parser. "
                + (" | ".join(parse_errors) if parse_errors else "Try a different parser or encoding.")
            )
        
        results = {
            'url': url,
            'status_code': response.status_code,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'content_type': response.headers.get('content-type', 'unknown'),
            'data': {}
        }
        
        if "All Text" in options:
            results['data']['all_text'] = _extract_all_text(soup)
        
        if "Links" in options:
            results['data']['links'] = _extract_links(soup, url)
        
        if "Images" in options:
            results['data']['images'] = _extract_images(soup, url)
        
        if "Tables" in options:
            results['data']['tables'] = _extract_tables(soup)
        
        if "Headings" in options:
            results['data']['headings'] = _extract_headings(soup)
        
        if "Metadata" in options:
            results['data']['metadata'] = _extract_metadata(soup)
        
        if "Paragraphs" in options:
            results['data']['paragraphs'] = _extract_paragraphs(soup)
        
        if "HTML Source" in options:
            results['data']['html_source'] = _extract_html_source(response.text)
        
        if "HTML Elements" in options:
            results['data']['html_elements'] = _extract_html_elements(soup)
        
        if "Code Snippets" in options:
            results['data']['code_snippets'] = _extract_code_snippets(soup)
        
        return results, None
    
    except requests.exceptions.HTTPError as e:
        return None, _format_http_error(e)
    
    except requests.exceptions.ConnectionError as e:
        return None, _format_connection_error(url)
    
    except requests.exceptions.Timeout as e:
        return None, _format_timeout_error(timeout)
    
    except requests.exceptions.RequestException as e:
        return None, f"Request Error: {str(e)}"
    
    except Exception as e:
        return None, f"Unexpected Error: {str(e)}"

def _extract_all_text(soup):
    # Remove script and style elements
    for script in soup(["script", "style", "noscript"]):
        script.decompose()
    
    # Get text and clean it up
    text = soup.get_text(separator='\n', strip=True)
    
    # Check if text contains too many non-printable characters
    printable_chars = sum(1 for c in text if c.isprintable() or c.isspace())
    if len(text) > 100 and printable_chars / len(text) < 0.7:
        return "Content appears to be encoded or binary data. This website may not be suitable for text extraction."
    
    # Remove excessive whitespace and empty lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    cleaned_text = '\n'.join(lines)
    
    # Limit text length to prevent overwhelming output
    if len(cleaned_text) > 10000:
        cleaned_text = cleaned_text[:10000] + "\n\n[... Content truncated for display. Use export to get full content.]"
    
    return cleaned_text

def _extract_links(soup, base_url):
    
    links = []
    for link in soup.find_all('a', href=True):
        absolute_url = urljoin(base_url, link['href'])
        link_text = link.get_text(strip=True) or "[No text]"
        links.append({
            'text': link_text,
            'url': absolute_url,
            'title': link.get('title', '')
        })
    return links

def _extract_images(soup, base_url):
    
    images = []
    for img in soup.find_all('img'):
        img_url = urljoin(base_url, img.get('src', ''))
        images.append({
            'url': img_url,
            'alt': img.get('alt', 'No alt text'),
            'title': img.get('title', ''),
            'width': img.get('width', ''),
            'height': img.get('height', '')
        })
    return images

def _extract_tables(soup):
    
    tables = []
    for idx, table in enumerate(soup.find_all('table')):
        try:
            df = pd.read_html(str(table))[0]
            tables.append({
                'table_number': idx + 1,
                'rows': len(df),
                'columns': len(df.columns),
                'data': df.to_dict('records')
            })
        except Exception as e:
            tables.append({
                'table_number': idx + 1,
                'error': f"Could not parse table: {str(e)}"
            })
    return tables

def _extract_headings(soup):
    
    headings = {}
    for level in range(1, 7):
        tag = f'h{level}'
        heading_texts = [h.get_text(strip=True) for h in soup.find_all(tag)]
        if heading_texts:
            headings[tag] = heading_texts
    return headings

def _extract_metadata(soup):
    
    metadata = {
        'title': soup.title.string if soup.title else 'No title',
        'meta_description': '',
        'meta_keywords': '',
        'author': '',
        'og_tags': {},
        'twitter_tags': {}
    }
    
    desc = soup.find('meta', attrs={'name': 'description'})
    if desc:
        metadata['meta_description'] = desc.get('content', '')
    
    keywords = soup.find('meta', attrs={'name': 'keywords'})
    if keywords:
        metadata['meta_keywords'] = keywords.get('content', '')
    
    author = soup.find('meta', attrs={'name': 'author'})
    if author:
        metadata['author'] = author.get('content', '')
    
    og_tags = soup.find_all('meta', property=re.compile(r'^og:'))
    for tag in og_tags:
        metadata['og_tags'][tag.get('property')] = tag.get('content', '')
    
    twitter_tags = soup.find_all('meta', attrs={'name': re.compile(r'^twitter:')})
    for tag in twitter_tags:
        metadata['twitter_tags'][tag.get('name')] = tag.get('content', '')
    
    return metadata

def _extract_paragraphs(soup):
    
    paragraphs = []
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if text:
            paragraphs.append(text)
    return paragraphs

def _extract_html_source(html_content):
    
    return html_content

def _extract_html_elements(soup):
    
    elements = {}
    
    # Extract divs with class or id (limit to 10 most important)
    divs = []
    for div in soup.find_all('div', limit=15):
        # Only include divs with class or id
        if not (div.get('class') or div.get('id')):
            continue
            
        # Skip divs with very long content
        text = div.get_text(strip=True)
        if len(text) > 1000:
            continue
            
        divs.append({
            'tag': 'div',
            'class': div.get('class', []),
            'id': div.get('id', ''),
            'content': text[:80] + ('...' if len(text) > 80 else '')
        })
        if len(divs) >= 10:
            break
    elements['divs'] = divs
    
    # Extract forms (limit to 5)
    forms = []
    for form in soup.find_all('form', limit=5):
        form_data = {
            'action': form.get('action', ''),
            'method': form.get('method', 'get'),
            'id': form.get('id', ''),
            'class': form.get('class', ''),
            'inputs': []
        }
        
        # Limit inputs to 10 per form
        for input_tag in form.find_all('input', limit=10):
            form_data['inputs'].append({
                'type': input_tag.get('type', 'text'),
                'name': input_tag.get('name', ''),
                'id': input_tag.get('id', '')
                # Removed value to improve performance
            })
        
        forms.append(form_data)
    elements['forms'] = forms
    
    # Extract buttons (limit to 10)
    buttons = []
    for button in soup.find_all(['button', 'input[type="submit"]', 'input[type="button"]', 'input[type="reset"]'], limit=10):
        if button.name == 'input' and button.get('type') not in ['submit', 'button', 'reset']:
            continue
        
        buttons.append({
            'tag': button.name,
            'type': button.get('type', ''),
            'id': button.get('id', ''),
            'text': button.get_text(strip=True)[:50] if button.name == 'button' else button.get('value', '')[:50]
        })
    elements['buttons'] = buttons
    
    return elements

def _extract_code_snippets(soup):
    
    code_snippets = []
    max_snippets = 20  # Limit total snippets
    max_content_length = 1000  # Limit content length
    
    # Extract code from <code> tags (limit to 5)
    for code in soup.find_all('code', limit=5):
        content = code.get_text(strip=True)
        if not content or len(content) > max_content_length:
            continue
            
        language = 'unknown'
        if code.get('class'):
            class_name = code.get('class')[0]
            if class_name.startswith('language-'):
                language = class_name
            else:
                language = class_name
                
        code_snippets.append({
            'type': 'inline',
            'language': language,
            'content': content[:max_content_length]
        })
    
    # Extract code from <pre> tags (limit to 5)
    for pre in soup.find_all('pre', limit=5):
        code_tag = pre.find('code')
        if code_tag:
            language = code_tag.get('class', [''])[0] if code_tag.get('class') else 'unknown'
            content = code_tag.get_text(strip=True)
        else:
            language = 'unknown'
            content = pre.get_text(strip=True)
        
        if not content or len(content) > max_content_length:
            continue
            
        code_snippets.append({
            'type': 'block',
            'language': language,
            'content': content[:max_content_length]
        })
        
        if len(code_snippets) >= max_snippets:
            return code_snippets
    
    # Extract script tags (limit to 5)
    for script in soup.find_all('script', limit=10):
        if script.get('src') or len(code_snippets) >= max_snippets:
            continue  # Skip external scripts
        
        content = script.string
        if content and content.strip():
            content = content.strip()
            if len(content) > max_content_length:
                content = content[:max_content_length] + "..."
                
            code_snippets.append({
                'type': 'script',
                'language': 'javascript',
                'content': content
            })
            
            if len(code_snippets) >= max_snippets:
                return code_snippets
    
    # Extract style tags (limit to 5)
    for style in soup.find_all('style', limit=5):
        if len(code_snippets) >= max_snippets:
            break
            
        content = style.string
        if content and content.strip():
            content = content.strip()
            if len(content) > max_content_length:
                content = content[:max_content_length] + "..."
                
            code_snippets.append({
                'type': 'style',
                'language': 'css',
                'content': content
            })
    
    return code_snippets

def _format_http_error(error):
    
    status_code = error.response.status_code if hasattr(error, 'response') and error.response else 'Unknown'
    
    # Handle case when ERROR_MESSAGES is not defined or status_code is not in it
    if 'ERROR_MESSAGES' in globals() and status_code in ERROR_MESSAGES:
        error_info = ERROR_MESSAGES[status_code]
        message = f"{error_info['title']}\n\n"
        message += f"{error_info['message']}\n\n"
        message += "Suggestions:\n"
        for tip in error_info['tips']:
            message += f"  • {tip}\n"
        return message
    else:
        return f"HTTP Error {status_code}: {str(error)}"
