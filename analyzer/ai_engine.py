from transformers import pipeline

import os
from transformers import pipeline

HF_TOKEN = os.getenv("HF_TOKEN")

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    token=HF_TOKEN
)

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

JOB_ROLES = [
    "Python Developer",
    "Django Developer",
    "Backend Developer",
    "Frontend Developer",
    "Data Scientist",
    "Machine Learning Engineer",
    "AI Engineer"
]


SKILL_MAP = {
    "Python Developer": ["Python", "Django", "REST API"],
    "Django Developer": ["Django", "ORM", "PostgreSQL"],
    "Backend Developer": ["APIs", "Databases", "Python"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript"],
    "Data Scientist": ["Pandas", "NumPy", "ML"],
    "Machine Learning Engineer": ["Scikit-learn", "TensorFlow"],
    "AI Engineer": ["Transformers", "NLP", "Deep Learning"]
}


# -------------------------
# JOB PREDICTION
# -------------------------
def predict_job(text):
    result = classifier(text, JOB_ROLES)

    return {
        "job": result["labels"][0],
        "confidence": round(result["scores"][0] * 100, 2)
    }


# -------------------------
# ATS SCORE ENGINE (NEW)
# -------------------------
def ats_score(text):
    score = 0

    keywords = [
        "python", "django", "api", "sql", "ml",
        "project", "experience", "education",
        "github", "development"
    ]

    for k in keywords:
        if k in text.lower():
            score += 10

    return min(score, 100)


# -------------------------
# AI IMPROVEMENT SUGGESTIONS (NEW)
# -------------------------
def improvement_suggestions(text):
    suggestions = []

    if "project" not in text.lower():
        suggestions.append("Add more real-world projects.")

    if "github" not in text.lower():
        suggestions.append("Include GitHub profile link.")

    if "api" not in text.lower():
        suggestions.append("Mention API development experience.")

    if len(text.split()) < 200:
        suggestions.append("Expand resume with more details.")

    if not suggestions:
        suggestions.append("Resume looks strong. Optimize keywords for ATS.")

    return suggestions


# -------------------------
# SKILL ASSESSMENT
# -------------------------
def assess_skills(text):
    assessment = {}

    for skill, keywords in SKILL_MAP.items():
        score = 0
        matched = []

        for k in keywords:
            if k.lower() in text.lower():
                score += 20
                matched.append(k)

        score = min(score, 100)

        if score >= 80:
            level = "Advanced"
        elif score >= 40:
            level = "Intermediate"
        else:
            level = "Beginner"

        assessment[skill] = {
            "score": score,
            "level": level,
            "matched": matched
        }

    return assessment