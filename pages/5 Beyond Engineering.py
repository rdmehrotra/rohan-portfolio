import streamlit as st

st.markdown("""
<style>
.block-container {
    max-width: none;
    padding-top: 1.6rem;
    padding-bottom: 1.5rem;
    padding-left: 1.4rem;
    padding-right: 1.4rem;
}

.gallery-title {
    text-align: center;
    font-size: 3.2rem;
    font-weight: 800;
    color: #00E5FF;
    text-shadow: 0 0 22px rgba(0,229,255,0.45);
    margin-bottom: 0.2rem;
}

.gallery-subtitle {
    text-align: center;
    font-size: 1.02rem;
    color: #cbd5e1;
    margin-bottom: 1.4rem;
}

.glow-line {
    width: 160px;
    height: 3px;
    margin: 0 auto 1.6rem auto;
    background: #00E5FF;
    box-shadow: 0 0 14px rgba(0,229,255,0.8);
    border-radius: 999px;
}

.photo-caption {
    color: #cbd5e1;
    font-size: 0.92rem;
    line-height: 1.5;
    margin-top: 0.45rem;
    margin-bottom: 0.75rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="gallery-title">Beyond Engineering</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="gallery-subtitle">A snippet of my baking.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

gallery_items = [
    {"image": "images/bake1.jpg", "caption": ""},
    {"image": "images/bake2.jpg", "caption": ""},
    {"image": "images/bake3.jpg", "caption": ""},
    {"image": "images/bake4.jpg", "caption": ""},
    {"image": "images/bake5.jpg", "caption": ""},
    {"image": "images/bake6.jpg", "caption": ""},
    {"image": "images/bake7.jpg", "caption": ""},
    {"image": "images/bake8.jpg", "caption": "I’m a huge latte and coffee person, so this one is making the gallery :)"},
    {"image": "images/bake9.jpg", "caption": "I’ve been baking since I was 9 years old!"},
]

for row_start in range(0, len(gallery_items), 3):
    cols = st.columns(3, gap="small")
    row_items = gallery_items[row_start:row_start + 3]

    for col, item in zip(cols, row_items):
        with col:
            st.image(item["image"], use_container_width=True)
            if item["caption"]:
                st.markdown(
                    f'<div class="photo-caption">{item["caption"]}</div>',
                    unsafe_allow_html=True
                )
