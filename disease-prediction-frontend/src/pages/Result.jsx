import ResultChart from "./ResultChart";

export default function Result({ predictions, onRestart }) {
  const getRiskClass = (confidence) => {
    if (confidence > 0.7) return "high-risk";
    if (confidence > 0.4) return "medium-risk";
    return "low-risk";
  };

  return (
    <div className="result-container">
      <div className="result-content">
        <div className="result-header fade-in">
          <h1>Your Health Assessment Results</h1>
          <p className="result-subtitle">
            Based on your responses, here are the disease predictions with confidence levels
          </p>
        </div>

        <div className="chart-section fade-in">
          <h2>Prediction Overview</h2>
          <div className="chart-wrapper">
            <ResultChart predictions={predictions} />
          </div>
        </div>

        <div className="predictions-grid">
          {predictions.map((p, idx) => (
            <div key={idx} className={`prediction-card ${getRiskClass(p.confidence)} slide-in`}>
              <div className="prediction-header">
                <div>
                  <h3 className="disease-name">{p.disease}</h3>
                </div>
                <div className="confidence-badge">
                  {Math.round(p.confidence * 100)}%
                </div>
              </div>

              {p.reasons && p.reasons.length > 0 && (
                <div className="reasons-section">
                  <strong>Possible reasons:</strong>
                  <p>{p.reasons.join(", ")}</p>
                </div>
              )}
            </div>
          ))}
        </div>

        <div className="restart-section">
          <button className="restart-button" onClick={onRestart}>
            Start New Assessment
          </button>
        </div>

        <div className="result-disclaimer">
          ⚠️ This tool provides AI-based health insights and is not a substitute for professional medical advice. 
          Please consult a healthcare provider for proper diagnosis and treatment.
        </div>
      </div>
    </div>
  );
}
