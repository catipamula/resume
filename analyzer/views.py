from django.shortcuts import render
from .ai_engine import assess_skills, ats_score, improvement_suggestions
from .utils import extract_pdf_text, scrape_jobs


def home(request):
    return render(request, "analyzer/index.html")


def detect_domain(text):
    text = text.lower()

    if any(k in text for k in ["django", "flask", "api", "backend", "python"]):
        return "Backend Developer"

    if any(k in text for k in ["html", "css", "javascript", "react", "frontend"]):
        return "Frontend Developer"

    if any(k in text for k in ["machine learning", "ai", "deep learning", "nlp", "tensorflow"]):
        return "Machine Learning Engineer"

    if any(k in text for k in ["cybersecurity", "network", "hacking", "security"]):
        return "Cybersecurity Engineer"

    if any(k in text for k in ["cloud", "aws", "azure", "devops", "docker", "kubernetes"]):
        return "Cloud/DevOps Engineer"

    if any(k in text for k in ["data", "pandas", "numpy", "sql", "analysis"]):
        return "Data Scientist"

    return "Software Engineer"


def analyze(request):
    text = ""

    if request.FILES.get("resume_pdf"):
        pdf_file = request.FILES["resume_pdf"]
        text = extract_pdf_text(pdf_file)

    elif request.POST.get("resume_text"):
        text = request.POST.get("resume_text")

    if not text:
        return render(request, "analyzer/index.html")

    job = detect_domain(text)

    skill_gap = assess_skills(text)
    ats = ats_score(text)
    suggestions = improvement_suggestions(text)

    jobs = scrape_jobs(job)

    missing = []

    domain_skills = {
        "Backend Developer": ["Python", "Django", "REST API", "Databases"],
        "Frontend Developer": ["HTML", "CSS", "JavaScript", "React"],
        "Machine Learning Engineer": ["Python", "TensorFlow", "Scikit-learn", "NLP"],
        "Cybersecurity Engineer": ["Networking", "Linux", "Security Tools", "Ethical Hacking"],
        "Cloud/DevOps Engineer": ["AWS", "Docker", "Kubernetes", "CI/CD"],
        "Data Scientist": ["Python", "Pandas", "NumPy", "SQL"],
        "Software Engineer": ["DSA", "OOP", "Problem Solving"]
    }

    required = domain_skills.get(job, [])

    for skill in required:
        if skill.lower() not in text.lower():
            missing.append(skill)

    return render(request, "analyzer/result.html", {
        "job": job,
        "confidence": 92,
        "assessment": skill_gap,
        "ats": ats,
        "suggestions": suggestions,
        "jobs": jobs,
        "missing": missing
    })