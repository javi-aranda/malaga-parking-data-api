from typing import List
from app.services.parking import fetch_latest
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger
from app.models.parking import ParkingDataResponse

router = APIRouter()

@router.get(
    "/latest",
    response_model=List[ParkingDataResponse],
    name="latest:get-data",
)
async def latest():
    logger.info("Getting latest data")
    try:
        latest_data = fetch_latest()
        return JSONResponse(content=[ParkingDataResponse(**item).dict() for item in latest_data])
    except Exception as error:
        raise HTTPException(status_code=500, detail=error)
