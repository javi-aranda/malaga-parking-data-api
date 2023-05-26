# Málaga Parking Data API

El proyecto Málaga Parking Data API nace para darle forma a los datos recopilados en el repositorio 
[malaga-parking-data](https://github.com/javisenberg/malaga-parking-data).

## Uso

La respuesta de la API será en un formato similar a:

```json
[
  {
    "poiID": "1",
    "nombre": "Salitre",
    "direccion": "Calle SalitreMu00e1laga",
    "telefono": "",
    "correoelectronico": "",
    "latitude": "36.7132149",
    "longitude": "-4.4276681",
    "altitud": "3.986444",
    "capacidad": "342",
    "capacidad_discapacitados": "None",
    "fechahora_ultima_actualizacion": "None",
    "libres": "174",
    "libres_discapacitados": "None",
    "nivelocupacion_naranja": "17",
    "nivelocupacion_rojo": "5",
    "smassa_sector_sare": "None",
  },
  {
    "poiID": "2",
    "nombre": "Cervantes",
    "direccion": "Calle CervantesMu00e1laga",
    "telefono": "",
    "correoelectronico": "",
    "latitude": "36.7208633",
    "longitude": "-4.4119148",
    "altitud": "9.531203",
    "capacidad": "414",
    "capacidad_discapacitados": "None",
    "fechahora_ultima_actualizacion": "None",
    "libres": "55",
    "libres_discapacitados": "None",
    "nivelocupacion_naranja": "22",
    "nivelocupacion_rojo": "5",
    "smassa_sector_sare": "None",
  },
  // ...
]
```