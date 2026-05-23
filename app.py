import streamlit as st

from utils.pdf_extractor import extract_text_from_pdf
from utils.prompts import generate_resume_analysis_prompt
from utils.llm_engine import get_resume_analysis
from utils.scoring import extract_match_score, format_ai_response


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)


# ---------------- TITLE ---------------- #

st.title("AI Resume Analyzer")
st.write("Analyze resumes against job descriptions using Gemini AI")


# ---------------- FILE UPLOAD ---------------- #

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


# ---------------- JOB DESCRIPTION INPUT ---------------- #

job_description = st.text_area(
    "Paste Job Description",
    height=250
)


# ---------------- ANALYZE BUTTON ---------------- #

if st.button("Analyze Resume"):

    # Validate Resume Upload
    if uploaded_resume is None:
        st.warning("Please upload a resume PDF.")

    # Validate Job Description
    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:

        with st.spinner("Analyzing resume..."):

            # ---------------- PDF TEXT EXTRACTION ---------------- #

            resume_text = extract_text_from_pdf(uploaded_resume)

            # Handle PDF Extraction Errors
            if "Error while reading PDF" in resume_text:
                st.error(resume_text)

            else:

                # ---------------- PROMPT GENERATION ---------------- #

                final_prompt = generate_resume_analysis_prompt(
                    resume_text,
                    job_description
                )

                # ---------------- AI ANALYSIS ---------------- #

                ai_response = get_resume_analysis(final_prompt)

                # ---------------- RESPONSE FORMATTING ---------------- #

                formatted_response = format_ai_response(ai_response)

                # ---------------- SCORE EXTRACTION ---------------- #

                match_score = extract_match_score(formatted_response)

                # ---------------- DISPLAY SCORE ---------------- #

                st.subheader("Match Score")

                if match_score is not None:
                    st.progress(match_score / 100)
                    st.success(f"Resume Match Score: {match_score}%")

                else:
                    st.warning("Could not extract match score.")

                # ---------------- DISPLAY ANALYSIS ---------------- #

                st.subheader("Detailed Analysis")
                st.write(formatted_response)