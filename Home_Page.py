import streamlit as st
import base64

st.set_page_config(page_title="Rohan Mehrotra", layout="wide")

def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{data}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* hide streamlit top stuff */
    header[data-testid="stHeader"] {{
        display: none;
    }}

    div[data-testid="stToolbar"] {{
        display: none;
    }}

    div[data-testid="stDecoration"] {{
        display: none;
    }}

    div[data-testid="stStatusWidget"] {{
        display: none;
    }}

    /* remove default top spacing */
    .block-container {{
        padding-top: 0rem !important;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: none;
    }}

    /* keep everything transparent so the image shows */
    [data-testid="stAppViewContainer"] {{
        background: transparent;
    }}

    [data-testid="stAppViewContainer"] > .main {{
        background: transparent;
    }}

    section[data-testid="stSidebar"] {{
        background: rgba(7, 12, 20, 0.82);
        backdrop-filter: blur(6px);
    }}

    /* dark overlay over the photo */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.38);
        z-index: -1;
    }}

    .hero {{
        text-align: center;
        padding-top: 120px;
        padding-bottom: 80px;
    }}

    .name {{
        font-size: 72px;
        font-weight: 800;
        color: #00E5FF;
        text-shadow: 0 0 22px rgba(0,229,255,0.60);
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

set_bg("images/background4.jpg")

st.markdown("""
<div class="hero">
    <div class="name">Rohan Mehrotra</div>
    <div class="subtitle">Electrical Engineering @ Georgia Tech</div>
    <div class="glow-line"></div>
</div>
""", unsafe_allow_html=True)
