import streamlit as st

from utils.pdf_extractor import extract_text_from_pdf
from utils.prompts import generate_resume_analysis_prompt
from utils.llm_engine import get_resume_analysis
from utils.scoring import extract_match_score, format_ai_response


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton>button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.stTextArea textarea {
    border-radius: 10px;
}

.stFileUploader {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ---------------- #

st.title("📄 AI Resume Analyzer")
st.caption("Analyze resumes against job descriptions using AI-powered evaluation")


# ---------------- LAYOUT ---------------- #

left_column, right_column = st.columns([1, 1])


# ---------------- LEFT COLUMN ---------------- #

with left_column:

    st.subheader("Upload Resume")

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    st.subheader("Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=300
    )


# ---------------- RIGHT COLUMN ---------------- #

with right_column:

    st.subheader("Analysis Results")

    if st.button("Analyze Resume"):

        # Validation
        if uploaded_resume is None:
            st.warning("Please upload a resume PDF.")

        elif not job_description.strip():
            st.warning("Please enter a job description.")

        else:

            with st.spinner("Analyzing resume..."):

                # Extract Resume Text
                resume_text = extract_text_from_pdf(uploaded_resume)

                # Handle Extraction Errors
                if "Error while reading PDF" in resume_text:
                    st.error(resume_text)

                else:

                    # Generate Prompt
                    final_prompt = generate_resume_analysis_prompt(
                        resume_text,
                        job_description
                    )

                    # AI Response
                    ai_response = get_resume_analysis(final_prompt)

                    # Format Response
                    formatted_response = format_ai_response(ai_response)

                    # Extract Score
                    match_score = extract_match_score(formatted_response)

                    # ---------------- SCORE DISPLAY ---------------- #

                    if match_score is not None:

                        st.metric(
                            label="Resume Match Score",
                            value=f"{match_score}%"
                        )

                        st.progress(match_score / 100)

                    else:
                        st.warning("Could not extract match score.")

                    # ---------------- ANALYSIS OUTPUT ---------------- #

                    st.markdown("---")

                    st.subheader("Detailed Analysis")

                    st.write(formatted_response)