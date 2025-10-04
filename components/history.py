

import streamlit as st
import pandas as pd

def render_history_tab(scrape_history):
    
    st.subheader("Scraping History")
    
    if scrape_history:
        _display_history_table(scrape_history)
        _display_history_actions()
    else:
        _display_empty_history()

def _display_history_table(history):
    
    df = pd.DataFrame(history)
    
    df.insert(0, '#', range(1, len(df) + 1))
    
    st.dataframe(
        df,
        use_container_width=True,
        column_config={
            "#": st.column_config.NumberColumn(
                "#",
                help="Entry number",
                width="small"
            ),
            "url": st.column_config.LinkColumn(
                "URL",
                help="The scraped website URL",
                max_chars=50
            ),
            "timestamp": st.column_config.TextColumn(
                "Timestamp",
                help="When the scraping occurred"
            ),
            "status": st.column_config.TextColumn(
                "Status",
                help="Success or failure"
            ),
            "time": st.column_config.TextColumn(
                "Duration",
                help="Time taken to scrape"
            )
        },
        hide_index=True
    )
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Scrapes", len(history))
    
    with col2:
        success_count = sum(1 for h in history if h.get('status') == 'Success')
        st.metric("Successful", success_count)
    
    with col3:
        fail_count = len(history) - success_count
        st.metric("Failed", fail_count)

def _display_history_actions():
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Clear History", use_container_width=True):
            st.session_state.scrape_history = []
            st.success("History cleared!")
            st.rerun()
    
    with col2:
        if st.button("Export History", use_container_width=True):
            df = pd.DataFrame(st.session_state.scrape_history)
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="scraping_history.csv",
                mime="text/csv",
                use_container_width=True
            )

def _display_empty_history():
    
    st.info("No scraping history yet. Start scraping to see your activity here!")
    
    st.markdown("Start by entering a URL in the sidebar and clicking 'Scrape'.")
