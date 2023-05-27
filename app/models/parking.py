from typing import Optional

from pydantic import BaseModel, Field, validator


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
    latest_updated: Optional[str] = Field(
        ..., alias="fechahora_ultima_actualizacion"
    )  # noqa: E501
    available_spots: int = Field(..., alias="libres")
    available_disability_spots: Optional[str] = Field(
        ..., alias="libres_discapacitados"
    )
    orange_occupation_level: Optional[str] = Field(..., alias="nivelocupacion_naranja")
    red_occupation_level: Optional[str] = Field(..., alias="nivelocupacion_rojo")
    smassa_sector_sare: Optional[str] = Field(..., alias="smassa_sector_sare")

    @validator("total_spots")
    def validate_total_spots(cls, v):
        return None if v == "None" else v

    @validator("disabled_spots")
    def validate_disabled_spots(cls, v):
        return None if v == "None" else v

    @validator("latest_updated")
    def validate_latest_updated(cls, v):
        return None if v == "None" else v

    @validator("available_disability_spots")
    def validate_available_disability_spots(cls, v):
        return None if v == "None" else v

    @validator("orange_occupation_level")
    def validate_orange_occupation_level(cls, v):
        return None if v == "None" else v

    @validator("red_occupation_level")
    def validate_red_occupation_level(cls, v):
        return None if v == "None" else v

    @validator("smassa_sector_sare")
    def validate_smassa_sector_sare(cls, v):
        return None if v == "None" else v
