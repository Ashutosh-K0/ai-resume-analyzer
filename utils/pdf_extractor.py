from PyPDF2 import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.

    Parameters:
        uploaded_file: Streamlit uploaded PDF file object

    Returns:
        str: Extracted text from the PDF
    """

    try:
        pdf_reader = PdfReader(uploaded_file)

        extracted_text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                extracted_text += page_text + "\n"

        cleaned_text = extracted_text.strip()

        if not cleaned_text:
            return "No readable text found in the PDF."

        return cleaned_text

    except Exception as error:
        return f"Error while reading PDF: {str(error)}"