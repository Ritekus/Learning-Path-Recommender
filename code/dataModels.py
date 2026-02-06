from pydantic import BaseModel
from typing import List, Dict

class StudentProfile(BaseModel):
    name: str
    goal: str
    available_time_per_day: int
    known_skills: List[str]
    completed_topics: List[str]

class TestResult(BaseModel):
    score: float
    weak_topics: List[str]

class LearningStep(BaseModel):
    topic: str
    duration_days: int
    action: str

class LearningPath(BaseModel):
    steps: List[LearningStep]
