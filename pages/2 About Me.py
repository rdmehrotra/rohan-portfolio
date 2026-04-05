import os
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

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18) !important;
    border-radius: 22px !important;
    padding: 1rem !important;
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
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

.card-title {
    font-size: 1.45rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.55rem;
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
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="about-title">💫 About Me</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="about-subtitle">A little more about who I am outside of just classes, code, and projects.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)


def show_if_exists(path):
    if os.path.exists(path):
        st.image(path, use_container_width=True)


# Hero section
with st.container(border=True):
    left, right = st.columns([1, 1.45], gap="large", vertical_alignment="center")

    with left:
        show_if_exists("images/profile.jpeg")

    with right:
        st.markdown('<div class="name">Hi, I’m Rohan 👋</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="body-text">
            I’m an Electrical Engineering student at Georgia Tech who’s especially interested in signal processing,
            embedded systems, and building things that feel interactive and alive. Outside of engineering, I’m also
            really into baking, coffee, music, and anything that makes life feel a little more fun and a little less
            robotic.
            <br><br>
            I wanted this page to feel a little more personal, because I’m definitely not just coursework and labs.
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("")

# Cute interest cards
col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.markdown('<div class="card-title">🏒 Go Canes!</div>', unsafe_allow_html=True)
        show_if_exists("images/canes.jpg")
        st.markdown(
            """
            <div class="card-text">
            I’m a huge Carolina Hurricanes fan, and yes, moving away from North Carolina definitely meant leaving one
            of my favorite things behind. Hockey is one of those things that always feels exciting to me, and being a
            Canes fan is honestly part of my personality at this point.
            </div>
            """,
            unsafe_allow_html=True
        )

with col2:
    with st.container(border=True):
        st.markdown('<div class="card-title">🐝 GT pride, unfortunately</div>', unsafe_allow_html=True)
        show_if_exists("images/gtcap.jpg")
        st.markdown(
            """
            <div class="card-text">
            I’m very much locked into the Georgia Tech world now. My sister graduated from GT, so lowkey I was kind of
            destined to end up here. At this point, being a Yellow Jacket feels less like a choice and more like a
            family requirement.
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("")

col3, col4 = st.columns(2, gap="large")

with col3:
    with st.container(border=True):
        st.markdown('<div class="card-title">🎷 Music & creativity</div>', unsafe_allow_html=True)
        show_if_exists("images/music.jpg")
        st.markdown(
            """
            <div class="card-text">
            Music has always been a big part of my life. I played saxophone for years, and I think that creative side
            of me still shows up in a lot of what I build now. Even when I’m working on technical stuff, I still care
            a lot about presentation, feel, and making things look polished.
            </div>
            """,
            unsafe_allow_html=True
        )

with col4:
    with st.container(border=True):
        st.markdown('<div class="card-title">🧁 Baking, coffee, and all that</div>', unsafe_allow_html=True)
        if os.path.exists("images/bake8.jpg"):
            st.image("images/bake8.jpg", use_container_width=True)
        elif os.path.exists("images/baby_me.jpeg"):
            st.image("images/baby_me.jpeg", use_container_width=True)
        st.markdown(
            """
            <div class="card-text">
            I’ve been baking since I was 9 years old, so at this point it’s kind of built into who I am. I also love
            coffee and lattes, which honestly makes sense because both baking and coffee feel a little bit like small
            daily rituals to me.
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("")

with st.container(border=True):
    st.markdown('<div class="card-title">Quick facts</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <span class="fun-pill">Chapel Hill roots</span>
        <span class="fun-pill">Georgia Tech EE</span>
        <span class="fun-pill">Signal Processing</span>
        <span class="fun-pill">Embedded Systems</span>
        <span class="fun-pill">Baking since age 9</span>
        <span class="fun-pill">Carolina Hurricanes fan</span>
        <span class="fun-pill">Coffee / latte lover</span>
        <span class="fun-pill">Music person</span>
        """,
        unsafe_allow_html=True
    )
