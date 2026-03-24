console.log("JS Loaded");

// make function GLOBAL
window.detectText = async function () {
  console.log("Button clicked");

  const text = document.getElementById("textInput").value;
  const resultDiv = document.getElementById("result");

  if (!text || text.trim() === "") {
    alert("Please enter text first");
    return;
  }

  resultDiv.style.display = "block";
  resultDiv.innerText = "Analyzing...";

  try {
    const response = await fetch("http://127.0.0.1:5000/detect-text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: text })
    });

    console.log("Response received");

    const data = await response.json();
    console.log(data); 

    const explanationBox = document.getElementById("explanation");

// clear previous explanation
explanationBox.innerText = "";

// check if explanation exists
if (data.explanation) {
  explanationBox.innerText = data.explanation.join("\n");
}

    resultDiv.innerText =
      data.result + " (" + data.confidence_percent + "%)";

  } catch (error) {
    console.log("ERROR:", error);
    resultDiv.innerText = "❌ Backend not working";
  }
};
window.openModal = function () {
  document.getElementById("detectModal").classList.add("show");
};

window.closeModal = function () {
  document.getElementById("detectModal").classList.remove("show");
};