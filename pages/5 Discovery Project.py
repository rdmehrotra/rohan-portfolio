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

.projects-title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    color: #00E5FF;
    text-shadow: 0 0 22px rgba(0,229,255,0.45);
    margin-bottom: 0.25rem;
}

.projects-subtitle {
    text-align: center;
    font-size: 1.08rem;
    color: #cbd5e1;
    margin-bottom: 2.2rem;
}

.glow-line {
    width: 180px;
    height: 3px;
    margin: 0 auto 2.6rem auto;
    background: #00E5FF;
    box-shadow: 0 0 14px rgba(0,229,255,0.8);
    border-radius: 999px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18) !important;
    border-radius: 22px !important;
    padding: 1.15rem !important;
    box-shadow: 0 0 22px rgba(0,229,255,0.08);
}

.project-title {
    font-size: 2.15rem;
    font-weight: 750;
    color: #f8fafc;
    margin-bottom: 0.3rem;
}

.project-subtitle {
    font-size: 1rem;
    color: #94a3b8;
    margin-bottom: 1.05rem;
}

.project-text {
    color: #dbe4ee;
    font-size: 1.03rem;
    line-height: 1.75;
    margin-bottom: 1rem;
}

.tag {
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

.image-note {
    color: #94a3b8;
    font-size: 0.92rem;
    margin-top: 0.45rem;
}

.project-gap {
    height: 1.2rem;
}

.coming-soon-btn {
    display: inline-block;
    padding: 0.78rem 1.15rem;
    border-radius: 12px;
    border: 1px solid rgba(0,229,255,0.18);
    background: rgba(255,255,255,0.03);
    color: #cbd5e1;
    font-size: 1rem;
    font-weight: 600;
    box-shadow: 0 0 14px rgba(0,229,255,0.06);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="projects-title">Discovery Project</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="projects-subtitle">A hands-on electronics build completed as part of ECE 1100.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)


def render_tags(tags):
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
    st.markdown(tags_html, unsafe_allow_html=True)


with st.container(border=True):
    left, right = st.columns([1.45, 1], gap="large", vertical_alignment="center")

    with left:
        st.markdown('<div class="project-title">DIY Electronic Piano Using a 555 Timer</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="project-subtitle">Breadboard-based sound circuit inspired by a YouTube tutorial</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="project-text">
            For my ECE 1100 Discovery Project, I built a DIY electronic piano using a 555 timer circuit on a breadboard.
            I followed a YouTube tutorial as a starting point, then worked through wiring, testing, and troubleshooting
            to get the circuit to produce sound.
            <br><br>
            This project gave me hands-on experience with basic electronics like resistors, pushbuttons, and speakers,
            while also helping me understand how simple circuits can generate different tones. It also showed me how
            important debugging is in hardware, since small mistakes had a big impact on performance.
            <br><br>
            Overall, it was a solid introduction to circuit building and strengthened my interest in hands-on electrical engineering work.
            </div>
            """,
            unsafe_allow_html=True
        )

        render_tags([
            "555 Timer",
            "Breadboarding",
            "Circuit Design",
            "Hardware Troubleshooting",
            "ECE 1100 Discovery Project"
        ])

        st.markdown(" ")
        st.markdown(
            '<div class="coming-soon-btn">Tutorial-based build — no separate code repository</div>',
            unsafe_allow_html=True
        )

    with right:
        image_path = "discovery_project.jpg"  # ✅ FIXED PATH

        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
            st.markdown(
                '<div class="image-note">Breadboard prototype of my 555 timer electronic piano project</div>',
                unsafe_allow_html=True
            )
        else:
            st.error("Image not found — make sure discovery_project.jpg is in the repo root")
