# data/question_bank.py

"""
This file defines ONLY user-facing questions.
It does NOT contain ML feature names.
It does NOT know about the model.
"""

# -------------------------
# PHASE 1 — SCREENING QUESTIONS
# -------------------------
PHASE1_QUESTIONS = [
    {
        "id": "fever",
        "question": "Do you have fever?"
    },
    {
        "id": "fatigue",
        "question": "Do you feel unusually tired or weak?"
    },
    {
        "id": "headache",
        "question": "Do you have a headache?"
    },
    {
        "id": "cough",
        "question": "Do you have a cough?"
    },
    {
        "id": "loss_of_appetite",
        "question": "Have you noticed a loss of appetite?"
    },
    {
        "id": "nausea",
        "question": "Do you feel nauseous or feel like vomiting?"
    },
    {
        "id": "abdominal_pain",
        "question": "Do you have any stomach or abdominal discomfort?"
    },
    {
        "id": "skin_rash",
        "question": "Have you noticed any skin rashes or changes in skin color?"
    },
    {
        "id": "chills",
        "question": "Do you experience chills or shivering?"
    },
    {
        "id": "weight_loss",
        "question": "Have you experienced unexplained weight loss?"
    }
]

# -------------------------
# PHASE 2 — FOLLOW-UP QUESTIONS (BY GROUP)
# -------------------------
PHASE2_QUESTIONS = {
    "group_0": [
        {
            "id": "joint_pain",
            "question": "Do you experience joint pain?"
        },
        {
            "id": "muscle_pain",
            "question": "Do you have muscle pain or body aches?"
        }
    ],

    "group_1": [
        {
            "id": "skin_rash",
            "question": "Do you have skin rashes or itching?"
        },
        {
            "id": "yellowish_skin",
            "question": "Have you noticed yellowing of skin or eyes?"
        }
    ],

    "group_2": [
        {
            "id": "chest_pain",
            "question": "Do you feel any chest discomfort?"
        },
        {
            "id": "breathlessness",
            "question": "Do you feel shortness of breath?"
        }
    ],

    "group_3": [
        {
            "id": "vomiting",
            "question": "Have you been vomiting?"
        },
        {
            "id": "diarrhea",
            "question": "Do you have diarrhea?"
        }
    ],

    "group_4": [
        {
            "id": "blurred_vision",
            "question": "Do you have blurred vision or vision problems?"
        },
        {
            "id": "loss_of_balance",
            "question": "Do you experience loss of balance or dizziness?"
        }
    ]
}
