from pdfminer.high_level import extract_text
import tempfile


def extract_pdf_text(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        for chunk in uploaded_file.chunks():
            tmp.write(chunk)
        tmp_path = tmp.name

    text = extract_text(tmp_path)
    return text


def scrape_jobs(query="python developer"):
    return [
        {
            "title": "Python Developer",
            "company": "TCS",
            "location": "Remote",
            "link": "https://www.naukri.com/python-jobs"
        },
        {
            "title": "Django Developer",
            "company": "Infosys",
            "location": "Bangalore",
            "link": "https://www.naukri.com/django-jobs"
        },
        {
            "title": "Backend Engineer",
            "company": "Wipro",
            "location": "Hyderabad",
            "link": "https://www.linkedin.com/jobs"
        }
    ]