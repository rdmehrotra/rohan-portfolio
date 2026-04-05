import os
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

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18) !important;
    border-radius: 20px !important;
    padding: 1rem !important;
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
}

.selected-title {
    font-size: 1.9rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.35rem;
}

.selected-text {
    color: #dbe4ee;
    font-size: 1rem;
    line-height: 1.7;
}

.rating-pill {
    display: inline-block;
    padding: 0.42rem 0.82rem;
    margin-top: 0.9rem;
    border-radius: 999px;
    background: rgba(0,229,255,0.11);
    color: #a5f3fc;
    font-size: 0.92rem;
    border: 1px solid rgba(0,229,255,0.18);
}

.thumb-note {
    text-align: center;
    color: #cbd5e1;
    font-size: 0.95rem;
    margin-top: 0.35rem;
    margin-bottom: 0.5rem;
}

.gallery-gap {
    height: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="gallery-title">🧁 Baking Gallery</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="gallery-subtitle">Click a bake below to enlarge it.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

# Change these captions / ratings however you want
gallery_items = [
    {"title": "Bake 1", "image": "bake 1.jpg", "caption": "Bake 1", "rating": "⭐"},
    {"title": "Bake 2", "image": "bake 2.jpg", "caption": "Bake 2", "rating": "⭐"},
    {"title": "Bake 3", "image": "bake 3.jpg", "caption": "Bake 3", "rating": "⭐"},
    {"title": "Bake 4", "image": "bake 4.jpg", "caption": "Bake 4", "rating": "⭐"},
    {"title": "Bake 5", "image": "bake 5.jpg", "caption": "Bake 5", "rating": "⭐"},
    {"title": "Bake 6", "image": "bake 6.jpg", "caption": "Bake 6", "rating": "⭐"},
    {"title": "Bake 7", "image": "bake 7.jpg", "caption": "Bake 7", "rating": "⭐"},
    {"title": "Bake 8", "image": "bake 8.jpg", "caption": "Bake 8", "rating": "⭐"},
    {"title": "Bake 9", "image": "bake 9.jpg", "caption": "Bake 9", "rating": "⭐"},
]

if "selected_bake_index" not in st.session_state:
    st.session_state.selected_bake_index = 0

selected_item = gallery_items[st.session_state.selected_bake_index]

# Enlarged selected bake
with st.container(border=True):
    left, right = st.columns([1.25, 1], gap="large", vertical_alignment="center")

    with left:
        st.image(os.path.join("images", selected_item["image"]), use_container_width=True)

    with right:
        st.markdown(
            f'<div class="selected-title">{selected_item["title"]}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="selected-text">{selected_item["caption"]}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="rating-pill">{selected_item["rating"]}</div>',
            unsafe_allow_html=True
        )

st.markdown('<div class="gallery-gap"></div>', unsafe_allow_html=True)

# 3x3 clickable-style grid
for row_start in range(0, len(gallery_items), 3):
    cols = st.columns(3, gap="large")
    row_items = gallery_items[row_start:row_start+3]

    for col, item in zip(cols, row_items):
        with col:
            with st.container(border=True):
                st.image(os.path.join("images", item["image"]), use_container_width=True)
                st.markdown(
                    f'<div class="thumb-note">{item["title"]}</div>',
                    unsafe_allow_html=True
                )
                if st.button(f"Open {item['title']}", key=item["title"], use_container_width=True):
                    st.session_state.selected_bake_index = gallery_items.index(item)
                    st.rerun()
