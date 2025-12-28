export default function QuestionRender({ question, value, onChange }){
    return(
        <div style={{ marginBottom: "16px" }}>
            <p>{question}</p>
            <select 
            value={value != undefined ? String(value) : ""}
            onChange={(e) => onChange(Number(e.target.value))}
            >
                <option value="">Select</option>
                <option value={1}>Yes</option>
                <option value={0}>No</option>
            </select>
        </div>
    );   
}