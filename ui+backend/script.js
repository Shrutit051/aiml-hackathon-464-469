document.getElementById('check-btn').addEventListener('click', async () => {
  const newsText = document.getElementById('news-input').value.trim();
  const resultBox = document.getElementById('result');

  if (!newsText) {
    resultBox.textContent = "⚠️ Please enter some text before checking.";
    resultBox.className = "result-box error";
    resultBox.classList.remove("hidden");
    return;
  }

  // Call Flask backend
  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: newsText })
    });

    const data = await response.json();

    if (data.error) {
      resultBox.textContent = "⚠️ " + data.error;
      resultBox.className = "result-box error";
    } else {
      const isFake = data.prediction.includes('Fake');
      resultBox.className = isFake ? "result-box error" : "result-box success";
      resultBox.innerHTML = `
        <strong>${data.prediction}</strong><br>
        Confidence: ${data.confidence}<br>
        <small>Model used: ${data.model_used}</small>
       `;

    }

    resultBox.classList.remove("hidden");
  } catch (error) {
    resultBox.textContent = "⚠️ Server error. Please try again.";
    resultBox.className = "result-box error";
    resultBox.classList.remove("hidden");
  }
});
