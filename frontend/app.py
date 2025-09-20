import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

import streamlit as st
from scoring import final_score

st.title("GenAI Resume Relevance Checker")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=['pdf', 'docx'])
jd_file = st.file_uploader("Upload Job Description (PDF/DOCX)", type=['pdf', 'docx'])

if st.button("Evaluate") and resume_file and jd_file:
    resume_path = os.path.join("temp_resume.pdf" if resume_file.type=="application/pdf" else "temp_resume.docx")
    jd_path = os.path.join("temp_jd.pdf" if jd_file.type=="application/pdf" else "temp_jd.docx")

    with open(resume_path, "wb") as f:
        f.write(resume_file.getbuffer())
    with open(jd_path, "wb") as f:
        f.write(jd_file.getbuffer())

    score, verdict = final_score(resume_path, jd_path)

    st.success(f"Relevance Score: {score}/100")
    st.info(f"Verdict: {verdict}")
