import streamlit as st
import base64

st.set_page_config(page_title="Rohan Mehrotra", layout="wide")

def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{data}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("images/background.jpg")

st.markdown("""
<style>
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(10, 15, 25, 0.7);
    z-index: -1;
}

.hero {
    text-align: center;
    padding-top: 80px;
    padding-bottom: 40px;
}

.name {
    font-size: 60px;
    font-weight: 700;
    color: #00E5FF;
    text-shadow: 0 0 20px rgba(0,229,255,0.6);
}

.subtitle {
    font-size: 24px;
    color: #cbd5e1;
    margin-top: 10px;
}

.tagline {
    font-size: 18px;
    color: #94a3b8;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="name">Rohan Mehrotra</div>
    <div class="subtitle">Electrical Engineering @ Georgia Tech</div>
    <div class="tagline">Signal Processing | Embedded Systems | Intelligent Systems</div>
</div>
""", unsafe_allow_html=True)
