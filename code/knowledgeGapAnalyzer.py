def detect_gaps(required_topics, known_topics):
    required = set(required_topics)
    known = set(known_topics)

    gaps = required - known
    return list(gaps)
