from profile_analyzer import analyze_profile
from courseCompressionEngine import compress_courses
from diagnosticTestEngine import evaluate_test
from knowledgeGapAnalyzer import detect_gaps
from learningPathGenerator import generate_learning_path
from adaptiveFeedbackEngine import adapt_path

class LearningPathAgent:
    def __init__(self):
        pass

    def assess(self, profile, course, answers):
        # 1. Analyze profile
        profile_info = analyze_profile(profile)

        # 2. Compress course descriptions (optional clustering)
        try:
            compressed = compress_courses([course.get("description", "")])
        except Exception:
            compressed = {0: [course.get("description", "")]}

        # 3. Build a simple diagnostic test key from topics
        correct_answers = {}
        for i, topic in enumerate(course.get("topics", []), start=1):
            q = f"q{i}"
            correct_answers[q] = {"topic": topic, "answer": "yes"}

        # If caller provided answers, evaluate them; otherwise simulate
        if not answers:
            # Simulate: assume learner answers 'yes' for known skills
            answers = {}
            known = profile_info.get("skills", set())
            for k, v in correct_answers.items():
                answers[k] = "yes" if v["topic"] in known else "no"

        test_results = evaluate_test(answers, correct_answers)

        # 4. Detect knowledge gaps (combine weak topics and missing skills)
        known_topics = set(profile_info.get("skills", set()))
        weak_topics = set(test_results.get("weak_topics", []))
        required_topics = course.get("topics", [])
        gaps = detect_gaps(required_topics, list(known_topics | weak_topics))

        # 5. Generate initial learning path
        path = generate_learning_path(gaps, profile_info.get("time", 30))

        # 6. Build a simple performance map (used by adaptive engine)
        performance = {}
        for t in required_topics:
            performance[t] = 90 if t in known_topics and t not in weak_topics else 50 if t in weak_topics else 30

        # 7. Adapt path based on performance
        adapted = adapt_path(performance, path)

        # 8. Add short explanation for each step
        for step in adapted:
            step["why"] = self._explain(step["topic"], profile_info, test_results)

        return {
            "profile": profile_info,
            "compressed": compressed,
            "test": test_results,
            "initial_path": path,
            "final_path": adapted,
        }

    def _explain(self, topic, profile_info, test_results):
        if topic in test_results.get("weak_topics", []):
            return f"Topic '{topic}' was flagged weak by the diagnostic test; recommended revision."
        if topic in profile_info.get("skills", set()):
            return f"Topic '{topic}' is partially known — practice and project recommended."
        return f"Topic '{topic}' is new; learn fundamentals then practice."


if __name__ == "__main__":
    # Simple demo runner
    class Profile:
        def __init__(self, goal, available_time_per_day, known_skills):
            self.goal = goal
            self.available_time_per_day = available_time_per_day
            self.known_skills = known_skills

    # Example course
    course = {
        "title": "Intro to Python",
        "description": "Learn basics: variables, loops, functions, lists, OOP",
        "topics": ["variables", "loops", "functions", "lists", "OOP"]
    }

    # Example student
    profile = Profile(goal="job", available_time_per_day=45, known_skills=["variables", "lists"])

    agent = LearningPathAgent()
    result = agent.assess(profile, course, answers={"Variables": "yes", "loops": "yes", "functions": "no"})

    print("=== Assessment Summary ===")
    print("Profile:", result["profile"]) 
    print("Test:", result["test"]) 
    print("Final learning path:")
    for step in result["final_path"]:
        print(f" - {step['topic']}: {step['duration_days']} days — {step['action']} — {step['why']}")
