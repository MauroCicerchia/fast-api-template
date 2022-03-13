from fastapi import FastAPI
from datetime import datetime
from schemas import *
from counters import *

app = FastAPI(
    title="Ejercicio Mauro Cicerchia",
    description="Prueba técnica - Marvik",
    version="0.1.0"
)


@app.on_event(event_type="startup")
def startup():
    db_startup()
    create_counters_table()


@app.on_event(event_type="shutdown")
def shutdown():
    db_shutdown()


@app.post("/datetime")
async def process_datetime(options: Optional[DatetimeOptions] = None):
    registerCall()
    return {"datetime": getDatetime(options and options.alternative_format)}


@app.get("/count")
async def get_count():
    registerCall()
    return {"count": getCount()}


def registerCall():
    Counter.registerCall()


def getDatetime(alternative_format):
    if(alternative_format):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        return datetime.now().strftime("%Y-%d-%m")


def getCount():
    return Counter.getCount()
