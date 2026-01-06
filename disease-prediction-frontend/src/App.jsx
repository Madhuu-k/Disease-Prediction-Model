import { useState } from "react";
import Assessment from "./pages/Assessment";
import Landing from "./pages/Landing";
import "./App.css";
import { predictDisease } from "./services/api";

export default function App() {
  const [started, setStarted] = useState(false);

  const handleAssessmentSubmit = async (answers) => {
    const result = await predictDisease(answers);
    return result;
  };

  return (
    <>
      {!started ? (
        <Landing onStart={() => setStarted(true)} />
      ) : (
        <Assessment onSubmit={handleAssessmentSubmit} />
      )}
    </>
  );
}
