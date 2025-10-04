# 🌐 Web Scraper - Final Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.0+-green.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **A comprehensive web scraping application built as a final project demonstration. This tool enables efficient extraction and analysis of web content with a modern, user-friendly interface.**

## 👨‍💻 About the Developer

**Aryan Patel** - Full Stack Developer from India
- 🎓 Computer Science Enthusiast
- 🌍 Passionate about data extraction and web technologies
- 🚀 This project showcases practical implementation of web scraping concepts

## 📋 Project Overview

This **Web Scraper** is a final project that demonstrates proficiency in:
- **Web Scraping Technologies** - BeautifulSoup, Requests, HTTP protocols
- **Modern Python Development** - Clean architecture, error handling, data processing
- **User Interface Design** - Streamlit-based responsive web application
- **Data Management** - Export functionality, session handling, structured data processing

## ✨ Key Features

### 🔍 **Comprehensive Data Extraction**
- **Text Content**: Extract all textual content from web pages
- **Links & Navigation**: Capture hyperlinks with anchor text and metadata
- **Media Assets**: Extract images with alt text, titles, and source URLs
- **Structured Data**: Convert HTML tables to structured formats (CSV/JSON)
- **Content Hierarchy**: Extract headings (H1-H6) for content structure analysis
- **Metadata**: Capture page titles, descriptions, and meta tags
- **Semantic Content**: Extract paragraphs and content sections
- **Source Code**: Access complete HTML source for advanced analysis
- **UI Components**: Extract forms, buttons, and interactive elements
- **Code Elements**: Capture code snippets and preformatted text

### 📊 **Export & Analysis**
- **Multiple Formats**: JSON, CSV, TXT, and HTML export options
- **Data Integration**: Excel-compatible formats for further analysis
- **Preview Functionality**: In-app preview before downloading
- **Batch Operations**: Process multiple data types simultaneously

### 🎨 **User Experience**
- **Dark Theme**: Modern, eye-friendly dark interface
- **Responsive Design**: Works across desktop and mobile devices
- **Session Management**: Persistent scraping history and results
- **Real-time Feedback**: Live progress indicators and status updates
- **Error Handling**: Comprehensive error reporting with actionable solutions

### ⚙️ **Advanced Configuration**
- **Custom User Agents**: Configure browser identification
- **Timeout Management**: Adjustable request timeouts (5-60 seconds)
- **SSL Handling**: Configurable SSL certificate verification
- **Redirect Management**: Control HTTP redirect following

## 🏗️ Architecture

### **System Architecture**
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   Core Engine    │    │   Data Export   │
│   Web UI        │◄──►│   (scraper.py)   │◄──►│   (export.py)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Components    │    │   Configuration  │    │   Session       │
│   (UI Modules)  │    │   (config.py)    │    │   Management    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### **Technology Stack**
- **Frontend**: Streamlit (Python web framework)
- **Backend**: Python 3.8+ with custom scraping engine
- **Data Processing**: BeautifulSoup 4, Pandas, Requests
- **Export System**: Custom formatting for multiple data types

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8 or higher
- Modern web browser
- Internet connection

### **Installation & Setup**

#### **Option 1: Automated Setup (Windows)**
```bash
# Simply double-click the run.bat file
./run.bat
```

#### **Option 2: Manual Installation**
```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch application
streamlit run app.py
```

#### **Option 3: Alternative Launch**
```bash
python app.py
```

The application will be available at `http://localhost:8501`

## 📖 Usage Guide

### **Basic Workflow**
1. **Navigate** to the application in your web browser
2. **Enter URL** in the sidebar input field
3. **Select Data Types** using checkboxes for desired content
4. **Configure Settings** (optional) - user agent, timeout, SSL settings
5. **Start Scraping** - click the "Start Scraping" button
6. **View Results** - extracted data displayed in organized sections
7. **Export Data** - download in preferred format (JSON/CSV/TXT/HTML)

### **Testing & Examples**
Ready-to-use test websites for development and testing:
- **Quotes Collection**: `https://quotes.toscrape.com`
- **Book Catalog**: `https://books.toscrape.com`
- **Simple Test Page**: `https://example.com`
- **HTML Test Page**: `https://httpbin.org/html`

