import os
import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

st.markdown("""
<style>
.block-container {
    max-width: none;
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
}

.page-title {
    text-align: center;
    font-size: 3.3rem;
    font-weight: 700;
    color: #00E5FF;
    text-shadow: 0 0 20px rgba(0,229,255,0.45);
    margin-bottom: 0.35rem;
}

.page-subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: #cbd5e1;
    margin-bottom: 2.2rem;
}

.project-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(0,229,255,0.18);
    border-radius: 18px;
    padding: 1.4rem;
    box-shadow: 0 0 18px rgba(0,229,255,0.08);
    margin-bottom: 1.5rem;
}

.project-title {
    font-size: 2rem;
    font-weight: 700;
    color: #e5e7eb;
    margin-bottom: 0.35rem;
}

.project-subtitle {
    font-size: 1rem;
    color: #94a3b8;
    margin-bottom: 1rem;
}

.project-text {
    color: #dbe4ee;
    font-size: 1.02rem;
    line-height: 1.7;
    margin-bottom: 1rem;
}

.tag {
    display: inline-block;
    padding: 0.4rem 0.8rem;
    margin-right: 0.45rem;
    margin-bottom: 0.55rem;
    border-radius: 999px;
    background: rgba(0,229,255,0.12);
    color: #9be7ff;
    font-size: 0.9rem;
    border: 1px solid rgba(0,229,255,0.18);
}

.image-placeholder {
    height: 270px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 1rem;
    color: #94a3b8;
    background: rgba(255,255,255,0.04);
    border: 1px dashed rgba(0,229,255,0.25);
}

.section-spacer {
    height: 0.4rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">🚀 Projects</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="page-subtitle">A few things I’ve built across algorithms, engineering, and interactive web development.</div>',
    unsafe_allow_html=True
)


def render_tags(tags):
    tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
    st.markdown(tags_html, unsafe_allow_html=True)


def render_project(title, subtitle, description, tags, github_url, image_path, image_note):
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    left, right = st.columns([1.55, 1], vertical_alignment="center")

    with left:
        st.markdown(f'<div class="project-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-subtitle">{subtitle}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-text">{description}</div>', unsafe_allow_html=True)
        render_tags(tags)
        st.link_button("View Code →", github_url)

    with right:
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
            if image_note:
                st.caption(image_note)
        else:
            st.markdown(
                f'<div class="image-placeholder">Add an image here later:<br><strong>{image_path}</strong></div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)


render_project(
    title="Path Optimization Algorithm",
    subtitle="Weighted-grid pathfinding and minimum-cost route selection",
    description="""
    This project focused on building an algorithm to find an efficient path through a weighted grid while minimizing total cost.
    I worked through the logic of dynamic programming, path updates, and state tracking to compute the best route instead of
    brute-forcing every possibility. It pushed me to think carefully about efficiency, debugging, and how to translate an
    algorithmic idea into working code.
    """,
    tags=["C", "Algorithms", "Dynamic Programming", "Optimization"],
    github_url="https://github.com/rdmehrotra/path-optimization-algorithm",
    image_path="images/project1.jpg",
    image_note="Path optimization / shortest-path style project"
)

render_project(
    title="Interactive Portfolio Website",
    subtitle="A custom Streamlit site for projects, resume, and personal dashboards",
    description="""
    I designed and deployed this portfolio website in Streamlit to create a more interactive alternative to a static personal site.
    The app includes custom styling, a live resume page, downloadable assets, project showcases, and personal data dashboards.
    I also worked through deployment issues, theming, layout design, and UI polish to make the final result feel much more like
    a real product than a classroom assignment.
    """,
    tags=["Python", "Streamlit", "UI Design", "Deployment", "Data Visualization"],
    github_url="https://github.com/rdmehrotra/rohan-portfolio",
    image_path="images/project2.jpg",
    image_note="This portfolio site"
)
