import streamlit as st

st.set_page_config(page_title="Under Maintenance", page_icon="🔧", layout="centered")

st.markdown(
    """
    <style>
    .main {
        text-align: center;
        padding-top: 100px;
    }
    h1 {
        font-size: 64px;
        color: #FF6B6B;
    }
    p {
        font-size: 24px;
        color: #333333;
    }
    </style>
    <div class="main">
        <h1>🚧 Under Maintenance 🚧</h1>
        <p>We’ll be back shortly. Thank you for your patience!</p>
    </div>
    """ ,
    unsafe_allow_html=True,
)
