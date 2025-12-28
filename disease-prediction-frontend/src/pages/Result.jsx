export default function Result({ predictions }) {
  return (
    <div style={{ padding: "24px" }}>
      <h2>Prediction Result</h2>

      {predictions.map((p) => (
        <div key={p.disease} style={{ marginBottom: "20px" }}>
          <strong>{p.disease}</strong>

          <div
            style={{
              height: "12px",
              background: "#eee",
              borderRadius: "6px",
              overflow: "hidden",
              marginTop: "6px"
            }}
          >
            <div
              style={{
                width: `${p.confidence * 100}%`,
                height: "100%",
                background: "#4CAF50"
              }}
            />
          </div>

          <small>{Math.round(p.confidence * 100)}%</small>

          <p style={{ marginTop: "6px" }}>
            Possible reasons: {p.reasons.join(", ")}
          </p>
        </div>
      ))}
    </div>
  );
}
