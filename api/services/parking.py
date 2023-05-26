import requests
import csv
import json
from functools import lru_cache
from loguru import logger

from api.core.config import LATEST_CSV

def csv_to_json(content: str):
    json_content = []
    reader = csv.DictReader(content.splitlines())
    for row in reader:
        json_content.append(row)
    return json.loads(json.dumps(json_content))

@lru_cache()
def fetch_latest() -> str:
    logger.info("Fetching latest data")
    r = requests.get(LATEST_CSV)
    r.raise_for_status()
    content = r.text
    return csv_to_json(content)
