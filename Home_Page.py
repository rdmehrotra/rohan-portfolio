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
        background-position: 10% center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

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

    .block-container {{
        padding-top: 0rem !important;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        max-width: none;
    }}

    [data-testid="stAppViewContainer"] {{
        background: transparent;
    }}

    [data-testid="stAppViewContainer"] > .main {{
        background: transparent;
    }}

    section[data-testid="stSidebar"] {{
        background: rgba(8, 12, 18, 0.68);
        backdrop-filter: blur(8px);
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(255, 255, 255, 0.08);
        z-index: -1;
    }}

    .hero {{
        min-height: 88vh;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding-right: 8%;
    }}

    .hero-panel {{
        width: min(720px, 48vw);
        text-align: center;
    }}

    .name {{
        font-size: 78px;
        font-weight: 800;
        color: #050505;
        line-height: 1.04;
        text-shadow:
            0 0 6px rgba(255,255,255,0.18),
            0 0 14px rgba(255,255,255,0.12),
            0 0 22px rgba(0,229,255,0.22);
    }}

    .subtitle {{
        font-size: 30px;
        color: rgba(20,20,20,0.82);
        margin-top: 18px;
        text-shadow:
            0 0 6px rgba(255,255,255,0.16),
            0 0 12px rgba(0,229,255,0.14);
    }}

    .glow-line {{
        width: 260px;
        height: 4px;
        margin: 28px auto 0 auto;
        background: #00E5FF;
        box-shadow: 0 0 16px rgba(0,229,255,0.8);
        border-radius: 999px;
    }}

    @media (max-width: 900px) {{
        .hero {{
            justify-content: center;
            padding-right: 0;
            min-height: 82vh;
        }}

        .hero-panel {{
            width: 90%;
        }}

        .name {{
            font-size: 56px;
        }}

        .subtitle {{
            font-size: 24px;
        }}

        .stApp {{
            background-position: 54% center;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

set_bg("images/background1.jpg")

st.markdown("""
<div class="hero">
    <div class="hero-panel">
        <div class="name">Rohan Mehrotra</div>
        <div class="subtitle">Electrical Engineering @ Georgia Tech</div>
        <div class="glow-line"></div>
    </div>
</div>
""", unsafe_allow_html=True)
