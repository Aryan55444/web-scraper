

import json
import pandas as pd
from datetime import datetime

def export_data(data, format_type):
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    exporters = {
        "JSON": _export_json,
        "CSV": _export_csv,
        "TXT": _export_txt,
        "HTML": _export_html
    }
    
    if format_type in exporters:
        return exporters[format_type](data, timestamp)
    else:
        raise ValueError(f"Unsupported export format: {format_type}")

def _export_json(data, timestamp):
    
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    return json_str, f"scraped_data_{timestamp}.json", "application/json"

def _export_csv(data, timestamp):
    
    rows = []
    
    for key, value in data['data'].items():
        if isinstance(value, list):
            for idx, item in enumerate(value):
                if isinstance(item, dict):
                    row = {
                        'data_type': key,
                        'index': idx + 1,
                        **item
                    }
                    rows.append(row)
                else:
                    rows.append({
                        'data_type': key,
                        'index': idx + 1,
                        'value': str(item)
                    })
        elif isinstance(value, dict):
            for sub_key, sub_value in value.items():
                rows.append({
                    'data_type': key,
                    'category': sub_key,
                    'value': str(sub_value)
                })
        else:
            rows.append({
                'data_type': key,
                'value': str(value)
            })
    
    rows.insert(0, {
        'data_type': 'metadata',
        'category': 'url',
        'value': data.get('url', '')
    })
    rows.insert(1, {
        'data_type': 'metadata',
        'category': 'timestamp',
        'value': data.get('timestamp', '')
    })
    rows.insert(2, {
        'data_type': 'metadata',
        'category': 'status_code',
        'value': str(data.get('status_code', ''))
    })
    
    df = pd.DataFrame(rows)
    csv_str = df.to_csv(index=False)
    return csv_str, f"scraped_data_{timestamp}.csv", "text/csv"

def _export_txt(data, timestamp):
    
    lines = []
    
    lines.append("=" * 70)
    lines.append("WEB SCRAPER PRO - SCRAPED DATA")
    lines.append("=" * 70)
    lines.append("")
    
    lines.append(f"URL: {data.get('url', 'N/A')}")
    lines.append(f"Scraped At: {data.get('timestamp', 'N/A')}")
    lines.append(f"Status Code: {data.get('status_code', 'N/A')}")
    lines.append(f"Content Type: {data.get('content_type', 'N/A')}")
    lines.append("")
    lines.append("=" * 70)
    lines.append("")
    
    for key, value in data['data'].items():
        lines.append(f"\n{'─' * 70}")
        lines.append(f"📦 {key.upper().replace('_', ' ')}")
        lines.append(f"{'─' * 70}\n")
        
        if isinstance(value, list):
            if not value:
                lines.append("  [No data found]")
            else:
                for idx, item in enumerate(value, 1):
                    if isinstance(item, dict):
                        lines.append(f"\n  Item {idx}:")
                        for k, v in item.items():
                            lines.append(f"    • {k}: {v}")
                    else:
                        lines.append(f"  {idx}. {item}")
        
        elif isinstance(value, dict):
            if not value:
                lines.append("  [No data found]")
            else:
                for k, v in value.items():
                    if isinstance(v, (list, dict)):
                        lines.append(f"\n  {k}:")
                        lines.append(f"    {v}")
                    else:
                        lines.append(f"  • {k}: {v}")
        
        else:
            lines.append(f"{value}")
        
        lines.append("")
    
    lines.append("\n" + "=" * 70)
    lines.append("End of scraped data")
    lines.append("=" * 70)
    
    txt_str = '\n'.join(lines)
    return txt_str, f"scraped_data_{timestamp}.txt", "text/plain"

def _export_html(data, timestamp):
    
    html_parts = []
    
    html_parts.append('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scraped Data - Web Scraper Pro</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { text-align: center; margin-bottom: 30px; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; }
        .section { margin-bottom: 30px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; }
        .section-title { background: #f8f9fa; padding: 15px; margin: 0; border-bottom: 1px solid #ddd; font-size: 18px; }
        .item { padding: 15px; border-bottom: 1px solid #eee; }
        .item:last-child { border-bottom: none; }
        .item-title { font-weight: bold; margin-bottom: 10px; color: #333; }
        .item-content { color: #666; line-height: 1.6; }
        .item-content pre { background: #f8f9fa; padding: 10px; border-radius: 5px; overflow-x: auto; }
        .metadata { background: #e9ecef; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🕷️ Web Scraper Pro - Scraped Data</h1>
            <p>Generated on: {timestamp}</p>
        </div>
        
        <div class="metadata">
            <p><strong>URL:</strong> {url}</p>
            <p><strong>Scraped At:</strong> {scrape_time}</p>
            <p><strong>Status Code:</strong> {status_code}</p>
            <p><strong>Content Type:</strong> {content_type}</p>
        </div>'''.format(
            timestamp=timestamp,
            url=data.get('url', 'N/A'),
            scrape_time=data.get('timestamp', 'N/A'),
            status_code=data.get('status_code', 'N/A'),
            content_type=data.get('content_type', 'N/A')
        ))
    
    for key, value in data['data'].items():
        section_title = key.replace('_', ' ').title()
        html_parts.append(f'<div class="section"><h2 class="section-title">📦 {section_title}</h2>')
        
        if isinstance(value, list):
            if not value:
                html_parts.append('<p class="item-content">No data found</p>')
            else:
                for idx, item in enumerate(value, 1):
                    if isinstance(item, dict):
                        html_parts.append(f'<div class="item"><div class="item-title">Item {idx}</div>')
                        for k, v in item.items():
                            if k == 'url' and isinstance(v, str) and v.startswith('http'):
                                html_parts.append(f'<div class="item-content"><strong>{k}:</strong> <a href="{v}" target="_blank">{v}</a></div>')
                            else:
                                html_parts.append(f'<div class="item-content"><strong>{k}:</strong> {v}</div>')
                        html_parts.append('</div>')
                    else:
                        html_parts.append(f'<div class="item"><div class="item-content">{idx}. {item}</div></div>')
        
        elif isinstance(value, dict):
            if not value:
                html_parts.append('<p class="item-content">No data found</p>')
            else:
                for k, v in value.items():
                    html_parts.append(f'<div class="item">')
                    html_parts.append(f'<div class="item-title">{k}</div>')
                    html_parts.append(f'<div class="item-content">{v}</div>')
                    html_parts.append('</div>')
        
        else:
            # Handle HTML source and other text content
            if key == 'html_source':
                html_parts.append(f'<div class="item"><div class="item-title">Raw HTML Source</div><pre class="item-content">{value}</pre></div>')
            else:
                html_parts.append(f'<div class="item"><pre class="item-content">{value}</pre></div>')
        
        html_parts.append('</div>')
    
    html_parts.append('''
    </div>
</body>
</html>''')
    
    html_str = ''.join(html_parts)
    return html_str, f"scraped_data_{timestamp}.html", "text/html"
