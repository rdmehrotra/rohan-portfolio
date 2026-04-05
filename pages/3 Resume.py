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

.linkedin-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(90deg, #0A66C2, #0077b5);
    padding: 12px 20px;
    border-radius: 12px;
    color: white !important;
    font-weight: 600;
    text-decoration: none;
    box-shadow: 0 0 14px rgba(10,102,194,0.45);
}

.resume-wrap {
    margin-top: 1.5rem;
    border-radius: 18px;
    padding: 0.75rem;
    background: rgba(255,255,255,0.06);
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="resume-title">📄 Resume</div>', unsafe_allow_html=True)

with open("assets/rohan_mehrotra_resume.pdf", "rb") as f:
    pdf_bytes = f.read()

top1, top2 = st.columns([1.2, 1])

with top1:
    st.download_button(
        label="📄 Download Resume",
        data=pdf_bytes,
        file_name="Rohan_Mehrotra_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )

with top2:
    st.markdown("""
    <a class="linkedin-btn" href="https://www.linkedin.com/in/YOUR-LINKEDIN/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20">
        Connect on LinkedIn
    </a>
    """, unsafe_allow_html=True)

st.markdown('<div class="resume-wrap">', unsafe_allow_html=True)
st.pdf(pdf_bytes, height=2200)
st.markdown('</div>', unsafe_allow_html=True)
