

import streamlit as st
from config import (
    SCRAPE_OPTIONS,
    EXPORT_FORMATS,
    DEFAULT_USER_AGENT,
    DEFAULT_TIMEOUT,
    MIN_TIMEOUT,
    MAX_TIMEOUT,
    TEST_WEBSITES
)

def render_sidebar():
    
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        url = st.text_input(
            "🔗 Enter URL to Scrape",
            placeholder="https://example.com",
            help="Enter the full URL of the website you want to scrape"
        )
        
        with st.expander("🧪 Test Websites", expanded=False):
            st.markdown("Click to copy:")
            for name, test_url in TEST_WEBSITES.items():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.text(name)
                with col2:
                    if st.button("📋", key=f"copy_{name}"):
                        st.code(test_url, language=None)
            
        st.subheader("📦 Data to Extract")
        scrape_options = st.multiselect(
            "Select what to scrape:",
            SCRAPE_OPTIONS,
            default=["All Text", "Links"],
            help="Choose the types of data you want to extract from the webpage"
        )
        
        with st.expander("🔧 Advanced Settings"):
            user_agent = st.text_area(
                "User Agent",
                value=DEFAULT_USER_AGENT,
                height=100,
                help="Identifies your scraper to the web server"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                timeout = st.number_input(
                    "Timeout (sec)",
                    min_value=MIN_TIMEOUT,
                    max_value=MAX_TIMEOUT,
                    value=DEFAULT_TIMEOUT,
                    help="Maximum time to wait for server response"
                )
            
            with col2:
                follow_redirects = st.checkbox(
                    "Follow Redirects",
                    value=True,
                    help="Follow HTTP redirects (301, 302, etc.)"
                )
            
            verify_ssl = st.checkbox(
                "Verify SSL Certificate",
                value=True,
                help="Verify the website's SSL certificate (uncheck for self-signed certificates)"
            )
        
        st.subheader("📥 Export Options")
        export_format = st.selectbox(
            "Export Format",
            EXPORT_FORMATS,
            help="Choose the format for downloading scraped data"
        )
        
        st.markdown("---")
        scrape_button = st.button(
            "🚀 Start Scraping",
            use_container_width=True,
            type="primary"
        )
        
        st.markdown("---")
        st.caption("💡 **Tip**: Test with scraper-friendly websites first!")
    
    return {
        'url': url,
        'scrape_options': scrape_options,
        'user_agent': user_agent,
        'timeout': timeout,
        'follow_redirects': follow_redirects,
        'verify_ssl': verify_ssl,
        'export_format': export_format,
        'scrape_button': scrape_button
    }
