import os
import streamlit as st
from PIL import Image, ImageOps

st.markdown("""
<style>
.block-container {
    max-width: none;
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2.6rem;
    padding-right: 2.6rem;
}

.about-title {
    text-align: center;
    font-size: 4rem;
    font-weight: 800;
    color: #00E5FF;
    text-shadow: 0 0 24px rgba(0,229,255,0.45);
    margin-bottom: 0.2rem;
}

.about-subtitle {
    text-align: center;
    font-size: 1.22rem;
    color: #cbd5e1;
    margin-bottom: 1.8rem;
}

.glow-line {
    width: 210px;
    height: 4px;
    margin: 0 auto 2.2rem auto;
    background: #00E5FF;
    box-shadow: 0 0 16px rgba(0,229,255,0.85);
    border-radius: 999px;
}

div[data-testid="stImage"] img {
    border-radius: 18px;
}

.name {
    font-size: 3rem;
    font-weight: 780;
    color: #f8fafc;
    margin-bottom: 0.75rem;
}

.body-text {
    color: #dbe4ee;
    font-size: 1.15rem;
    line-height: 1.9;
}

.card-title {
    font-size: 1.95rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.75rem;
}

.card-text {
    color: #dbe4ee;
    font-size: 1.08rem;
    line-height: 1.85;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="about-title">About Me</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="about-subtitle">A little more about who I am outside of classes, code, and projects.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)


def cropped_image(path, size, centering=(0.5, 0.5)):
    if not os.path.exists(path):
        return None

    img = Image.open(path).convert("RGB")
    try:
        resample = Image.Resampling.LANCZOS
    except AttributeError:
        resample = Image.LANCZOS

    return ImageOps.fit(img, size, method=resample, centering=centering)


# HERO SECTION
left, right = st.columns([1.05, 1.35], gap="large", vertical_alignment="center")

with left:
    with st.container(border=True):
        hero_img = cropped_image("images/headshot.jpg", (1200, 1400), centering=(0.5, 0.4))
        if hero_img is not None:
            st.image(hero_img, use_container_width=True)

with right:
    with st.container(border=True):
        st.markdown('<div class="name">Hi, I’m Rohan.</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="body-text">
            I’m an Electrical Engineering student at Georgia Tech with interests in signal processing,
            embedded systems, and building things that feel interactive, thoughtful, and well-designed.
            I really enjoy the balance between technical problem-solving and creativity, which is probably
            why I care just as much about how something feels as I do about whether it works.
            <br><br>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("")

# ROW 1
col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.markdown('<div class="card-title">Carolina Hurricanes</div>', unsafe_allow_html=True)
        hurricanes_img = cropped_image("images/hurricanes.jpg", (1400, 900), centering=(0.5, 0.5))
        if hurricanes_img is not None:
            st.image(hurricanes_img, use_container_width=True)
        st.markdown(
            """
            <div class="card-text">
            I’m a longtime Carolina Hurricanes fan, so hockey has been one of those constants in my life for years.
            It is something I have always genuinely enjoyed, and it still feels like a piece of home for me.
            Even being away at school, it is one of those interests that still makes me feel connected to where I grew up.
            </div>
            """,
            unsafe_allow_html=True
        )

with col2:
    with st.container(border=True):
        st.markdown('<div class="card-title">Georgia Tech</div>', unsafe_allow_html=True)
        tech_img = cropped_image("images/gtcap.jpg", (1200, 900), centering=(0.5, 0.42))
        if tech_img is not None:
            st.image(tech_img, use_container_width=True)
        st.markdown(
            """
            <div class="card-text">
            Georgia Tech has become a huge part of my life, and at this point it feels very natural to be here.
            My sister graduated from Tech, so there was always a connection to it growing up, and now I get to
            build my own experience here. It has been challenging, exciting, and honestly a really rewarding place to grow.
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("")

# ROW 2
col3, col4 = st.columns(2, gap="large")

with col3:
    with st.container(border=True):
        st.markdown('<div class="card-title">Music</div>', unsafe_allow_html=True)
        music_img = cropped_image("images/music.jpg", (1000, 1350), centering=(0.5, 0.18))
        if music_img is not None:
            st.image(music_img, use_container_width=True)
        st.markdown(
            """
            <div class="card-text">
            Since 8, I have played the piano and flute and been in group ensembles (orchestras, quintets, band)
            for a total of 10 years now! That creative side still shows up in a lot of what I do now and what I
            try to implement even with my technical work.
            </div>
            """,
            unsafe_allow_html=True
        )

with col4:
    with st.container(border=True):
        st.markdown('<div class="card-title">Baking and coffee</div>', unsafe_allow_html=True)

        bake8_img = cropped_image("images/bake8.jpg", (1200, 700), centering=(0.5, 0.5))
        bake9_img = cropped_image("images/bake9.jpg", (1200, 700), centering=(0.5, 0.35))

        if bake8_img is not None:
            st.image(bake8_img, use_container_width=True)

        if bake9_img is not None:
            st.image(bake9_img, use_container_width=True)

        st.markdown(
            """
            <div class="card-text">
            I’ve been baking since I was 9 years old, so at this point it feels less like a hobby and more like part of who I am.
            I also really enjoy coffee shop hunting, especially in a cultural powerhouse like Atlanta.
            Check my Beyond Engineering page for more.
            </div>
            """,
            unsafe_allow_html=True
        )
