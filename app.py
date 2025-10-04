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
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_styles()

if 'scraped_data' not in st.session_state:
    st.session_state.scraped_data = None

if 'scrape_history' not in st.session_state:
    st.session_state.scrape_history = []

if 'show_preview' not in st.session_state:
    st.session_state.show_preview = False

# Main header
st.title(APP_TITLE)
st.markdown("Just paste a URL and grab the data you need")

sidebar_values = render_sidebar()

tab1, tab2, tab3 = st.tabs(["Results", "History", "About"])

if sidebar_values['scrape_button']:
    url = sidebar_values['url']
    scrape_options = sidebar_values['scrape_options']

    if not url:
        st.error("Please enter a URL")
    elif not scrape_options:
        st.error("Please select scraping options")
    else:
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        with st.spinner("Scraping..."):
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
                st.error(f"Error: {error}")
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
                st.success(f"Completed in {elapsed_time:.2f}s")
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

st.caption("© 2025 Aryan Patel")
