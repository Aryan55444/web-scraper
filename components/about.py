

import streamlit as st
from config import APP_VERSION, TEST_WEBSITES

def render_about_tab():
    
    st.subheader("ℹ️ About Web Scraper Pro")
    
    _display_features()
    _display_how_to_use()
    _display_test_websites()
    _display_important_notes()
    _display_tech_stack()
    _display_version()

def _display_features():
    
    st.markdown("### Key Features\n- Web scraping with multiple data extraction options\n- HTML and code snippet extraction\n- Export to various formats\n- Scraping history tracking")

def _display_how_to_use():
    
    st.markdown("### How to Use\n1. Enter a URL in the sidebar\n2. Select data extraction options\n3. Click 'Scrape' to start\n4. View and export results")

def _display_test_websites():
    
    st.markdown("### Test Websites")
    
    for name, url in TEST_WEBSITES.items():
        st.markdown(f"- **{name}**: [{url}]({url})")
    
    st.warning("These are sample websites for testing. Always respect website terms of service.")
    
    st.markdown("---")

def _display_important_notes():
    
    st.markdown("### Important Notes\n- Some websites may block scraping attempts\n- Always respect robots.txt and website terms\n- Performance may vary based on website size and complexity")

def _display_tech_stack():
    
    st.markdown("### Tech Stack\n- Python\n- Streamlit\n- BeautifulSoup4\n- Requests\n- Pandas")

def _display_version():
    
    st.markdown(f"**Version:** {APP_VERSION}")
