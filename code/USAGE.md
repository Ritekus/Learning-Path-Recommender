# Learning Path Agent — Usage

Quick demo (from repository root):

```bash
python3 code/learning_path_agent.py
```

Programmatic example:

```python
from code.learning_path_agent import LearningPathAgent

class Profile:
    def __init__(self, goal, available_time_per_day, known_skills):
        self.goal = goal
        self.available_time_per_day = available_time_per_day
        self.known_skills = known_skills

agent = LearningPathAgent()
profile = Profile(goal="job", available_time_per_day=45, known_skills=["variables", "lists"])
course = {"title": "Intro to Python", "description": "...", "topics": ["variables","loops","functions","lists","OOP"]}
result = agent.assess(profile, course, answers=None)
print(result["final_path"]) 
```

Notes:
- The demo uses simple heuristics and the modules in the `code/` folder.
- Optional NLP clustering requires extra packages (see `requirements.txt`); the demo will still run without them.
