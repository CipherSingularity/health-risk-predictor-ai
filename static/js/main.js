document.getElementById('healthForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);

  const response = await fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  displayResults(result);
});

function displayResults({ risks, recommendations }) {
  const resultsDiv = document.getElementById('results');
  const risksDiv = document.getElementById('risks');
  const recsUl = document.getElementById('recs');

  risksDiv.innerHTML = `
    <div><strong>Diabetes Risk:</strong> <div class="risk-bar"><div class="risk-fill diabetes" style="width: ${risks.diabetes}%"></div></div> ${risks.diabetes}%</div>
    <div><strong>Heart Disease:</strong> <div class="risk-bar"><div class="risk-fill heart" style="width: ${risks.heart_disease}%"></div></div> ${risks.heart_disease}%</div>
    <div><strong>Stroke Risk:</strong> <div class="risk-bar"><div class="risk-fill stroke" style="width: ${risks.stroke}%"></div></div> ${risks.stroke}%</div>
  `;

  recsUl.innerHTML = recommendations.map(r => `<li>${r}</li>`).join('');
  resultsDiv.classList.remove('hidden');
}