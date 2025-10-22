import streamlit as st
from pathlib import Path

st.set_page_config(page_title="OSINT Report", page_icon="🌍", layout="wide")

# Streamlit dark theme + remove top padding/margins
st.markdown(
    """
    <style>
    /* Dark background for Streamlit app */
    body, .main, .block-container {
        background-color: #0E1117;
        color: white;
    }

    /* Force all text to white */
    h1, h2, h3, h4, h5, h6, p, span, li, a {
        color: white !important;
    }

    /* Remove Streamlit top padding/margin */
    .css-18e3th9, .main, .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        margin-top: 0rem;
    }

    /* Optional: remove extra margin below headers */
    .block-container > * {
        margin-top: 0;
        margin-bottom: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

index_path = Path("osint_report.html")

if index_path.exists():
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Embed HTML with no padding/margin
    html_content_dark = f"""
    <div style="background-color:#0E1117; color:white; padding:0; margin:0;">
        {html_content}
    </div>
    """

    st.components.v1.html(html_content_dark, height=1000, scrolling=True)
else:
    st.warning(f"{index_path} not found. Please make sure it's in the repo root.")
