

import streamlit as st
import pandas as pd
from urllib.parse import urlparse
from utils.export import export_data

def render_results_tab(scraped_data, export_format):
    
    if scraped_data:
        _display_metrics(scraped_data)
        st.markdown("---")
        _display_scraped_data(scraped_data)
        st.markdown("---")
        _display_export_section(scraped_data, export_format)
    else:
        _display_empty_state()

def _display_metrics(data):
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Status",
            data['status_code'],
            delta="Success" if data['status_code'] == 200 else "Error"
        )
    
    with col2:
        domain = urlparse(data['url']).netloc
        st.metric("Domain", domain if domain else "Unknown")
    
    with col3:
        data_types = len(data['data'])
        st.metric("Data Types", data_types)
    
    with col4:
        time_only = data['timestamp'].split()[1] if ' ' in data['timestamp'] else data['timestamp']
        st.metric("Scraped At", time_only)

def _display_scraped_data(data):
    
    st.subheader("📊 Extracted Data")
    
    if not data['data']:
        st.info("No data was extracted. Try selecting different scraping options.")
        return
    
    for key, value in data['data'].items():
        section_title = key.replace('_', ' ').title()
        
        with st.expander(f"📦 {section_title}", expanded=True):
            if isinstance(value, list):
                _display_list_data(key, value)
            elif isinstance(value, dict):
                _display_dict_data(value)
            else:
                _display_text_data(value)

def _display_list_data(data_type, items):
    
    if not items:
        st.info(f"No {data_type} found on this page.")
        return
    
    st.caption(f"Found {len(items)} item(s)")
    
    if data_type == "links":
        df = pd.DataFrame(items)
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "url": st.column_config.LinkColumn("URL"),
                "text": "Link Text",
                "title": "Title"
            }
        )
    
    elif data_type == "images":
        df = pd.DataFrame(items)
        st.dataframe(
            df,
            use_container_width=True,
            column_config={
                "url": st.column_config.LinkColumn("Image URL"),
                "alt": "Alt Text",
                "title": "Title"
            }
        )
    
    elif data_type == "tables":
        for table in items:
            if 'error' in table:
                st.warning(f"Table {table['table_number']}: {table['error']}")
            else:
                st.write(f"**Table {table['table_number']}** ({table['rows']} rows × {table['columns']} columns)")
                df = pd.DataFrame(table['data'])
                st.dataframe(df, use_container_width=True)
    
    elif data_type == "paragraphs":
        for idx, para in enumerate(items, 1):
            with st.container():
                st.markdown(f"**Paragraph {idx}:**")
                st.write(para)
                st.markdown("---")
    
    elif data_type == "html_elements":
        tabs = st.tabs(["Divs", "Forms", "Buttons"])
        
        with tabs[0]:
            if "divs" in items and items["divs"]:
                st.write(f"Found {len(items['divs'])} divs with class/id")
                for div in items["divs"]:
                    st.code(f"<div class='{' '.join(div['class']) if isinstance(div['class'], list) else div['class']}' id='{div['id']}'>\n  {div['content']}\n</div>", language="html")
            else:
                st.info("No divs with class/id found")
        
        with tabs[1]:
            if "forms" in items and items["forms"]:
                st.write(f"Found {len(items['forms'])} forms")
                for form in items["forms"]:
                    form_html = f"<form action='{form['action']}' method='{form['method']}'>"
                    for input_field in form["inputs"]:
                        form_html += f"\n  <input type='{input_field['type']}' name='{input_field['name']}' id='{input_field['id']}' value='{input_field['value']}'>"
                    form_html += "\n</form>"
                    st.code(form_html, language="html")
            else:
                st.info("No forms found")
        
        with tabs[2]:
            if "buttons" in items and items["buttons"]:
                st.write(f"Found {len(items['buttons'])} buttons")
                for button in items["buttons"]:
                    if button["tag"] == "button":
                        st.code(f"<button type='{button['type']}' id='{button['id']}'>{button['text']}</button>", language="html")
                    else:
                        st.code(f"<input type='{button['type']}' id='{button['id']}' value='{button['text']}'>", language="html")
            else:
                st.info("No buttons found")
    
    elif data_type == "code_snippets":
        if not items:
            st.info("No code snippets found on this page")
            return
            
        code_types = set(item["type"] for item in items)
        tabs = st.tabs(list(code_types))
        
        for i, code_type in enumerate(code_types):
            with tabs[i]:
                filtered_items = [item for item in items if item["type"] == code_type]
                st.write(f"Found {len(filtered_items)} {code_type} code snippets")
                
                for idx, snippet in enumerate(filtered_items, 1):
                    language = snippet["language"].replace("language-", "") if snippet["language"].startswith("language-") else snippet["language"]
                    if language == "unknown":
                        language = "text"
                    
                    with st.expander(f"Snippet {idx} ({language})"):
                        st.code(snippet["content"], language=language)
    
    else:
        for idx, item in enumerate(items, 1):
            if isinstance(item, dict):
                st.json(item)
            else:
                st.write(f"{idx}. {item}")

def _display_dict_data(data):
    
    if not data:
        st.info("No data available.")
        return
    
    try:
        df = pd.DataFrame([data]).T
        df.columns = ['Value']
        st.dataframe(df, use_container_width=True)
    except:
        st.json(data)

