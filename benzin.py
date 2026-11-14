import requests
from datetime import date

url = "https://europe-west6-tcs-digitalbackend.cloudfunctions.net/benzinGetStationById"
headers = {"Content-Type": "application/json", "Origin": "https://benzin.tcs.ch"}

stations = [
    ("COOP Arlesheim", "wVmt2ZXP7OsGmm3jDSl1"),
    ("AVIA Dornach", "WA8zY4mRudc4jOPZCHZR"),
    ("BP Dornach", "qduhc2wSnbHpbQ7jngis"),
    ("RuediRüssel Rheinach", "gcDZMaISP6nHAOtTL40v"),
    ("RuediRüssel Muttenz", "HFCfbbLXs2LFa9TPTJlT"),
    ("Scall Tankstelle Basel", "Ka6a3C2cR5VEohOc5xa5"),
]

today = date.today().strftime("%d.%m.%Y")
results = []

with requests.Session() as session:
    for name, station_id in stations:
        try:
            r = session.post(url, json={"id": station_id}, headers=headers, timeout=10)
            r.raise_for_status()
            price = float(r.json()["fuelCollection"]["SP95"]["displayPrice"])
            results.append((name, price))
        except (requests.RequestException, KeyError, TypeError, ValueError) as e:
            results.append((name, None))

results.sort(key=lambda x: x[1] if x[1] is not None else float("inf"))

print(f"{'Datum':<12}{'Ort':<24}{'Preis':<10}")
print("-" * 46)
for name, price in results:
    display = f"{price:.2f} Sfr" if price is not None else "n/a"
    print(f"{today:<12}{name:<24}{display}")
