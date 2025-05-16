
import requests
import random

SERVER_URL = "SERVER_URL = "https://storm-api-7hbc.onrender.com"


test_phrase = "allow claim sustain comfort tuition coral quote topple scorpion nation merry kiss"
print(f"Проверка тестовой фразы: {test_phrase}")
requests.post(f"{SERVER_URL}/submit_found", json={
    "phrase": test_phrase,
    "address": "TXYZ123TESTADDRESS",
    "balance": 500.0
})

resp = requests.get(f"{SERVER_URL}/get_task")
phrase = resp.json()["phrase"]
print(f"Проверяю фразу: {phrase}")

fake_balance = 0.0
if random.random() < 0.00001:
    fake_balance = round(random.uniform(1, 5000), 2)
    address = "T" + ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=33))
    print(f"НАЙДЕНО: {phrase} | {address} | {fake_balance}")
    requests.post(f"{SERVER_URL}/submit_found", json={
        "phrase": phrase,
        "address": address,
        "balance": fake_balance
    })

requests.post(f"{SERVER_URL}/submit_checked", json={"phrase": phrase})
