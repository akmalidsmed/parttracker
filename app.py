import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Monitoring Pengambilan Part", layout="wide")

st.markdown("""<style>
footer {visibility: hidden;}
</style>""", unsafe_allow_html=True)

st.sidebar.title("Kontrol")
st.sidebar.markdown("Upload file HTML asli atau gunakan tampilan bawaan.")
uploaded = st.sidebar.file_uploader("Upload file HTML", type=["html"])
height = st.sidebar.slider("Tinggi iframe (px)", 600, 800, 1100)

if uploaded:
    html = uploaded.read().decode('utf-8')
else:
    assets_path = os.path.join(os.path.dirname(__file__), "assets", "index.html")
    with open(assets_path, "r", encoding="utf-8") as f:
        html = f.read()

components.html(html, height=height, scrolling=True)
