import os
import streamlit as st

st.markdown("""
<style>
.block-container {
    max-width: none;
    padding: 2rem 2.75rem;
}

.projects-title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    color: #00E5FF;
    text-shadow: 0 0 22px rgba(0,229,255,0.45);
    margin-bottom: 0.2rem;
}

.projects-subtitle {
    text-align: center;
    font-size: 1.08rem;
    color: #cbd5e1;
    margin-bottom: 2rem;
}

.glow-line {
    width: 180px;
    height: 3px;
    margin: 0 auto 2rem auto;
    background: #00E5FF;
    box-shadow: 0 0 14px rgba(0,229,255,0.8);
    border-radius: 999px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18) !important;
    border-radius: 22px !important;
    padding: 1.5rem !important;
}

.project-title {
    font-size: 2.3rem;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 0.4rem;
}

.project-subtitle {
    font-size: 1.05rem;
    color: #94a3b8;
    margin-bottom: 1rem;
}

.project-text {
    color: #dbe4ee;
    font-size: 1.02rem;
    line-height: 1.65;
}

.tag {
    display: inline-block;
    padding: 0.42rem 0.82rem;
    margin-right: 0.45rem;
    margin-top: 0.6rem;
    border-radius: 999px;
    background: rgba(0,229,255,0.11);
    color: #a5f3fc;
    font-size: 0.9rem;
    border: 1px solid rgba(0,229,255,0.18);
}

.image-note {
    color: #94a3b8;
    font-size: 0.9rem;
    margin-top: 0.4rem;
    margin-bottom: 1rem;
}

.video-section {
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="projects-title">Discovery Project</div>', unsafe_allow_html=True)
st.markdown('<div class="projects-subtitle">A hands-on electronics build completed as part of ECE 1100.</div>', unsafe_allow_html=True)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

def render_tags(tags):
    st.markdown("".join([f'<span class="tag">{t}</span>' for t in tags]), unsafe_allow_html=True)

def find_img(paths):
    for p in paths:
        if os.path.exists(p):
            return p
    return None

with st.container(border=True):
    left, right = st.columns([1.05, 1.25], gap="large")

    with left:
        st.markdown('<div class="project-title">DIY Electronic Piano Using a 555 Timer</div>', unsafe_allow_html=True)
        st.markdown('<div class="project-subtitle">Breadboard-based sound circuit inspired by a YouTube tutorial</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="project-text">
        For my ECE 1100 Discovery Project, I built a DIY electronic piano using a 555 timer circuit on a breadboard.
        I followed a YouTube tutorial as a starting point, then worked through wiring, testing, and troubleshooting
        to actually get the circuit to produce sound.

        <br><br>

        Since I’m also taking ECE 2035 (programming for hardware/software systems) and ECE 2040 (circuit analysis),
        this project was a nice way to connect what I’m learning in class to something physical and hands-on.
        It helped reinforce how circuit components interact while also showing how small wiring mistakes can completely
        break a system.

        <br><br>

        Overall, this was a fun introduction to building real circuits and gave me a better appreciation for the
        hardware side of electrical engineering.
        </div>
        """, unsafe_allow_html=True)

        render_tags(["555 Timer","Breadboarding","Circuit Design","Hardware Troubleshooting"])

    with right:
        img1 = find_img(["images/discovery_project.jpg","discovery_project.jpg"])
        img2 = find_img(["images/discovery_project_2.jpg","discovery_project_2.jpg"])

        if img1:
            st.image(img1, use_container_width=True)
            st.markdown('<div class="image-note">Breadboard prototype of my build</div>', unsafe_allow_html=True)

        if img2:
            st.image(img2, use_container_width=True)
            st.markdown('<div class="image-note">Additional circuit photo</div>', unsafe_allow_html=True)

st.markdown('<div class="video-section"></div>', unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=6K89_3BDuSU&t=5s")
st.caption("Tutorial I used as a reference for building the circuit.")
