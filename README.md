# 🚀 TalentIQ — AI Recruitment Intelligence Platform

## 📌 Overview

TalentIQ is an AI-powered recruitment automation platform designed to streamline candidate screening and hiring workflows.

The system automatically parses resumes, evaluates candidate profiles against job descriptions, performs multi-dimensional scoring, ranks applicants, identifies skill gaps, and generates hiring recommendations through an interactive analytics dashboard.

This project demonstrates the application of Artificial Intelligence, Natural Language Processing (NLP), Resume Parsing, and Data Analytics in modern recruitment systems.

---

## 🎯 Key Objectives

* Automate resume screening
* Reduce manual recruiter effort
* Improve candidate shortlisting accuracy
* Identify skill gaps between job requirements and candidate profiles
* Generate data-driven hiring recommendations
* Visualize recruitment insights through dashboards

---

## ✨ Features

### 📄 Intelligent Resume Parsing

* Supports PDF and DOCX resumes
* Extracts candidate information and resume text automatically

### 🧠 AI-Driven Candidate Evaluation

* Compares resumes against job descriptions
* Performs skill-based matching

### 📊 Multi-Dimensional Candidate Scoring

Candidates are evaluated across multiple hiring dimensions:

| Dimension                  | Weight |
| -------------------------- | ------ |
| Skills Match               | 30%    |
| Experience Relevance       | 25%    |
| Education & Certifications | 15%    |
| Projects & Portfolio       | 20%    |
| Communication Quality      | 10%    |

### 🏆 Automated Candidate Ranking

* Sorts candidates by overall suitability score
* Enables recruiters to identify top applicants instantly

### 🔍 Skill Gap Detection

* Displays matched skills
* Highlights missing skills required for the role

### 📈 Recruitment Analytics Dashboard

Provides:

* Total Candidates
* Top Candidate Score
* Average Candidate Score
* Shortlisted Candidates
* Score Distribution Visualization

### 📌 Hiring Recommendations

Automatically classifies candidates as:

* Strong Match
* Shortlisted
* Rejected

---

## 🛠 Technology Stack

### Programming & Frameworks

* Python
* Streamlit

### Data Processing

* Pandas
* NumPy

### NLP & Text Processing

* Regular Expressions (Regex)
* Text Normalization

### Document Processing

* PyPDF
* Python-Docx

### Data Visualization

* Streamlit Analytics Dashboard

### Version Control

* Git
* GitHub

---

## 🏗 System Architecture

1. Recruiter uploads Job Description
2. Candidate resumes are uploaded
3. Resume Parser extracts text
4. Skill Extraction Engine identifies technical skills
5. Candidate Scoring Engine evaluates profiles
6. Ranking Module generates candidate rankings
7. Analytics Dashboard displays recruitment insights
8. Hiring Recommendation Engine suggests final actions

---

## 📂 Project Structure

```text
TalentIQ-AI-Recruitment-Intelligence-Platform/

├── app.py
├── requirements.txt
├── README.md
├── .gitignore

├── modules/
│   ├── resume_parser.py
│   ├── scorer.py
│   ├── report_generator.py
│   └── utils.py

├── data/
│   ├── resumes/
│   └── reports/

└── assets/
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd TalentIQ-AI-Recruitment-Intelligence-Platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📊 Sample Outputs

* Resume Match Percentage
* Skill Match Analysis
* Missing Skills Detection
* Candidate Ranking Table
* Recruitment Analytics Dashboard
* Hiring Recommendations

---

## 🎯 Future Enhancements

* Semantic Resume Matching using Sentence Transformers
* ATS Integration
* AI-Powered Interview Question Generation
* Resume Summarization using LLMs
* Advanced Candidate Recommendation Engine
* Real-Time Hiring Analytics
* Recruiter Feedback Learning System

---

## 👩‍💻 Developed By

**Oorjita Sharma**

B.Tech Computer Science Engineering (AI)

---

## ⭐ Project Title

**TalentIQ — AI Recruitment Intelligence Platform**
