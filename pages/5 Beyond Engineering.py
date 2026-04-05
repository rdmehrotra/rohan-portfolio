import os
import base64
import streamlit as st
from streamlit_clickable_images import clickable_images

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
    margin-bottom: 1.6rem;
}

.selected-title {
    text-align: center;
    font-size: 1.9rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="gallery-title">🧁 Beyond Engineering</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="gallery-subtitle">Click any photo to enlarge it.</div>',
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

def encode_image(path):
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    ext = path.split(".")[-1].lower()
    if ext == "jpg":
        ext = "jpeg"
    return f"data:image/{ext};base64,{encoded}"

existing_items = [item for item in gallery_items if os.path.exists(item["image"])]

if not existing_items:
    st.error("No baking images were found in the images folder.")
    st.stop()

if "selected_bake_index" not in st.session_state:
    st.session_state.selected_bake_index = 0

image_urls = [encode_image(item["image"]) for item in existing_items]

clicked = clickable_images(
    image_urls,
    titles=[item["title"] for item in existing_items],
    div_style={
        "display": "flex",
        "justify-content": "center",
        "flex-wrap": "wrap",
        "gap": "16px",
        "margin-bottom": "10px",
    },
    img_style={
        "width": "31%",
        "min-width": "220px",
        "border-radius": "16px",
        "border": "2px solid rgba(0,229,255,0.18)",
        "box-shadow": "0 0 16px rgba(0,229,255,0.08)",
        "cursor": "pointer",
        "object-fit": "cover",
    },
    key="baking_gallery",
)

if clicked > -1:
    st.session_state.selected_bake_index = clicked

selected_item = existing_items[st.session_state.selected_bake_index]

st.markdown('<div class="selected-card">', unsafe_allow_html=True)
st.markdown(
    f'<div class="selected-title">{selected_item["title"]}</div>',
    unsafe_allow_html=True
)
st.image(selected_item["image"], use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
