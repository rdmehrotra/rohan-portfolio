import streamlit as st
import base64
import streamlit.components.v1 as components

st.title("📄 Resume")

# ---------- LOAD PDF ----------
with open("assets/rohan_mehrotra_resume.pdf", "rb") as f:
    pdf_bytes = f.read()

# ---------- DOWNLOAD BUTTON ----------
col1, col2 = st.columns(2)

with col1:
    st.download_button(
        label="📄 Download Resume",
        data=pdf_bytes,
        file_name="Rohan_Mehrotra_Resume.pdf",
        mime="application/pdf"
    )

with col2:
    st.link_button("🔍 Open in New Tab", "/assets/rohan_mehrotra_resume.pdf")

st.markdown("##")

# ---------- DISPLAY PDF (THIS WORKS) ----------
base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

pdf_html = f"""
<div style="display:flex; justify-content:center;">
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="800px" 
        height="1000px" 
        style="border:none; border-radius:10px;">
    </iframe>
</div>
"""

components.html(pdf_html, height=1000)

# ---------- LINKEDIN ----------
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
