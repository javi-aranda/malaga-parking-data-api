import requests
import csv
import json
from functools import lru_cache
from requests.exceptions import RequestException
from fastapi import FastAPI, HTTPException

app = FastAPI()

BASE_URL = 'https://raw.githubusercontent.com/javisenberg/malaga-parking-data/master'
LATEST_CSV = f'{BASE_URL}/latest.csv'


@lru_cache()
def fetch_latest() -> str:
    r = requests.get(LATEST_CSV)
    r.raise_for_status()
    content = r.text
    return content


def csv_to_json(content: str):
    json_content = []
    reader = csv.DictReader(content.splitlines())
    for row in reader:
        json_content.append(row)
    return json.loads(json.dumps(json_content))


@app.get("/")
async def root():
    try:
        data = fetch_latest()
        data = csv_to_json(data)
        return data
    except RequestException as e:
        raise HTTPException(status_code=500, detail=e)
