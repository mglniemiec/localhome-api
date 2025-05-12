from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Load real estate site data from the JSON file
with open("sites_data.json", "r") as f:
    data = {k.lower(): v for k, v in json.load(f).items()}

@app.get("/real-estate-sites/{country}")
def get_site(country):
    country = country.lower()
    if country in data:
        return {"country": country, "site": data[country]}
    else:
        raise HTTPException(status_code=404, detail="Country not found")

