

import streamlit as st
from config import (
    SCRAPE_OPTIONS,
    EXPORT_FORMATS,
    DEFAULT_USER_AGENT,
    DEFAULT_TIMEOUT,
    MIN_TIMEOUT,
    MAX_TIMEOUT
)

def render_sidebar():
    with st.sidebar:
        st.header("Settings")

        url = st.text_input(
            "Website URL",
            placeholder="https://example.com"
        )

        st.subheader("Data to Extract")
        scrape_options = st.multiselect(
            "Select options:",
            SCRAPE_OPTIONS,
            default=["All Text", "Links"]
        )

        with st.expander("Advanced"):
            user_agent = st.text_area(
                "User Agent",
                value=DEFAULT_USER_AGENT,
                height=80
            )

            col1, col2 = st.columns(2)
            with col1:
                timeout = st.number_input(
                    "Timeout (sec)",
                    min_value=MIN_TIMEOUT,
                    max_value=MAX_TIMEOUT,
                    value=DEFAULT_TIMEOUT
                )

            with col2:
                follow_redirects = st.checkbox(
                    "Follow Redirects",
                    value=True
                )

            verify_ssl = st.checkbox(
                "Verify SSL",
                value=True
            )

        st.subheader("Export Format")
        export_format = st.selectbox(
            "Format:",
            EXPORT_FORMATS
        )

        scrape_button = st.button(
            "Scrape Website",
            use_container_width=True,
            type="primary"
        )

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
