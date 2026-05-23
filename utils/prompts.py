def generate_resume_analysis_prompt(resume_text, job_description):
    """
    Creates a structured prompt for resume evaluation.

    Parameters:
        resume_text (str): Extracted resume content
        job_description (str): User-provided job description

    Returns:
        str: Final formatted prompt
    """

    prompt = f"""
You are an expert ATS (Applicant Tracking System) and technical recruiter.

Your task is to analyze the given resume against the provided job description.

Evaluate the candidate based on:
1. Technical Skills Match
2. Relevant Experience
3. Project Relevance
4. Education & Certifications
5. Overall Job Fit

Resume:
{resume_text}

Job Description:
{job_description}

Provide the response STRICTLY in the following format:

Match Score: <score out of 100>

Strengths:
- Point 1
- Point 2
- Point 3

Missing Skills:
- Skill 1
- Skill 2
- Skill 3

Suggestions for Improvement:
- Suggestion 1
- Suggestion 2
- Suggestion 3

Final Verdict:
<Short evaluation summary>
"""

    return prompt