## 🔧 Technical Implementation

### **Core Scraping Process**
1. **HTTP Request**: Configurable GET request with custom headers
2. **HTML Parsing**: BeautifulSoup processes DOM structure
3. **Data Extraction**: Targeted extraction based on user selections
4. **Data Structuring**: Standardized format for all data types
5. **Results Presentation**: Streamlit components for data display
6. **Export Generation**: Multiple format support for data portability

### **Data Types & Extraction Methods**

| Data Type | HTML Elements | Processing Method |
|-----------|---------------|-------------------|
| Text Content | `body`, `div`, `span` | Recursive text extraction |
| Links | `<a>` tags | href + anchor text capture |
| Images | `<img>` tags | src, alt, title attributes |
| Tables | `<table>` elements | Pandas DataFrame conversion |
| Headings | `<h1>`-`<h6>` | Hierarchical structure preservation |
| Metadata | `<meta>`, `<title>` | SEO and page information |
| Paragraphs | `<p>` elements | Content sectioning |
| HTML Source | Complete document | Raw source preservation |
| UI Elements | `<div>`, `<form>`, `<button>` | Interactive component analysis |
| Code Snippets | `<code>`, `<pre>` | Syntax-highlighted content |

## 📈 Performance & Optimization

### **Efficiency Features**
- **Selective Processing**: Only extracts requested data types
- **Memory Management**: Streaming processing for large datasets
- **Connection Reuse**: HTTP keep-alive for improved performance
- **Compression Support**: Gzip/deflate content encoding
- **Error Recovery**: Graceful handling of malformed content

### **Scalability Considerations**
- **Session-based Storage**: In-memory processing with export capability
- **Modular Architecture**: Independent component loading
- **Configuration-driven**: Runtime behavior modification
- **Extensible Design**: Easy addition of new data extractors

## 🛡️ Security & Best Practices

### **Responsible Scraping**
- ✅ **Terms Compliance**: Respects website Terms of Service
- ✅ **Robots.txt Awareness**: Checks scraping permissions
- ✅ **Rate Limiting**: Reasonable request intervals
- ✅ **Legal Compliance**: Adheres to local regulations

### **Security Measures**
- **Input Validation**: URL and configuration sanitization
- **Error Handling**: Safe failure without information disclosure
- **SSL Support**: Secure connection handling
- **User Agent Declaration**: Identifies scraper purpose

## 🐛 Troubleshooting

### **Common Issues**

#### **Installation Problems**
- **Module Import Errors**: Ensure virtual environment activation
- **Python Version**: Requires Python 3.8 or higher
- **Dependencies**: Run `pip install -r requirements.txt`

#### **Runtime Issues**
- **Port Conflicts**: Streamlit auto-selects alternative ports
- **SSL Certificate Errors**: Toggle SSL verification in settings
- **Scraping Failures**: Check URL validity and website accessibility
- **Performance Issues**: Increase timeout for slow websites

#### **Data Extraction Problems**
- **Empty Results**: Verify website allows scraping, check robots.txt
- **JavaScript Content**: Tool focuses on static HTML content
- **Anti-scraping Protection**: Use test websites for development

## 📚 Documentation

For comprehensive technical documentation, see [`DOCUMENTATION.txt`](DOCUMENTATION.txt) which includes:
- Detailed architecture explanation
- Complete API documentation
- Development guidelines
- Performance optimization details

## 🤝 Contributing

This is a **final project** demonstrating web scraping concepts. While contributions are welcome, please note:

1. **Fork** the repository for your modifications
2. **Create** a feature branch for your changes
3. **Test** thoroughly with multiple websites
4. **Document** any new features or modifications
5. **Submit** pull requests with clear descriptions

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

## 🙏 Acknowledgments

- **BeautifulSoup** developers for the excellent HTML parsing library
- **Streamlit** team for the intuitive web framework
- **Python** community for comprehensive documentation and support
- **Testing websites** (quotes.toscrape.com, books.toscrape.com) for development support



<div align="center">

**🎓 Final Project - Web Scraping Application**

*Built with ❤️ in India | Comprehensive data extraction made simple*

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-FF4B4B.svg)](https://streamlit.io/)

</div>
