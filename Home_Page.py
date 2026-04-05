import streamlit as st
import base64

# ---------- BACKGROUND IMAGE ----------
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

# ---------- DARK OVERLAY ----------
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
</style>
""", unsafe_allow_html=True)

# ---------- HERO STYLING ----------
st.markdown("""
<style>
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

# ---------- HERO CONTENT ----------
st.markdown("""
<div class="hero">
    <div class="name">Rohan Mehrotra</div>
    <div class="subtitle">Electrical Engineering @ Georgia Tech</div>
    <div class="tagline">Signal Processing | Embedded Systems | Intelligent Systems</div>
</div>
""", unsafe_allow_html=True)

# ---------- BUTTONS ----------
col1, col2 = st.columns(2)

# Resume button
with col1:
    with open("assets/resume.pdf", "rb") as file:
        st.download_button(
            label="📄 Resume",
            data=file,
            file_name="Rohan_Mehrotra_Resume.pdf",
            mime="application/pdf"
        )

# LinkedIn button
with col2:
    st.markdown("""
    <a href="https://www.linkedin.com/in/YOUR-LINKEDIN/" target="_blank" style="text-decoration:none;">
        <div style="
            display:inline-flex;
            align-items:center;
            gap:10px;
            background-color:#0A66C2;
            padding:10px 16px;
            border-radius:8px;
            color:white;
            font-weight:500;">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20">
            LinkedIn
        </div>
    </a>
    """, unsafe_allow_html=True)
