import re


def extract_match_score(response_text):
    """
    Extracts match score from AI response.

    Parameters:
        response_text (str): Complete AI response

    Returns:
        int or None: Extracted score
    """

    try:
        score_pattern = r"Match Score:\s*(\d+)"

        match = re.search(score_pattern, response_text)

        if match:
            return int(match.group(1))

        return None

    except Exception:
        return None


def format_ai_response(response_text):
    """
    Cleans and formats AI response.

    Parameters:
        response_text (str): Raw AI output

    Returns:
        str: Clean formatted response
    """

    try:
        cleaned_response = response_text.strip()

        return cleaned_response

    except Exception:
        return response_text