def _display_text_data(text):
    
    if not text or not str(text).strip():
        st.info("No text content found.")
        return
    
    text_str = str(text)
    if len(text_str) > 5000:
        st.text_area(
            "Content (truncated to 5000 characters)",
            text_str[:5000] + "\n\n[...Content truncated. Download the full data using export.]",
            height=300
        )
    else:
        st.text_area("Content", text_str, height=300)

def _display_export_section(data, export_format):
    
    st.subheader("📥 Export Data")
    
    try:
        export_data_str, filename, mime_type = export_data(data, export_format)
        
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            st.download_button(
                label=f"⬇️ Download as {export_format}",
                data=export_data_str,
                file_name=filename,
                mime=mime_type,
                use_container_width=True
            )
        
        with col2:
            if st.button("👁️ Preview Export", use_container_width=True):
                st.session_state.show_preview = not st.session_state.get('show_preview', False)
        
        with col3:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.scraped_data = None
                st.rerun()
        
        if st.session_state.get('show_preview', False):
            st.markdown("**Export Preview:**")
            if export_format == "HTML":
                st.code(export_data_str[:1000] + "\n...[truncated]", language="html")
            elif export_format == "JSON":
                st.code(export_data_str[:1000] + "\n...[truncated]", language="json")
            elif export_format == "CSV":
                st.code(export_data_str[:1000] + "\n...[truncated]", language="text")
            else:
                st.text(export_data_str[:1000] + "\n...[truncated]")
    
    except Exception as e:
        st.error(f"Export error: {str(e)}")

def _display_empty_state():
    st.markdown("""
        <div style='text-align: center; padding: 3rem 2rem; 
                    background: linear-gradient(135deg, #1e293b 0%, #2d3748 100%);
                    border-radius: 20px; 
                    box-shadow: 0 4px 20px rgba(0,0,0,0.5);
                    border: 1px solid rgba(102, 126, 234, 0.3);
                    margin: 2rem 0;'>
            <div style='font-size: 4rem; margin-bottom: 1rem;'>🕷️</div>
            <h2 style='color: #667eea; margin-bottom: 1rem;'>Ready to Start Scraping?</h2>
            <p style='font-size: 1.1rem; color: #b0b0b0; margin-bottom: 2rem;'>
                Configure your options in the sidebar and click <strong style="color: #e0e0e0;">Start Scraping</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🧪 Test Websites - Scraper Friendly")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='padding: 1.5rem; 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 15px; 
                    color: white;
                    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
                    margin-bottom: 1rem;'>
            <h4 style='margin: 0 0 0.5rem 0;'>📚 Quotes to Scrape</h4>
            <code style='background: rgba(255,255,255,0.2); 
                         color: white; 
                         padding: 0.3rem 0.6rem; 
                         border-radius: 5px;
                         display: block;
                         margin: 0.5rem 0;'>
                https://quotes.toscrape.com
            </code>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;'>
                Perfect for text extraction & pagination
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='padding: 1.5rem; 
                    background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
                    border-radius: 15px; 
                    color: white;
                    box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
                    margin-bottom: 1rem;'>
            <h4 style='margin: 0 0 0.5rem 0;'>📖 Books to Scrape</h4>
            <code style='background: rgba(255,255,255,0.2); 
                         color: white; 
                         padding: 0.3rem 0.6rem; 
                         border-radius: 5px;
                         display: block;
                         margin: 0.5rem 0;'>
                https://books.toscrape.com
            </code>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;'>
                Great for tables, images & product data
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='padding: 1.5rem; 
                    background: linear-gradient(135deg, #17a2b8 0%, #138496 100%);
                    border-radius: 15px; 
                    color: white;
                    box-shadow: 0 4px 15px rgba(23, 162, 184, 0.3);
                    margin-bottom: 1rem;'>
            <h4 style='margin: 0 0 0.5rem 0;'>🌐 Example.com</h4>
            <code style='background: rgba(255,255,255,0.2); 
                         color: white; 
                         padding: 0.3rem 0.6rem; 
                         border-radius: 5px;
                         display: block;
                         margin: 0.5rem 0;'>
                https://example.com
            </code>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;'>
                Simple test page for basic scraping
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='padding: 1.5rem; 
                    background: linear-gradient(135deg, #ffc107 0%, #ff9800 100%);
                    border-radius: 15px; 
                    color: white;
                    box-shadow: 0 4px 15px rgba(255, 193, 7, 0.3);
                    margin-bottom: 1rem;'>
            <h4 style='margin: 0 0 0.5rem 0;'>🔧 HTTPBin HTML</h4>
            <code style='background: rgba(255,255,255,0.2); 
                         color: white; 
                         padding: 0.3rem 0.6rem; 
                         border-radius: 5px;
                         display: block;
                         margin: 0.5rem 0;'>
                https://httpbin.org/html
            </code>
            <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;'>
                HTML test page for debugging
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.warning("⚠️ **Warning**: Many modern websites (ChatGPT, social media) actively block scrapers with 403 errors.")
    with col2:
        st.info("⚖️ **Legal**: Always respect Terms of Service and robots.txt files.")
