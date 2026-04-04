import streamlit as st

st.markdown("""
<style>
.hero {
    text-align: center;
    padding-top: 60px;
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

<div class="hero">
    <div class="name">Rohan Mehrotra</div>
    <div class="subtitle">Electrical Engineering @ Georgia Tech</div>
    <div class="tagline">Signal Processing • Embedded Systems • AI Applications</div>
</div>
""", unsafe_allow_html=True)
