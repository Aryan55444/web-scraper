import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        .stApp {
            background: #1a1a1a;
        }

        .main .block-container {
            max-width: 1000px;
            padding: 1rem;
        }

        .main h1 {
            color: #ffffff;
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .main p {
            color: #b0b0b0;
            font-size: 1.1rem;
        }
        </style>
    """, unsafe_allow_html=True)
