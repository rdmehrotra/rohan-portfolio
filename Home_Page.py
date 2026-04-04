import streamlit as st

st.markdown("""
<style>
/* Glow titles */
h1, h2, h3 {
    color: #00E5FF;
    text-shadow: 0 0 12px rgba(0,229,255,0.6);
}

/* Sidebar glow */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid rgba(0,229,255,0.2);
}

/* Cards (like STRIDE GPT boxes) */
.block-container {
    padding-top: 2rem;
}

div[data-testid="stExpander"] {
    border: 1px solid rgba(0,229,255,0.2);
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,229,255,0.1);
}
</style>
""", unsafe_allow_html=True)
st.title("Rohan Mehrotra")
st.subheader("Electrical Engineering @ Georgia Tech")

st.write("""
Welcome to my interactive portfolio.

Use the sidebar to explore:
- Portfolio
- Personal Dashboard
""")
