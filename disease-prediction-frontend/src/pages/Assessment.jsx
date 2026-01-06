import { useState } from "react";
import QUESTIONS from "../config/questions";
import QuestionRender from "../components/QuestionRender";
import Result from "./Result";
import "./Assessment.css";

export default function Assessment({ onSubmit }) {
  const [phase, setPhase] = useState(1);
  const [answers, setAnswers] = useState({});
  const [phase2Questions, setPhase2Questions] = useState([]);
  const [finalResult, setFinalResult] = useState(null)
  const [currentPage, setCurrentPage] = useState(0);

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
    setCurrentPage(0);
    setPhase(2);
  };

  const handlePhase2Submit = async () => {
    const result = await onSubmit(answers);
    setFinalResult(result.disease_predictions)
    setPhase(3);
    console.log("Final Answers:", answers);
  };

  const RestartAssessment = () => {
    setAnswers({});
    setPhase2Questions([]);
    setFinalResult(null);
    setPhase(1);
  };

  if (phase === 3) {
    return(
        <div className="assessment-container">
            <Result predictions={finalResult}/>
        </div>
    );
  }

  const QUESTIONS_PER_PAGE = 3;
  const questionsToRender = phase === 1 ? QUESTIONS : phase2Questions;

  const startIndex = QUESTIONS_PER_PAGE * currentPage;
  const endIndex = startIndex + QUESTIONS_PER_PAGE;
  
  const currentQuestions = questionsToRender.slice(startIndex, endIndex);
  const isLast = endIndex >= questionsToRender.length;


  return (
    <div className="assessment-container">
      <div className="assessment-wrapper">
        <div className="assessment-content">
      <h2>{phase === 1 ? "Health Assessment" : "Follow-up Questions"}</h2>

      {currentQuestions.map((q) => (
        <QuestionRender
          key={q.id}
          question={q.question}
          value={answers[q.id]}
          onChange={(val) => handleChange(q.id, val)}
        />
      ))}

      {!isLast && 
      <div className="button-group">
        <button
          disabled={currentPage===0}
          onClick={() => setCurrentPage((p) => p - 1)}
        >Previous</button>

        <button
          disabled={currentQuestions.some(
            (q) => answers[q.id] === undefined
          )}
          onClick={() => setCurrentPage((p) => p + 1)}
        >Next</button>  
      </div>
      }

      {isLast && phase === 1 && (
        <button onClick={handlePhase1Submit}>
          Continue
        </button>
      )}

      {isLast && phase === 2 && (
        <button onClick={handlePhase2Submit}>
          Submit
        </button>
      )}

      <div className="assessment-disclaimer">
        This assessment provides AI-based insights and does not replace professional medical consultation.
      </div>
      </div>
      </div>
    </div>
  );
}
