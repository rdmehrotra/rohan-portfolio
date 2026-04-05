import streamlit as st
import base64

st.title("📄 Resume")

# ---------- LOAD PDF ----------
with open("assets/rohan_mehrotra_resume.pdf", "rb") as f:
    pdf_bytes = f.read()

# ---------- DOWNLOAD BUTTON ----------
st.download_button(
    label="📄 Download Resume",
    data=pdf_bytes,
    file_name="Rohan_Mehrotra_Resume.pdf",
    mime="application/pdf"
)

st.markdown("##")

# ---------- SAFE EMBED (WORKS ON STREAMLIT CLOUD) ----------
base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')

pdf_display = f"""
<embed 
    src="data:application/pdf;base64,{base64_pdf}" 
    width="100%" 
    height="800px" 
    type="application/pdf">
"""

st.markdown(pdf_display, unsafe_allow_html=True)

# ---------- LINKEDIN BUTTON ----------
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
    ">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20">
        Connect on LinkedIn
    </div>
</a>
""", unsafe_allow_html=True)
