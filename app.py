import streamlit as st
from pathlib import Path

# --- Page config ---
st.set_page_config(page_title="OSINT Report", page_icon="🌍", layout="wide")

# --- Dark theme injection ---
st.markdown(
    """
    <style>
    /* Main app background */
    .css-18e3th9, .main {
        background-color: #0E1117 !important;
    }

    /* Top menu / banner */
    header, .css-1v3fvcr {
        background-color: #0E1117 !important;
        color: white !important;
    }

    /* Sidebar background */
    .css-1d391kg {
        background-color: #0E1117 !important;
    }

    /* Main container (content area) */
    .block-container {
        background-color: #0E1117 !important;
        color: white !important;
        padding-top: 1rem;  /* small top padding for entire content */
    }

    /* Force all text to white */
    h1, h2, h3, h4, h5, h6, p, span, li, a {
        color: white !important;
    }

    /* Header1 padding (slightly more to avoid banner overlap) */
    h1 {
        padding-top: 1.1rem;  /* ~17px */
        margin-top: 0;         /* remove extra margin */
    }

    /* Remove extra margins/padding between blocks */
    .block-container > * {
        margin-top: 0;
        margin-bottom: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)




# --- Load HTML report ---
index_path = Path("osint_report.html")

if index_path.exists():
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Wrap report in a dark div
    html_content_dark = f"""
    <div style="background-color:#0E1117; color:white; padding:10px;">
        {html_content}
    </div>
    """

    st.components.v1.html(html_content_dark, height=1000, scrolling=True)
else:
    st.warning(f"{index_path} not found. Please make sure it's in the repo root.")
