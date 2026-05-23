# AI Resume Analyzer

AI-powered Resume Analyzer built using Python and Streamlit to evaluate resumes against job descriptions.

## Features

- Upload resume in PDF format
- Analyze resumes against job descriptions
- Generate match score
- Identify strengths and missing skills
- Provide improvement suggestions
- Interactive Streamlit UI

## Tech Stack

- Python
- Streamlit
- PyPDF2
- Prompt Engineering
- LLM Workflow Integration

## Folder Structure

```bash
AI_RESUME_ANALYZER/
│
├── utils/
│   ├── llm_engine.py
│   ├── pdf_extractor.py
│   ├── prompts.py
│   └── scoring.py
│
├── app.py
├── requirements.txt
├── README.md
```

## Installation

### Clone Repository

```bash
git clone <https://github.com/Ashutosh-K0/ai-resume-analyzer>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

## Future Improvements

- Real-time LLM API integration
- Advanced ATS scoring
- Skill keyword extraction
- Resume recommendations
- Multi-role resume analysis

## Author

Ashutosh Kumar