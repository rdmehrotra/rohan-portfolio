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
    margin-bottom: 2.5rem;
}

.glow-line {
    width: 180px;
    height: 3px;
    margin: 0 auto 2.5rem auto;
    background: #00E5FF;
    box-shadow: 0 0 14px rgba(0,229,255,0.8);
    border-radius: 999px;
}

.project-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.04));
    border: 1px solid rgba(0,229,255,0.18);
    border-radius: 22px;
    padding: 1.6rem;
    box-shadow: 0 0 24px rgba(0,229,255,0.08);
    margin-bottom: 1.7rem;
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

.image-shell {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(0,229,255,0.16);
    border-radius: 18px;
    padding: 0.7rem;
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
}

.image-placeholder {
    height: 300px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 1rem;
    color: #94a3b8;
    background: rgba(255,255,255,0.04);
    border: 1px dashed rgba(0,229,255,0.25);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="projects-title">🚀 Projects</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="projects-subtitle">A closer look at some of the engineering and technical work I’ve built.</div>',
    unsafe_allow_html=True
)
st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)


def render_tags(tags):
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
    st.markdown(tags_html, unsafe_allow_html=True)


def render_project(title, subtitle, description, tags, github_url, image_path, image_caption):
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    left, right = st.columns([1.45, 1], vertical_alignment="center")

    with left:
        st.markdown(f'<div class="project-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-subtitle">{subtitle}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-text">{description}</div>', unsafe_allow_html=True)
        render_tags(tags)
        st.link_button("View Code →", github_url)

    with right:
        st.markdown('<div class="image-shell">', unsafe_allow_html=True)
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
            if image_caption:
                st.caption(image_caption)
        else:
            st.markdown(
                f'<div class="image-placeholder">Drop your image here later:<br><strong>{image_path}</strong></div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


render_project(
    title="Path Optimization Algorithm",
    subtitle="Minimum-cost route selection through a weighted grid",
    description="""
    This project focused on building an algorithm to determine the most efficient path through a weighted environment while minimizing total cost.
    I implemented the logic needed to compare candidate routes, update path values efficiently, and arrive at the optimal solution without brute-forcing every possibility.
    It strengthened my understanding of algorithm design, dynamic programming style thinking, and how to turn a mathematical idea into code that actually works under constraints.
    """,
    tags=["C", "Algorithms", "Dynamic Programming", "Optimization"],
    github_url="https://github.com/rdmehrotra/path-optimization-algorithm",
    image_path="images/project1.jpg",
    image_caption="Path optimization project"
)

render_project(
    title="Embedded Systems Interface",
    subtitle="Interactive ESP32-based system with display, buttons, and real-time behavior",
    description="""
    In this project, I worked with an ESP32-C6 microcontroller to build an interactive embedded system using hardware inputs and outputs in real time.
    The system involved integrating push or navigation switch input, LCD display behavior, timers, GPIO logic, and speaker functionality while debugging both code and physical wiring.
    Beyond just getting the system to run, this project taught me how closely software and hardware depend on each other, especially when timing, peripherals, and user interaction all need to work together smoothly.
    """,
    tags=["Embedded C", "ESP32", "Microcontrollers", "GPIO", "Real-Time Systems"],
    github_url="https://github.com/rdmehrotra/embedded-systems-interface",
    image_path="images/project2.jpg",
    image_caption="Hardware prototype, update coming soon"
)
