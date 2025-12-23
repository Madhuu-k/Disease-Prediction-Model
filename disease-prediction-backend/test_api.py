import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "fatigue": 1,
    "high_fever": 1,
    "headache": 1
}

res = requests.post(url, json=data)
print(res.json())