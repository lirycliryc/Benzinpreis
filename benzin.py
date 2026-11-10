import requests
from datetime import date

url = "https://europe-west6-tcs-digitalbackend.cloudfunctions.net/benzinGetStationById"
headers = {"Content-Type": "application/json", "Origin": "https://benzin.tcs.ch"}

stations = [
    ("COOP Arlesheim", "wVmt2ZXP7OsGmm3jDSl1"),
    ("AVIA Dornach", "WA8zY4mRudc4jOPZCHZR"),
    ("RuediRüssel Muttenz", "HFCfbbLXs2LFa9TPTJlT"),
    ("Scall Tankstelle Basel, "Ka6a3C2cR5VEohOc5xa5"),
]

today = date.today().strftime("%d.%m.%Y")

print(f"{'Datum':<12}{'Ort':<22}{'Preis':<22}")
print("-" * 56)

for name, station_id in stations:
    r = requests.post(url, json={"id": station_id}, headers=headers)
    price = r.json()["fuelCollection"]["SP95"]["displayPrice"]
    print(f"{today:<12}{name:<22}{price} Sfr")

