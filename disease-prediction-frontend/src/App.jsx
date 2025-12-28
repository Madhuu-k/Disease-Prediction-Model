import Assessment  from "./pages/Assessment";
import { predictDisease } from "./services/api";

export default function App() {
  const handleAssessmentSubmit = async (answers) => {
    const result = await predictDisease(answers);
    return result;
  };

  return(
    <Assessment onSubmit={handleAssessmentSubmit} />
  );
}