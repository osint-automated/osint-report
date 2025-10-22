import streamlit as st
from pathlib import Path

st.set_page_config(page_title="OSINT Report", page_icon="🌍", layout="wide")

# Dark theme for Streamlit app itself
st.markdown(
    """
    <style>
    /* Dark background for Streamlit app */
    body, .css-18e3th9, .main {
        background-color: #121212;
        color: white;
    }

    /* Force text colors */
    h1, h2, h3, h4, h5, h6, p, span, li, a {
        color: white !important;
    }

    /* Optional: scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #555;
        border-radius: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

index_path = Path("osint_report.html")

if index_path.exists():
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Wrap HTML in a dark background container with white text
    html_content_dark = f"""
    <div style="background-color:#121212; color:white; padding:10px;">
        {html_content}
    </div>
    """

    st.components.v1.html(html_content_dark, height=1000, scrolling=True)
else:
    st.warning(f"{index_path} not found. Please make sure it's in the repo root.")
