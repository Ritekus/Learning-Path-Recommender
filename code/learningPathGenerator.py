import networkx as nx

def generate_learning_path(gaps, time_per_day):
    G = nx.DiGraph()

    for topic in gaps:
        G.add_node(topic)

    steps = []
    for topic in nx.topological_sort(G):
        days = 1 if time_per_day >= 60 else 2
        steps.append({
            "topic": topic,
            "duration_days": days,
            "action": "Learn & Practice"
        })

    return steps
