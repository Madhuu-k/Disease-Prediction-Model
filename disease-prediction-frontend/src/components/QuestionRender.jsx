import "./QuestionRender.css";

export default function QuestionRender({ question, value, onChange }) {
  return (
    <div className="question-card slide-in">
      <label className="question-text">{question}</label>

      <select 
        value={value != undefined ? String(value) : ""}
        onChange={(e) => onChange(Number(e.target.value))}>
            <option value="">Select</option>
            <option value={1}>Yes</option>
            <option value={0}>No</option>
        </select>
    </div>
  );
}

