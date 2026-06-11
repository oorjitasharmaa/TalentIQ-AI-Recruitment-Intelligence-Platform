import re

# =========================
# SKILL DATABASE
# =========================

skills_database = [
    "python",
    "java",
    "c++",
    "sql",
    "react",
    "fastapi",
    "docker",
    "git",
    "aws",
    "machine learning",
    "streamlit",
    "javascript",
    "html",
    "css",
    "power bi",
    "excel",
    "pandas",
    "numpy",
    "nlp",
    "tableau"
]


# =========================
# EXTRACT SKILLS
# =========================

def extract_skills(text):

    text = str(text).lower()

    # Handle PDFs where letters are separated:
    # P y t h o n -> python
    normalized_text = text.replace(" ", "")

    found_skills = []

    for skill in skills_database:

        skill_normalized = skill.lower().replace(" ", "")

        if skill_normalized in normalized_text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


# =========================
# EXPERIENCE SCORE
# =========================

def experience_score(resume_text, jd_text):

    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    score = 0

    if "intern" in resume_text:
        score += 5

    if "experience" in resume_text:
        score += 5

    if "developer" in resume_text and "developer" in jd_text:
        score += 10

    if "machine learning" in resume_text and "machine learning" in jd_text:
        score += 5

    return min(score, 25)


# =========================
# EDUCATION SCORE
# =========================

def education_score(resume_text):

    resume_text = resume_text.lower()

    score = 0

    if "b.tech" in resume_text or "btech" in resume_text:
        score += 8

    if (
        "computer science" in resume_text
        or "cse" in resume_text
        or "artificial intelligence" in resume_text
        or "(ai)" in resume_text
    ):
        score += 4

    if (
        "certification" in resume_text
        or "certifications" in resume_text
        or "coursera" in resume_text
        or "forage" in resume_text
    ):
        score += 3

    return min(score, 15)


# =========================
# PROJECT SCORE
# =========================

def project_score(resume_text):

    resume_text = resume_text.lower()

    score = 0

    if "project" in resume_text or "projects" in resume_text:
        score += 10

    if "analysis" in resume_text:
        score += 5

    if "dashboard" in resume_text:
        score += 5

    if "github" in resume_text:
        score += 5

    return min(score, 20)


# =========================
# COMMUNICATION SCORE
# =========================

def communication_score(resume_text):

    words = len(resume_text.split())

    if words > 350:
        return 10

    elif words > 200:
        return 7

    else:
        return 4


# =========================
# MAIN SCORING FUNCTION
# =========================

def score_resume(job_description, resume_text):

    jd_skills = extract_skills(job_description)

    resume_skills = extract_skills(resume_text)

    matched_skills = sorted(
        list(set(jd_skills) & set(resume_skills))
    )

    missing_skills = sorted(
        list(set(jd_skills) - set(resume_skills))
    )

    # Skills Score (30)

    if len(jd_skills) == 0:
        skills_score = 0
    else:
        skills_score = int(
            (len(matched_skills) / len(jd_skills)) * 30
        )

    # Other Scores

    exp_score = experience_score(
        resume_text,
        job_description
    )

    edu_score = education_score(
        resume_text
    )

    proj_score = project_score(
        resume_text
    )

    comm_score = communication_score(
        resume_text
    )

    total_score = (
        skills_score
        + exp_score
        + edu_score
        + proj_score
        + comm_score
    )

    total_score = min(total_score, 100)

    return {

        "score": total_score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "dimension_scores": {

            "Skills Match": skills_score,

            "Experience Relevance": exp_score,

            "Education & Certifications": edu_score,

            "Projects / Portfolio": proj_score,

            "Communication Quality": comm_score
        }
    }