def get_health_tips(disease):
    TIPS = {

        "Heart Disease": [
            "Reduce salt and oily food intake",
            "Engage in light cardiovascular exercise",
            "Avoid smoking and alcohol",
            "Monitor blood pressure regularly",
            "Manage stress effectively"
        ],

        "Neurological Disorder": [
            "Ensure adequate sleep",
            "Avoid alcohol and stimulants",
            "Reduce screen time",
            "Practice stress-relief techniques",
            "Consult a neurologist promptly"
        ],

        "Infection": [
            "Stay hydrated",
            "Take adequate rest",
            "Monitor body temperature",
            "Maintain hygiene",
            "Seek medical care if symptoms persist"
        ],

        "Respiratory Disease": [
            "Avoid exposure to dust and smoke",
            "Use steam inhalation if advised",
            "Stay hydrated",
            "Avoid cold air exposure",
            "Consult a pulmonologist if breathing worsens"
        ]
    }

    return TIPS.get(disease, [
        "Consult a qualified medical professional",
        "Maintain a healthy lifestyle",
        "Do not self-medicate"
    ])
