import os
import streamlit as st

st.markdown("""
<style>
.block-container {
    max-width: none;
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
}

.projects-title {
    text-align: center;
    font-size: 3.2rem;
    font-weight: 800;
    color: #00E5FF;
    text-shadow: 0 0 22px rgba(0,229,255,0.45);
    margin-bottom: 0.2rem;
}

.projects-subtitle {
    text-align: center;
    font-size: 1rem;
    color: #cbd5e1;
    margin-bottom: 1.6rem;
}

.glow-line {
    width: 160px;
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
    padding: 1rem !important;
    box-shadow: 0 0 22px rgba(0,229,255,0.08);
}

.project-title {
    font-size: 2rem;
    font-weight: 750;
    color: #f8fafc;
    margin-bottom: 0.25rem;
}

.project-subtitle {
    font-size: 0.95rem;
    color: #94a3b8;
    margin-bottom: 0.8rem;
}

.project-text {
    color: #dbe4ee;
    font-size: 1rem;
    line-height: 1.5;
    margin-bottom: 0.6rem;
}

.tag {
    display: inline-block;
    padding: 0.35rem 0.75rem;
    margin-right: 0.35rem;
    margin-bottom: 0.45rem;
    border-radius: 999px;
    background: rgba(0,229,255,0.11);
    color: #a5f3fc;
    font-size: 0.85rem;
    border: 1px solid rgba(0,229,255,0.18);
}

.image-note {
    color: #94a3b8;
    font-size: 0.85rem;
    margin-top: 0.35rem;
}

.coming-soon-btn {
    display: inline-block;
    padding: 0.7rem 1rem;
    border-radius: 10px;
    border: 1px solid rgba(0,229,255,0.18);
    background: rgba(255,255,255,0.03);
    color: #cbd5e1;
    font-size: 0.95rem;
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
            <b>Project Idea:</b><br>
            Build a DIY electronic piano using a 555 timer circuit on a breadboard, starting from a YouTube tutorial.
            
            <br>
            <b>Project Progress:</b><br>
            Wired components step-by-step, testing along the way to understand how each part affected the output.
            
            <br>
            <b>Successes & Failures:</b><br>
            Debugging was the hardest part — small wiring mistakes completely broke the circuit, but getting sound working was a big success.
            
            <br>
            <b>ECE Skills Gained:</b><br>
            Learned breadboarding, circuit debugging, and how resistors + timers interact to generate signals.
            
            <br>
            <b>Final Thoughts:</b><br>
            Strengthened my interest in hands-on electrical engineering and showed how much patience hardware work requires.
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
            st.error("Image not found. Put discovery_project.jpg inside the images folder.")
