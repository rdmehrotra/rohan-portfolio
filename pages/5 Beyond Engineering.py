import streamlit as st

st.markdown("""
<style>
.block-container {
    max-width: none;
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2.75rem;
    padding-right: 2.75rem;
}

.gallery-title {
    text-align: center;
    font-size: 3.4rem;
    font-weight: 800;
    color: #00E5FF;
    text-shadow: 0 0 22px rgba(0,229,255,0.45);
    margin-bottom: 0.25rem;
}

.gallery-subtitle {
    text-align: center;
    font-size: 1.08rem;
    color: #cbd5e1;
    margin-bottom: 2.2rem;
}

.glow-line {
    width: 180px;
    height: 3px;
    margin: 0 auto 2.3rem auto;
    background: #00E5FF;
    box-shadow: 0 0 14px rgba(0,229,255,0.8);
    border-radius: 999px;
}

.bake-label {
    text-align: center;
    color: #cbd5e1;
    font-size: 0.95rem;
    margin-top: 0.45rem;
    margin-bottom: 1.1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="gallery-title">🧁 Beyond Engineering</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="gallery-subtitle">A little gallery of some of my baking.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

gallery_items = [
    {"title": "Bake 1", "image": "images/bake1.jpg"},
    {"title": "Bake 2", "image": "images/bake2.jpg"},
    {"title": "Bake 3", "image": "images/bake3.jpg"},
    {"title": "Bake 4", "image": "images/bake4.jpg"},
    {"title": "Bake 5", "image": "images/bake5.jpg"},
    {"title": "Bake 6", "image": "images/bake6.jpg"},
    {"title": "Bake 7", "image": "images/bake7.jpg"},
    {"title": "Bake 8", "image": "images/bake8.jpg"},
    {"title": "Bake 9", "image": "images/bake9.jpg"},
]

for row_start in range(0, len(gallery_items), 3):
    cols = st.columns(3, gap="large")
    row_items = gallery_items[row_start:row_start + 3]

    for col, item in zip(cols, row_items):
        with col:
            st.image(item["image"], use_container_width=True)
            st.markdown(
                f'<div class="bake-label">{item["title"]}</div>',
                unsafe_allow_html=True
            )
