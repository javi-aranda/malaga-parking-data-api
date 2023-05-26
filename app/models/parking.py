from typing import Optional
from pydantic import BaseModel, Field


class ParkingDataResponse(BaseModel):
    parking_id: int = Field(..., alias="poiID")
    name: str = Field(..., alias="nombre")
    address: Optional[str] = Field(..., alias="direccion")
    contact_number: Optional[str] = Field(..., alias="telefono")
    email_address: Optional[str] = Field(..., alias="correoelectronico")
    latitude: float = Field(..., alias="latitude")
    longitude: float = Field(..., alias="longitude")
    altitude: float = Field(..., alias="altitud")
    total_spots: Optional[str] = Field(..., alias="capacidad")
    disabled_spots: Optional[str] = Field(..., alias="capacidad_discapacitados")
    latest_updated: Optional[str] = Field(..., alias="fechahora_ultima_actualizacion")
    available_spots: int = Field(..., alias="libres")
    available_disability_spots: Optional[str] = Field(..., alias="libres_discapacitados")
    orange_occupation_level: Optional[str] = Field(..., alias="nivelocupacion_naranja")
    red_occupation_level: Optional[str] = Field(..., alias="nivelocupacion_rojo")
    smassa_sector_sare: Optional[str] = Field(..., alias="smassa_sector_sare")
