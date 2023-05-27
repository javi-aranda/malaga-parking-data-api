# Málaga Parking Data API

El proyecto Málaga Parking Data API nace para darle forma a los datos recopilados en el repositorio
[malaga-parking-data](https://github.com/javisenberg/malaga-parking-data).

## Instalación de dependencias y uso

Se puede clonar el proyecto mediante el comando
```bash
~ git clone https://github.com/javisenberg/malaga-parking-data-api.git
```

Para trabajar de forma local se recomienda crear un entorno virtual de Python >= 3.9
```bash
~ python3.9 -m venv ~/.venvs/malaga-parking-api
~ source ~/.venvs/malaga-parking-api/bin/activate
(malaga-parking-api) ~ pip install -r requirements/requirements.txt
(malaga-parking-api) ~ uvicorn app.main:app --port 8000
```

La documentación de los endpoint se encuentra disponible en `/api/docs`.

La respuesta de la API `GET /api/v1/latest` es:

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
