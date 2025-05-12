# Real Estate Sites API

A simple FastAPI project that returns the most popular real estate listing site for a given country.

---

## Table of Contents

- [Purpose](#purpose)
- [Example Usage](#example-usage)
- [Run the API](#run-the-api)
- [Data Source](#data-source)

---

## Purpose

When searching for real estate in another country using English, people often land on overpriced, expat-targeted platforms.  
This API helps by returning the most popular **local** site per country — so you can go directly to the source.

---

## Example Usage

GET `/real-estate-sites/france`

Response:
{
  "country": "france",
  "site": "https://www.seloger.com"
}


## Run the API
1. Make sure you have FastAPI and Uvicorn installed and start API server:
uvicorn main:app --reload

This will start the server locally on http://127.0.0.1:8000.

2. Access the Swagger UI:
After the server is running, you can open a web browser and go to http://127.0.0.1:8000/docs.
This will open the interactive Swagger UI, where you can see and interact with the available API endpoints.

3. Test the API:
You can now test the API by sending a GET request to the endpoint:
GET /real-estate-sites/{country}


## Data Source
The site data is stored in a local JSON file: sites_data.json.


More countries and features to come... :)
