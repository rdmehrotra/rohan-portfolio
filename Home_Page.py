import streamlit as st
import base64

st.set_page_config(page_title="Rohan Mehrotra", layout="wide")

def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{data}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}

    /* Kill the ugly top Streamlit bar */
    header[data-testid="stHeader"] {{
        background: transparent;
        height: 0rem;
    }}

    /* Hide the top-right toolbar icons too */
    div[data-testid="stToolbar"] {{
        display: none;
    }}

    /* Pull the page content upward */
    .block-container {{
        padding-top: 0rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }}

    /* Make sure the main area stays transparent */
    [data-testid="stAppViewContainer"] {{
        background: transparent;
    }}

    [data-testid="stAppViewContainer"] > .main {{
        background: transparent;
    }}

    /* Dark overlay over the image */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.42);
        z-index: -1;
    }}

    .hero {{
        text-align: center;
        padding-top: 130px;
        padding-bottom: 80px;
    }}

    .name {{
        font-size: 72px;
        font-weight: 800;
        color: #00E5FF;
        text-shadow: 0 0 22px rgba(0,229,255,0.6);
    }}

    .subtitle {{
        font-size: 28px;
        color: #E5E7EB;
        margin-top: 14px;
    }}

    .tagline {{
        font-size: 20px;
        color: #CBD5E1;
        margin-top: 20px;
    }}

    .glow-line {{
        width: 230px;
        height: 4px;
        margin: 30px auto 0 auto;
        background: #00E5FF;
        box-shadow: 0 0 16px rgba(0,229,255,0.8);
        border-radius: 999px;
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("images/background1.jpg")

st.markdown("""
<div class="hero">
    <div class="name">Rohan Mehrotra</div>
    <div class="subtitle">Electrical Engineering @ Georgia Tech</div>
    <div class="glow-line"></div>
</div>
""", unsafe_allow_html=True)
