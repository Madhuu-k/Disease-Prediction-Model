import { useState } from "react";
import { QUESTIONS } from "../config/questions";
import QuestionRender from "../components/QuestionRender";

export default function Assessment({ onSubmit }) {
    const [step, setStep] = useState(0);
    const [answers, setAnswers] = useState([]);

    // Filter questions for current step
    const currentQuestions = QUESTIONS.filter(
        (q) => q.step === step
    );

    // Handle change in Input
    const handleChange = (id, value) => {
        setAnswers((prev) => ({
            ...prev,
            [id]:value,
        }));
    };

    // Navigation (Back and Next)
    const handleNext = () => {
        setStep((prev) => prev + 1);
    };

    const handleBack = () => {
        setStep((prev) => prev - 1);
    };

    const handleSubmit = () => {
        onSubmit(answers);
    };

    return(
        <div className="assessment-container">
            <h2>Health Assessment</h2>
            <p>Step {step} of 5</p>

            {QuestionRender.map((question) => (
                <QuestionRender 
                    key={question.id}
                    question={question}
                    value={answers[question.id]}
                    onChange={handleChange}
                />
            ))}

            <div className="navigation-buttons">
                {step > 1 && ( 
                    <button onClick={handleBack}>
                        Back
                    </button>
                )}

                {step < 5 && (
                    <button onClick={handleNext}>
                        Next
                    </button>
                )}
                
                {step === 5 && (
                    <button onClick={handleSubmit}>
                        Submit
                    </button>
                )}
                
            </div>
        </div>
    )
}
