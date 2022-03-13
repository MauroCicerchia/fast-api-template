# Ejercicio Mauro Cicerchia

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

La documentación de la API se encuentra [aquí](https://documenter.getpostman.com/view/9096048/UVsJvmqH)

También puede encontrarse una vez levantada la aplicación, en la ruta `/docs`

## Aclaraciones

Tomé la decisión de persistir el contador de llamadas. En caso de no querer utilizar la base de datos, en la rama `no-db-version` se encuentra otra versión de la aplicación implementada sin base de datos.

Asumí que el contador debía contar llamadas tanto al endpoint de `POST /datetime` como al de `GET /count` según lo que interpreté en la consigna.
