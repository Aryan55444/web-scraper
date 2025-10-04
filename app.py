import streamlit as st
import time

from config import APP_TITLE, APP_ICON
from utils import scrape_website
from components import (
    apply_custom_styles,
    render_sidebar,
    render_results_tab,
    render_history_tab,
    render_about_tab
)

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Web Scraper Pro - A powerful tool for ethical web scraping"
    }
)

apply_custom_styles()

if 'scraped_data' not in st.session_state:
    st.session_state.scraped_data = None

if 'scrape_history' not in st.session_state:
    st.session_state.scrape_history = []

if 'show_preview' not in st.session_state:
    st.session_state.show_preview = False

st.markdown(f'<h1 class="main-header">{APP_ICON} {APP_TITLE}</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align: center; color: #6c757d; margin-top: -1rem; font-size: 1.1rem; font-weight: 500;'>
        Extract data from websites with ease 🚀
    </p>
    <div style='text-align: center; margin-bottom: 2rem;'>
        <span style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                     padding: 0.5rem 1.5rem; 
                     border-radius: 20px; 
                     color: white; 
                     font-size: 0.85rem; 
                     font-weight: 600; 
                     box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
                     display: inline-block;
                     margin: 0 0.5rem;'>
            ✨ Modular Architecture
        </span>
        <span style='background: linear-gradient(135deg, #28a745 0%, #20c997 100%); 
                     padding: 0.5rem 1.5rem; 
                     border-radius: 20px; 
                     color: white; 
                     font-size: 0.85rem; 
                     font-weight: 600; 
                     box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
                     display: inline-block;
                     margin: 0 0.5rem;'>
            🎨 Beautiful UI
        </span>
        <span style='background: linear-gradient(135deg, #17a2b8 0%, #138496 100%); 
                     padding: 0.5rem 1.5rem; 
                     border-radius: 20px; 
                     color: white; 
                     font-size: 0.85rem; 
                     font-weight: 600; 
                     box-shadow: 0 4px 15px rgba(23, 162, 184, 0.3);
                     display: inline-block;
                     margin: 0 0.5rem;'>
            ⚡ Fast & Reliable
    </div>
    """,
    unsafe_allow_html=True
)

sidebar_values = render_sidebar()

tab1, tab2, tab3 = st.tabs(["📊 Results", "📜 History", "ℹ️ About"])

if sidebar_values['scrape_button']:
    url = sidebar_values['url']
    scrape_options = sidebar_values['scrape_options']
    
    if not url:
        st.error("❌ Please enter a URL to scrape!")
    elif not scrape_options:
        st.error("❌ Please select at least one scraping option!")
    else:
        # Add http:// prefix if missing
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        with st.spinner("🔄 Scraping website... Please wait..."):
            start_time = time.time()
            
            results, error = scrape_website(
                url=url,
                options=scrape_options,
                user_agent=sidebar_values['user_agent'],
                timeout=sidebar_values['timeout'],
                verify_ssl=sidebar_values['verify_ssl'],
                follow_redirects=sidebar_values['follow_redirects']
            )
            
            elapsed_time = time.time() - start_time
            
            if error:
                st.error(f"❌ Scraping Error: {error}")
                st.error(f"URL: {url}")
                st.error(f"Options: {scrape_options}")
               
                st.session_state.scrape_history.insert(0, {
                    'url': url,
                    'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
                    'status': 'Failed',
                    'time': f"{elapsed_time:.2f}s"
                })
            else:
                st.session_state.scraped_data = results
                
                st.session_state.scrape_history.insert(0, {
                    'url': url,
                    'timestamp': results['timestamp'],
                    'time': f"{elapsed_time:.2f}s"
                })
                st.success(f"✅ Successfully scraped in {elapsed_time:.2f} seconds!")
                st.info(f"📊 Extracted {len(results['data'])} data types: {', '.join(results['data'].keys())}")
                st.rerun()

with tab1:
    render_results_tab(
        st.session_state.scraped_data,
        sidebar_values['export_format']
    )

with tab2:
    render_history_tab(st.session_state.scrape_history)

with tab3:
    render_about_tab()

st.markdown("---")
st.markdown(
    """
    <div class="footer">
        <p><strong>Web Scraper Pro</strong> © 2025 | Made with ❤️ using Python and Streamlit 🎈</p>
        <p style='font-size: 0.85rem; color: #6c757d;'>
            Always scrape responsibly and ethically. Respect robots.txt and Terms of Service.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
