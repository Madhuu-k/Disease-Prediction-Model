export async function predictDisease(payload) {
    const res = await fetch("http://127.0.0.1:5000/predict",{
        method: "POST",
        headers: {
            "Contten-Type" : "application/json"
        },
        body: JSON.stringify(payload)
    });

    if(!res.ok) throw new Error("Prediction Failed");
    return res.json();

}