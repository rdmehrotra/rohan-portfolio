import streamlit as st

st.title("📄 Resume")

# ---------- SHOW PDF (WORKS WITH STREAMLIT CLOUD) ----------
with open("assets/rohan_mehrotra_resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Download Resume",
    data=PDFbyte,
    file_name="Rohan_Mehrotra_Resume.pdf",
    mime='application/octet-stream'
)

st.markdown("##")

# THIS DISPLAYS THE PDF PROPERLY
st.write("### Preview")
st.pdf(PDFbyte)  # ← THIS IS THE FIX

# ---------- LINKEDIN BUTTON ----------
st.markdown("""
<a href="https://www.linkedin.com/in/YOUR-LINKEDIN/" target="_blank" style="text-decoration:none;">
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
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20">
        Connect on LinkedIn
    </div>
</a>
""", unsafe_allow_html=True)
