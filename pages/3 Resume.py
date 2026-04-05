import streamlit as st

st.title("📄 Resume")

with open("assets/rohan_mehrotra_resume.pdf", "rb") as f:
    pdf_bytes = f.read()

# Buttons
col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "📄 Download Resume",
        data=pdf_bytes,
        file_name="Rohan_Mehrotra_Resume.pdf",
        mime="application/pdf"
    )

with col2:
    st.link_button("🔍 Open Resume", "/assets/rohan_mehrotra_resume.pdf")

st.markdown("##")

# ✅ THIS IS THE CLEAN WORKING VIEWER
st.pdf(pdf_bytes)

# LinkedIn
st.markdown("""
<a href="https://www.linkedin.com/in/rohan-d-mehrotra/" target="_blank" style="text-decoration:none;">
    <div style="
        display:inline-flex;
        align-items:center;
        gap:10px;
        background: linear-gradient(90deg, #0A66C2, #0077b5);
        padding:12px 18px;
        border-radius:10px;
        color:white;
        font-weight:600;
        box-shadow: 0 0 10px rgba(10,102,194,0.5);
        margin-top:20px;
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20">
        Connect on LinkedIn
    </div>
</a>
""", unsafe_allow_html=True)
