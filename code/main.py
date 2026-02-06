from fastapi import FastAPI
from dataModels import StudentProfile
from profile_analyzer import analyze_profile
from knowledgeGapAnalyzer import detect_gaps
from learningPathGenerator import generate_learning_path

app = FastAPI(title="Learning Path Recommender")

REQUIRED_TOPICS = [
    "Basics", "Algebra", "Linear Equations",
    "Functions", "Problem Solving"
]

@app.post("/generate-path")
def generate_path(profile: StudentProfile):
    analysis = analyze_profile(profile)
    gaps = detect_gaps(REQUIRED_TOPICS, profile.completed_topics)
    path = generate_learning_path(gaps, analysis["time"])
    return {
        "student": profile.name,
        "learning_path": path
    }
