import streamlit as st
from pathlib import Path

st.set_page_config(page_title="OSINT Report", page_icon="🌍", layout="wide")

# --- Page Styling ---
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"] {
        height: 100%;
        width: 100%;
        margin: 0;
        padding: 0;
        background-color: #0E1117 !important;
    }

    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        height: calc(100vh - 3.5rem) !important;  /* leave space for Streamlit's top bar */
        width: 100vw !important;
        background-color: #0E1117 !important;
    }

    iframe {
        height: calc(100vh - 3.5rem) !important;
        width: 100vw !important;
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Load and display the HTML file ---
index_path = Path("osint_report.html")

if index_path.exists():
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Wrapper with top and side padding
    full_html = f"""
    <div style="
        background-color:#0E1117;
        color:white;
        height:calc(100vh - 3.5rem);
        width:100vw;
        overflow:auto;
        padding:1rem 2rem;  /* 1rem top/bottom, 2rem left/right */
        box-sizing:border-box;">
        {html_content}
    </div>
    """

    st.components.v1.html(full_html, height=0, scrolling=False)
else:
    st.warning(f"{index_path} not found. Please make sure it's in the repo root.")
