from fastapi import FastAPI
from datetime import datetime
from schemas import *
from counters import *

app = FastAPI()


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
    if(options and options.alternative_format):
        return {"datetime": datetime.now().strftime("%Y-%d-%m")}
    else:
        return {"datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


@app.get("/count")
async def get_count():
    registerCall()
    return {"count": getCount()}


def registerCall():
    Counter.registerCall()


def getCount():
    return Counter.getCount()
