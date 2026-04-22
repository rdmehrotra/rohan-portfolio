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
    padding: 1.5rem !important;
    box-shadow: 0 0 22px rgba(0,229,255,0.08);
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
    margin-bottom: 1.4rem;
}

.project-text {
    color: #dbe4ee;
    font-size: 1.05rem;
    line-height: 1.8;
    margin-bottom: 1.2rem;
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
    margin-top: 0.6rem;
}

.coming-soon-btn {
    display: inline-block;
    padding: 0.85rem 1.2rem;
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
    left, right = st.columns([1.1, 1.3], gap="large")  # 🔥 bigger image side

    with left:
        st.markdown('<div class="project-title">DIY Electronic Piano Using a 555 Timer</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="project-subtitle">Breadboard-based sound circuit inspired by a YouTube tutorial</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="project-text">

            <b>Project Idea:</b><br>
            For my ECE 1100 Discovery Project, I set out to build a DIY electronic piano using a 555 timer circuit on a breadboard, following a YouTube tutorial as a starting point.

            <br><br>

            <b>Project Progress:</b><br>
            I began by gathering components and recreating the circuit layout, then worked step-by-step through wiring the buttons, resistors, and speaker. I tested the system incrementally to understand how each part affected the output.

            <br><br>

            <b>Successes & Failures:</b><br>
            One of the biggest challenges was troubleshooting when the circuit wouldn’t produce sound, even when the wiring looked correct. Through trial and error, I realized how sensitive hardware systems are to small mistakes. Successfully getting the circuit to generate sound was a major turning point.

            <br><br>

            <b>ECE Skills Gained:</b><br>
            This project helped me build hands-on skills in breadboarding, circuit debugging, and understanding how components like resistors and timers interact to generate signals.

            <br><br>

            <b>Final Thoughts:</b><br>
            Overall, this project gave me a better appreciation for hardware design and strengthened my interest in hands-on electrical engineering work.

            </div>
            """,
            unsafe_allow_html=True
        )

        render_tags([
            "555 Timer",
            "Breadboarding",
            "Circuit Design",
            "Hardware Troubleshooting"
        ])

        st.markdown(" ")
        st.markdown(
            '<div class="coming-soon-btn">Tutorial-based build — no separate code repository</div>',
            unsafe_allow_html=True
        )

    with right:
        image_path = "images/discovery_project.jpg"

        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
            st.markdown(
                '<div class="image-note">Breadboard prototype of my 555 timer electronic piano project</div>',
                unsafe_allow_html=True
            )
        else:
            st.error("Image not found. Make sure discovery_project.jpg is inside the images folder.")
