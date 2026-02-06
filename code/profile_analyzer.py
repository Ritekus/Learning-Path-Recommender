def analyze_profile(profile):
    return {
        "goal": profile.goal,
        "time": profile.available_time_per_day,
        "skills": set(profile.known_skills),
    }
