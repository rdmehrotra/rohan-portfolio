import streamlit as st
import info
import pandas as pd

st.header("About Me")
st.write(info.about_me)

st.header("Education")
st.write(f"**{info.education_data['Institution']}**")
st.write(f"Degree: {info.education_data['Degree']}")
st.write(f"GPA: {info.education_data['GPA']}")

st.subheader("Coursework")
st.dataframe(pd.DataFrame(info.course_data))

st.header("Experience")
for job, (desc, _) in info.experience_data.items():
    with st.expander(job):
        for d in desc:
            st.write(d)

st.header("Projects")
for proj, desc in info.projects_data.items():
    with st.expander(proj):
        st.write(desc)

st.header("Skills")
for skill, val in info.programming_data.items():
    st.write(skill)
    st.progress(val)
