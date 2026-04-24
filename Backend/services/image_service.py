import os

def analyze_image(file_path):
    try:
        # Get file size in KB
        file_size_kb = os.path.getsize(file_path) / 1024

        # Demo logic (replace later with real ML)
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

    except FileNotFoundError:
        return {
            "error": "File not found"
        }


# Main program
if __name__ == "__main__":
    file_path = input("Enter image file path: ")

    output = analyze_image(file_path)

    if "error" in output:
        print("Error:", output["error"])
    else:
        print("Analysis Result:")
        print("Result:", output["result"])
        print("Confidence:", output["confidence_percent"], "%")
