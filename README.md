# FastAPI template

## Requisitos

- Clonar el repositorio
- Instalar pipenv con `pip install pipenv` (en caso de no tenerlo instalado)
- Instalar dependencias con `pipenv install`
- Levantar una instancia de Postgres
  - Utilizando docker con `docker run -p 5432:5432 -e POSTGRES_PASSWORD=admin -d postgres`
  - Utilizando una propia y configurando la aplicación con las variables de entorno
    - `DB_HOST`
    - `DB_PORT`
    - `DB_USER`
    - `DB_PASSWORD`
    - `DB_DATABASE`

## Ejecución

Servir la aplicación usando `pipenv run serve`

## Documentación

La documentación de la API se encuentra en la ruta `/docs`
