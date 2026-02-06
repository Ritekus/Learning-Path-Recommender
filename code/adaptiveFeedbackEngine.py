def adapt_path(performance, learning_path):
    for step in learning_path:
        if performance.get(step["topic"], 0) < 60:
            step["action"] = "Revise & Re-test"
            step["duration_days"] += 1
        elif performance.get(step["topic"], 0) > 85:
            step["duration_days"] = max(1, step["duration_days"] - 1)
    return learning_path
