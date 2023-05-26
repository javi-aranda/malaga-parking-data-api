# Málaga Parking Data API

El proyecto Málaga Parking Data API nace para darle forma a los datos recopilados en el repositorio
[malaga-parking-data](https://github.com/javisenberg/malaga-parking-data).

## Uso

La documentación de los endpoint se encuentra disponible en `/api/docs`.

La respuesta de la API `GET /api/v1/latest/` es:

```json
[
  {
    "parking_id": 1,
    "name": "Salitre",
    "address": "Calle SalitreMálaga",
    "contact_number": "",
    "email_address": "",
    "latitude": 36.7132149,
    "longitude": -4.4276681,
    "altitude": 3.986444,
    "total_spots": "342",
    "disabled_spots": "None",
    "latest_updated": "None",
    "available_spots": 181,
    "available_disability_spots": "None",
    "orange_occupation_level": "17",
    "red_occupation_level": "5",
    "smassa_sector_sare": "None"
  },
  {
    "parking_id": 2,
    "name": "Cervantes",
    "address": "Calle CervantesMálaga",
    "contact_number": "",
    "email_address": "",
    "latitude": 36.7208633,
    "longitude": -4.4119148,
    "altitude": 9.531203,
    "total_spots": "414",
    "disabled_spots": "None",
    "latest_updated": "None",
    "available_spots": 55,
    "available_disability_spots": "None",
    "orange_occupation_level": "22",
    "red_occupation_level": "5",
    "smassa_sector_sare": "None"
  },
  // ...
]
```
