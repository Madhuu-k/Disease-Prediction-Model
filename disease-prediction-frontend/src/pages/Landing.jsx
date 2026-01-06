import "./Landing.css";

export default function Landing({ onStart }) {
  return (
    <div className="landing-wrapper">
      <div className="landing-content fade-in">
        <span className="badge">AI Health Intelligence</span>

        <h1 className="landing-title">
          AI-Powered Disease <span>Prediction</span>
        </h1>

        <p className="landing-subtitle">
          Answer a short health questionnaire and receive AI-driven
          disease risk insights based on clinical patterns.
        </p>

        <div className="landing-actions">
          <button className="primary-btn" onClick={onStart}>
            Start Assessment →
          </button>
        </div>

        <div className="landing-disclaimer">
            Educational purposes only. This tool does not provide medical advice, diagnosis, or treatment. Consult a qualified healthcare professional for medical decisions.
        </div>

      </div>
    </div>
  );
}
