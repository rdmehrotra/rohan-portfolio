import os
import streamlit as st
from streamlit_image_select import image_select

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

.selected-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18);
    border-radius: 22px;
    padding: 1rem;
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
    margin-top: 2rem;
}

.selected-title {
    text-align: center;
    font-size: 1.9rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.9rem;
}

.selected-caption {
    text-align: center;
    color: #cbd5e1;
    font-size: 1rem;
    margin-top: 0.75rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="gallery-title">🧁 Beyond Engineering</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="gallery-subtitle">Click any bake to enlarge it.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

gallery_items = [
    {"title": "Bake 1", "image": "images/bake1.jpg", "caption": "Bake 1"},
    {"title": "Bake 2", "image": "images/bake2.jpg", "caption": "Bake 2"},
    {"title": "Bake 3", "image": "images/bake3.jpg", "caption": "Bake 3"},
    {"title": "Bake 4", "image": "images/bake4.jpg", "caption": "Bake 4"},
    {"title": "Bake 5", "image": "images/bake5.jpg", "caption": "Bake 5"},
    {"title": "Bake 6", "image": "images/bake6.jpg", "caption": "Bake 6"},
    {"title": "Bake 7", "image": "images/bake7.jpg", "caption": "Bake 7"},
    {"title": "Bake 8", "image": "images/bake8.jpg", "caption": "Bake 8"},
    {"title": "Bake 9", "image": "images/bake9.jpg", "caption": "Bake 9"},
]

existing_items = [item for item in gallery_items if os.path.exists(item["image"])]

if not existing_items:
    st.error("No baking images were found in the images folder.")
    st.stop()

default_index = 0
selected_image = image_select(
    label="",
    images=[item["image"] for item in existing_items],
    captions=[item["title"] for item in existing_items],
    use_container_width=True,
    index=default_index,
    return_value="index",
)

if selected_image is None:
    selected_image = 0

selected_item = existing_items[selected_image]

st.markdown('<div class="selected-card">', unsafe_allow_html=True)
st.markdown(
    f'<div class="selected-title">{selected_item["title"]}</div>',
    unsafe_allow_html=True
)
st.image(selected_item["image"], use_container_width=True)
st.markdown(
    f'<div class="selected-caption">{selected_item["caption"]}</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
