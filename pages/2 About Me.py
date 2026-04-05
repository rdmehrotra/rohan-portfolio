import os
import base64
import streamlit as st

st.markdown("""
<style>
.block-container {
    max-width: none;
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
}

.about-title {
    text-align: center;
    font-size: 3.4rem;
    font-weight: 800;
    color: #00E5FF;
    text-shadow: 0 0 22px rgba(0,229,255,0.45);
    margin-bottom: 0.2rem;
}

.about-subtitle {
    text-align: center;
    font-size: 1.08rem;
    color: #cbd5e1;
    margin-bottom: 2rem;
}

.glow-line {
    width: 170px;
    height: 3px;
    margin: 0 auto 2.2rem auto;
    background: #00E5FF;
    box-shadow: 0 0 14px rgba(0,229,255,0.8);
    border-radius: 999px;
}

.hero-wrap {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18);
    border-radius: 24px;
    padding: 1.2rem;
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
    margin-bottom: 1.4rem;
}

.info-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18);
    border-radius: 22px;
    padding: 1rem;
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
    min-height: 610px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.card-title {
    font-size: 1.45rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.65rem;
}

.name {
    font-size: 2.2rem;
    font-weight: 750;
    color: #f8fafc;
    margin-bottom: 0.5rem;
}

.body-text {
    color: #dbe4ee;
    font-size: 1.03rem;
    line-height: 1.75;
}

.card-text {
    color: #dbe4ee;
    font-size: 1rem;
    line-height: 1.7;
}

.fun-pill {
    display: inline-block;
    padding: 0.42rem 0.82rem;
    margin-right: 0.45rem;
    margin-bottom: 0.55rem;
    border-radius: 999px;
    background: rgba(0,229,255,0.11);
    color: #a5f3fc;
    font-size: 0.9rem;
    border: 1px solid rgba(0,229,255,0.18);
}

.card-img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    border-radius: 16px;
    margin-bottom: 0.9rem;
}

.card-img-stack {
    width: 100%;
    height: 155px;
    object-fit: cover;
    border-radius: 16px;
    margin-bottom: 0.7rem;
}

.quick-facts-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18);
    border-radius: 22px;
    padding: 1rem;
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="about-title">About Me</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="about-subtitle">A little more about who I am outside of classes, code, and projects.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)


def image_to_data_uri(path):
    if not os.path.exists(path):
        return None

    ext = path.split(".")[-1].lower()
    if ext == "jpg":
        ext = "jpeg"

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    return f"data:image/{ext};base64,{encoded}"


def single_image_html(path, class_name="card-img"):
    uri = image_to_data_uri(path)
    if not uri:
        return ""
    return f'<img src="{uri}" class="{class_name}">'


def stacked_images_html(paths):
    html = ""
    for path in paths:
        uri = image_to_data_uri(path)
        if uri:
            html += f'<img src="{uri}" class="card-img-stack">'
    return html


# Hero
left, right = st.columns([1, 1.45], gap="large", vertical_alignment="center")

with left:
    st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
    if os.path.exists("images/headshot.jpg"):
        st.image("images/headshot.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="hero-wrap">
        <div class="name">Hi, I’m Rohan.</div>
        <div class="body-text">
        I’m an Electrical Engineering student at Georgia Tech with interests in signal processing,
        embedded systems, and building things that feel interactive, thoughtful, and well-designed.
        I really enjoy the balance between technical problem-solving and creativity, which is probably
        why I care just as much about how something feels as I do about whether it works.
        <br><br>
        Outside of engineering, a lot of the things I love most are the ones that make life feel a little
        warmer and more fun — baking, coffee, music, and the kinds of small traditions and hobbies that
        people carry with them over time.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# Row 1
col1, col2 = st.columns(2, gap="large")

with col1:
    hurricanes_img = single_image_html("images/hurricanes.jpg")
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">Carolina Hurricanes</div>
        {hurricanes_img}
        <div class="card-text">
        I’m a longtime Carolina Hurricanes fan, so hockey has been one of those constants in my life for years.
        It is something I have always genuinely enjoyed, and it still feels like a piece of home for me.
        Even being away at school, it is one of those interests that still makes me feel connected to where I grew up.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    tech_img = single_image_html("images/gtcap.jpg")
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">Georgia Tech</div>
        {tech_img}
        <div class="card-text">
        Georgia Tech has become a huge part of my life, and at this point it feels very natural to be here.
        My sister graduated from Tech, so there was always a connection to it growing up, and now I get to
        build my own experience here. It has been challenging, exciting, and honestly a really rewarding place to grow.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# Row 2
col3, col4 = st.columns(2, gap="large")

with col3:
    music_img = single_image_html("images/music.jpg")
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">Music</div>
        {music_img}
        <div class="card-text">
        Since 8, I have played the piano and flute and been in group ensembles (orchestras, quintets, band)
        for a total of 10 years now! That creative side still shows up in a lot of what I do now and what I
        try to implement even with my technical work.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    baking_imgs = stacked_images_html(["images/bake8.jpg", "images/bake9.jpg"])
    st.markdown(f"""
    <div class="info-card">
        <div class="card-title">Baking and coffee</div>
        {baking_imgs}
        <div class="card-text">
        I’ve been baking since I was 9 years old, so at this point it feels less like a hobby and more like part of who I am.
        I also really enjoy coffee shop hunting, especially in a cultural powerhouse like Atlanta.
        Check my Beyond Engineering page for more.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Quick facts
st.markdown("""
<div class="quick-facts-card">
    <div class="card-title">Quick Facts</div>
    <span class="fun-pill">Raleigh roots</span>
    <span class="fun-pill">Georgia Tech EE</span>
    <span class="fun-pill">Signal Processing</span>
    <span class="fun-pill">Embedded Systems</span>
    <span class="fun-pill">Baking since age 9</span>
    <span class="fun-pill">Carolina Hurricanes fan</span>
    <span class="fun-pill">Coffee and latte lover</span>
    <span class="fun-pill">Music person</span>
</div>
""", unsafe_allow_html=True)
