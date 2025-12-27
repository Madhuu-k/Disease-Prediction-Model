import { useState, useEffect } from "react";
import { QUESTIONS } from "../config/questions";
import QuestionRender from "../components/QuestionRender";

export default function Assessment({ onSubmit }) {
    const [step, setStep] = useState(1);
    const [answers, setAnswers] = useState({});
    const [route, setRoute] = useState("general");

    useEffect(() => {
        if (step < 3) return;
        if (answers.chest_pain || answers.shortness_of_breath) {
            setRoute("heart");
        } else if (answers.headache && answers.fever) {
            setRoute("neuro");
        }
    }, [answers, step]);

    // Filter questions for current step
    const currentQuestions = QUESTIONS.filter((q) => {
        if(q.step !== step) return false;
        if(q.route && q.route !== route) return false;
        return true;}
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

            {currentQuestions.map((question) => (
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
