import Assessment  from "./pages/Assessment";
import { predictDisease } from "./services/api";

export default function App() {
  const handleAssessmentSubmit = async (answers) => {
    try{
      console.log("Sending Answers to backend: ", answers);
      const result = await predictDisease(answers);
      console.log("Prediction result: ", result);
    } catch(err) {
      console.log(err);
    }
  };

  return(
    <Assessment onSubmit={handleAssessmentSubmit} />
  );
}