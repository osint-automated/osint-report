import streamlit as st
from pathlib import Path

st.set_page_config(page_title="OSINT Report", page_icon="🌍", layout="wide")

index_path = Path("osint_report.html")

if index_path.exists():
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=1000, scrolling=True)
else:
    st.warning(f"{index_path} not found. Please make sure it's in the repo root.")