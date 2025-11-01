document.getElementById('healthForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);

  // show a loading state
  const resultsDiv = document.getElementById('results');
  resultsDiv.classList.remove('hidden');
  document.getElementById('risks').innerHTML = '<p>Loading predictions...</p>';

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (!response.ok) throw new Error('Prediction request failed');
    const result = await response.json();
    displayResults(result);
  } catch (err) {
    document.getElementById('risks').innerHTML = `<p style="color:crimson">Error: ${err.message}</p>`;
    document.getElementById('recs').innerHTML = '';
  }
});

function displayResults(payload) {
  // payload expected: { risks: {diabetes, heart_disease, stroke}, recommendations: [...] }
  const { risks, recommendations } = payload;

  const resultsDiv = document.getElementById('results');
  const risksDiv = document.getElementById('risks');
  const recsUl = document.getElementById('recs');

  // timestamp
  const ts = new Date().toLocaleString();
  const tsEl = document.getElementById('result-timestamp');
  if (tsEl) tsEl.textContent = ts;

  // Build risk rows
  const makeRow = (label, value, cls) => `
    <div class="risk-row">
      <div class="risk-label">${label}</div>
      <div style="flex:1">
        <div class="risk-bar"><div class="risk-fill ${cls}" style="width:${value}%"></div></div>
      </div>
      <div class="risk-value">${value}%</div>
    </div>`;

  risksDiv.innerHTML = '';
  if (risks) {
    risksDiv.innerHTML += makeRow('Diabetes', Number(risks.diabetes || risks.Diabetes_Risk || 0).toFixed(1), 'diabetes');
    risksDiv.innerHTML += makeRow('Heart Disease', Number(risks.heart_disease || risks.Heart_Disease || 0).toFixed(1), 'heart');
    risksDiv.innerHTML += makeRow('Stroke', Number(risks.stroke || risks.Stroke || 0).toFixed(1), 'stroke');
  } else {
    risksDiv.innerHTML = '<p>No risk data returned.</p>';
  }

  // Recommendations
  if (recommendations && recommendations.length) {
    recsUl.innerHTML = recommendations.map(r => `<li>${r}</li>`).join('');
  } else {
    recsUl.innerHTML = '<li>No recommendations available.</li>';
  }

  resultsDiv.classList.remove('hidden');
}