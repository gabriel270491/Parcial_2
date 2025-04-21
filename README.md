
# API RESTful - Vacunación contra el Sarampión en Panamá

Esta API de solo lectura proporciona datos históricos de vacunación contra el sarampión en niños de 12 a 23 meses en Panamá, desde 1983 hasta 2018.

## Requisitos

- Python 3.8+
- Flask

## Instalación

```bash
pip install Flask
```

## Ejecución

```bash
python app.py
```

## Endpoints

- `GET /api/v1/vacunacion`: Retorna todos los datos disponibles.
- `GET /api/v1/vacunacion/anio/<year>`: Retorna datos del año específico.
- `GET /api/v1/vacunacion/provincia/<provincia>`: Retorna datos por provincia (en este caso solo "Panamá").

## Pruebas

```bash
python test_api.py
```

## Fuente de datos

Datos obtenidos del [Banco Mundial](https://data.worldbank.org/indicator/SH.IMM.MEAS?end=2018&locations=PA&start=1983&view=chart).
