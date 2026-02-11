import json
import os
from datetime import datetime

FEEDBACK_FILE = "memory/feedback.json"


def save_feedback(query, answer, score, feedback):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "query": query,
        "answer": answer,
        "score": score,
        "feedback": feedback
    }

    # create file if not exists
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w") as f:
            json.dump([], f)

    # append entry
    with open(FEEDBACK_FILE, "r") as f:
        data = json.load(f)

    data.append(entry)

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=2)
