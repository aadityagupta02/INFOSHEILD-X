import os

def analyze_image(file_path):
    # Demo logic (replace later with real ML)
    file_size_kb = os.path.getsize(file_path) / 1024

    if file_size_kb > 100:
        result = "Likely FAKE"
        confidence = 75
    else:
        result = "Likely REAL"
        confidence = 60

    return {
        "result": result,
        "confidence_percent": confidence
    }