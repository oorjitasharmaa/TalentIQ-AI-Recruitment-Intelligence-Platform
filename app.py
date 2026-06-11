import streamlit as st
import os
import pandas as pd
from modules.scorer import score_resume, extract_skills
from modules.resume_parser import parse_resume
from modules.scorer import score_resume

# PAGE CONFIG
st.set_page_config(
    page_title= "TalentIQ — AI Recruitment Intelligence Platform",
    page_icon= "🤖",
    layout= "wide"
)

# CUSTOM CSS
st.markdown(
    """
    <style>

    .main {
        background-color: #0e1117;
    }

    .stButton button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# SIDEBAR
with st.sidebar:

    st.title("AI HR Resuming Shortlisting Agent")

    st.markdown("---")
    
    st.subheader("🚀 Platform Capabilities")

    st.write("*AI-Powered Resume Analysis*")
    st.write("*Intelligent Resume Parsing*")
    st.write("*Multi-Dimensional Candidate Scoring*")
    st.write("*Automated Candidate Ranking*")
    st.write("*Recruitment Analytics Dashboard*")
    st.write("*Real-Time Hiring Insights*")
    st.write("*Skill Gap Detection*")


    st.markdown("---")

    st.success("Upload job descriptions and resumes to get started!")

# MAIN TITLE
st.title("🤖 TalentIQ — AI Recruitment Intelligence Platform")

st.markdown(
    "AI-powered recruitment system for intelligent resume analysis and candidate shortlisting."
)

# TABS
upload_tab, ranking_tab, analytics_tab = st.tabs([
    "📂 Upload",
    "🏆 Rankings",
    "📊 Analytics"
])

# CANDIDATE STORAGE
candidate_data = []

# UPLOAD TAB
with upload_tab:

    st.header("📄 Job Description")

    job_description = st.text_area(
        "Paste Job Description Here",
        height=220
    )

    st.header("📂 Upload Candidate Resumes")

    uploaded_files = st.file_uploader(
        "Upload PDF or DOCX resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files and job_description:

        os.makedirs("data/resumes", exist_ok=True)

        st.header("🧠 Candidate Analysis")

        for file in uploaded_files:

            file_path = os.path.join("data/resumes", file.name)

            with open(file_path, "wb") as f:
                f.write(file.getbuffer())

            # PARSE RESUME

            extracted_text = parse_resume(file_path)
         
            # SCORE RESUME

            result = score_resume(
                job_description,
                extracted_text
            )

            score = result["score"]

            # RECOMMENDATION
        
            if score >= 75:
                recommendation = "✅ Strong Match"

            elif score >= 60:
                recommendation = "⚠ Shortlisted"

            else:
                recommendation = "❌ Rejected"

            # SAVE DATA

            candidate_data.append({
                "Candidate": file.name,
                "Score": score,
                "Recommendation": recommendation
            })

            
            # UI CARD 

            st.markdown("---")

            st.subheader(f"👤 {file.name}")

            st.metric(
                "Match Score",
                f"{score}%"
            )

            st.progress(score / 100)

           
            # MATCHED SKILLS

            st.write("### ✅ Matched Skills")

            for skill in result["matched_skills"]:
                st.success(skill)

            # MISSING SKILLS

            st.write("### ❌ Missing Skills")

            for skill in result["missing_skills"]:
                st.error(skill)

            # RECOMMENDATION

            st.write("### 📌 Hiring Recommendation")

            st.success(recommendation)

            # DIMENSION SCORES

            st.write("### 📊 Dimension Scores")

            st.json(
                result["dimension_scores"]
            )

            # EXTRACTED TEXT

            with st.expander(
                "📄 View Extracted Resume Text"
            ):

                st.text(extracted_text)

# RANKING TAB

with ranking_tab:

    st.header("🏆 Candidate Rankings")

    if len(candidate_data) > 0:

        df = pd.DataFrame(candidate_data)

        df = df.sort_values(
            by="Score",
            ascending=False
        )

        df.index = range(
            1,
            len(df) + 1
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "Upload resumes to see rankings."
        )

# ANALYTICS TAB 

with analytics_tab:

    st.header("📊 Recruitment Analytics")

    if len(candidate_data) > 0:

        df = pd.DataFrame(candidate_data)

        total_candidates = len(df)

        top_score = df["Score"].max()

        average_score = round(
            df["Score"].mean(),
            2
        )

        shortlisted = len(
            df[df["Score"] >= 70]
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Candidates",
            total_candidates
        )

        col2.metric(
            "Top Score",
            f"{top_score}%"
        )

        col3.metric(
            "Average Score",
            f"{average_score}%"
        )

        col4.metric(
            "Shortlisted",
            shortlisted
        )

        st.markdown("---")

        st.subheader("📈 Score Distribution")

        st.bar_chart(
            df.set_index("Candidate")["Score"]
        )

    else:

        st.info(
            "Analytics will appear after resume processing."
        )