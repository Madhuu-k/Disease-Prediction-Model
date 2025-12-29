import { useState } from "react";
import QUESTIONS from "../config/questions";
import QuestionRender from "../components/QuestionRender";
import Result from "./Result";

export default function Assessment({ onSubmit }) {
  const [phase, setPhase] = useState(1);
  const [answers, setAnswers] = useState({});
  const [phase2Questions, setPhase2Questions] = useState([]);
  const [finalResult, setFinalResult] = useState(null)

  const handleChange = (id, value) => {
    setAnswers((prev) => ({
      ...prev,
      [id]: value
    }));
  };

  const handlePhase1Submit = async () => {
    const result = await onSubmit(answers);

    const questions = Object.values(result.phase2_questions || {}).flat();

    setPhase2Questions(questions);
    setPhase(2);
  };

  const handlePhase2Submit = async () => {
    const result = await onSubmit(answers);
    setFinalResult(result.disease_predictions)
    setPhase(3);
    console.log("Final Answers:", answers);
    alert("Phase-2 answers captured. (Next: disease prediction)");
  };

  const RestartAssessment = () => {
    setAnswers({});
    setPhase2Questions([]);
    setFinalResult(null);
    setPhase(1);
  };

  if (phase === 3) {
    return(
        <div>
            <Result predictions={finalResult}/>

            <p style={{ marginTop: "20px", color: "#777", fontSize: "14px" }}>
                ⚠️ This tool provides AI-based health insights and is not a substitute for professional medical advice.
            </p>
            
            <button onClick={RestartAssessment} style={{ marginTop: "20px" }}>
                Restart Assessment
            </button>
        </div>
    );
  }

  const questionsToRender = phase === 1 ? QUESTIONS : phase2Questions;

  return (
    <div style={{ padding: "24px" }}>
      <h2>{phase === 1 ? "Health Assessment" : "Follow-up Questions"}</h2>

      {questionsToRender.map((q) => (
        <QuestionRender
          key={q.id}
          question={q.question}
          value={answers[q.id]}
          onChange={(val) => handleChange(q.id, val)}
        />
      ))}

      {phase === 1 && (
        <button onClick={handlePhase1Submit}>
          Continue
        </button>
      )}

      {phase === 2 && (
        <button onClick={handlePhase2Submit}>
          Submit
        </button>
      )}
    </div>
  );
}
