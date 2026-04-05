import streamlit as st

st.markdown("""
<style>
.block-container {
    max-width: none;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

.resume-title {
    text-align: center;
    font-size: 3.2rem;
    font-weight: 700;
    color: #e5e7eb;
    margin-bottom: 1.5rem;
}

.button-row {
    margin-bottom: 1.4rem;
}

div[data-testid="stDownloadButton"] > button {
    width: 100%;
    height: 62px;
    border-radius: 12px;
    border: 1px solid rgba(0,229,255,0.18);
    background: rgba(255,255,255,0.03);
    color: #e5e7eb;
    font-size: 1.05rem;
    font-weight: 600;
    box-shadow: 0 0 14px rgba(0,229,255,0.06);
}

div[data-testid="stDownloadButton"] > button:hover {
    border: 1px solid rgba(0,229,255,0.35);
    color: #ffffff;
}

.linkedin-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    width: 100%;
    height: 62px;
    background: linear-gradient(90deg, #0A66C2, #0077b5);
    border-radius: 12px;
    color: white !important;
    font-weight: 600;
    font-size: 1.05rem;
    text-decoration: none;
    box-shadow: 0 0 14px rgba(10,102,194,0.45);
}

.resume-wrap {
    margin-top: 1.4rem;
    border-radius: 18px;
    padding: 0.75rem;
    background: rgba(255,255,255,0.06);
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="resume-title">Resume</div>', unsafe_allow_html=True)

with open("assets/rohan_mehrotra_resume.pdf", "rb") as f:
    pdf_bytes = f.read()

outer_left, center, outer_right = st.columns([0.12, 1, 0.12])

with center:
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.download_button(
            label="Download Resume",
            data=pdf_bytes,
            file_name="Rohan_Mehrotra_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <a class="linkedin-btn" href="https://www.linkedin.com/in/rohan-d-mehrotra/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20">
            Connect on LinkedIn
        </a>
        """, unsafe_allow_html=True)

st.markdown('<div class="resume-wrap">', unsafe_allow_html=True)
st.pdf(pdf_bytes, height=2200)
st.markdown('</div>', unsafe_allow_html=True)
