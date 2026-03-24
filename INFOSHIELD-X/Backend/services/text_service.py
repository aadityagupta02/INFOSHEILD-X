def analyze_text(text):
    features = {
        "urgency": {
            "keywords": ["urgent", "act now", "limited time"],
            "weight": 3
        },
        "guarantee": {
            "keywords": ["guaranteed", "100%", "no risk"],
            "weight": 3
        },
        "clickbait": {
            "keywords": ["click here", "shocking", "breaking"],
            "weight": 2
        },
        "greed": {
            "keywords": ["win money", "free", "prize"],
            "weight": 2
        }
    }

    score = 0
    reasons = []

    for feature, data in features.items():
        for word in data["keywords"]:
            if word in text:
                score += data["weight"]
                reasons.append(feature)
                break

    confidence = min(score * 10, 100)

    if score >= 7:
        result = "Highly Likely Fake"
    elif score >= 4:
        result = "Likely Fake"
    else:
        result = "Likely Real"

    return {
        "result": result,
        "confidence_percent": confidence,
        "reasons": reasons
    }
