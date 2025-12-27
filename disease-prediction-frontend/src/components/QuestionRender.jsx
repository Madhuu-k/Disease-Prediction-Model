export default function QuestionRender({ question, value, onChange }){
    const { id, label, type, options } = question;

    const handleChange =  (e) => {
        let newValue;

        if(type === "boolean") newValue = e.target.value === "true";
        else if(type === "number") newValue = e.target.value === "" ? "" : Number(e.target.value);
        else if(type === "select") newValue = e.target.value;

        onChange(id, newValue);
    };

    return(
        <div className="questions">
            <label>{label}</label>
            
            {type === "boolean" && (
                <select value={value ?? ""} onChange={handleChange}>
                    <option value="">select</option>
                    <option value="true">Yes</option>
                    <option value="false">No</option>
                </select>
            )}

            {type === "number" && (
                <input
                    type="number"
                    value={value ?? ""}
                    onChange={handleChange}
                />
            )}

            {type === "select" && (
                <select value={value ?? ""} onChange={handleChange}>
                    <option value="">Select</option>
                    {options.map((opt) => (
                        <option key={opt} value={opt}>
                            {opt}
                        </option>
                    ))}
                </select>
            )}
        </div>
    );
}