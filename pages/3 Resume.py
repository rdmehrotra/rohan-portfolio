import streamlit as st
import base64

st.title("📄 Resume")

# ---------- EMBED PDF (SCROLLABLE) ----------
def display_pdf(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f"""
    <iframe 
        src="data:application/pdf;base64,{base64_pdf}" 
        width="100%" 
        height="800px" 
        type="application/pdf">
    </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

display_pdf("assets/rohan_mehrotra_resume.pdf")

# ---------- BUTTONS ----------
st.markdown("##")

col1, col2 = st.columns(2)

# Download button
with col1:
    with open("assets/rohan_mehrotra_resume.pdf", "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Rohan_Mehrotra_Resume.pdf",
            mime="application/pdf"
        )

# LinkedIn button (sexy version)
with col2:
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
