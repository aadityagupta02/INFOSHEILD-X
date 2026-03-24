from ai_models.model import predict_text


def analyze_text(text):
    ml_result = predict_text(text)

    explanation = []
    text_lower = text.lower()

    ai_score = 0  # 🔥 rule score

    # 🔥 RULE 1 — AI phrases
    if "in conclusion" in text_lower:
        explanation.append("Contains AI-style phrase: 'in conclusion'")
        ai_score += 2

    if "furthermore" in text_lower:
        explanation.append("Contains AI-style phrase: 'furthermore'")
        ai_score += 2

    # 🔥 RULE 2 — sentence length
    word_count = len(text.split())

    if word_count >= 12:
        explanation.append("Long structured sentence")
        ai_score += 2
    elif word_count >= 8:
        explanation.append("Moderately long structured sentence")
        ai_score += 1

    # 🔥 RULE 3 — punctuation
    if "," in text:
        explanation.append("Uses comma (structured writing style)")
        ai_score += 1

    if not explanation:
        explanation.append("No strong AI patterns detected")

    # 🔥 ML confidence
    ml_conf = ml_result["confidence_percent"]

    # 🔥 HYBRID SCORE
    final_score = (ml_conf * 0.7) + (ai_score * 10)

    # 🔥 FINAL DECISION
    if final_score >= 60:
        final_result = "FAKE (AI Generated)"
    else:
        final_result = "REAL (Human Written)"

    final_confidence = min(int(final_score), 100)

    # 🔥 CONFIDENCE REASON
    if final_confidence >= 80:
        confidence_reason = "High confidence due to strong AI patterns"
    elif final_confidence >= 60:
        confidence_reason = "Moderate confidence based on text structure"
    else:
        confidence_reason = "Low confidence, limited indicators"

    return {
        "result": final_result,
        "confidence_percent": final_confidence,
        "confidence_reason": confidence_reason,
        "explanation": explanation
    }