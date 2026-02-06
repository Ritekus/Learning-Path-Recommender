def evaluate_test(answers: dict, correct_answers: dict):
    score = 0
    weak_topics = []

    for q, ans in answers.items():
        if ans == correct_answers[q]["answer"]:
            score += 1
        else:
            weak_topics.append(correct_answers[q]["topic"])

    percentage = (score / len(correct_answers)) * 100

    return {
        "score": percentage,
        "weak_topics": list(set(weak_topics))
    }
