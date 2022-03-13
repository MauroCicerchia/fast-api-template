from fastapi import FastAPI
from datetime import datetime
from schemas import *

app = FastAPI()

counter = 0

@app.post("/datetime")
def process_datetime(options: Optional[DatetimeOptions] = None):
    registerCall()
    return {"datetime": getDatetime(options and options.alternative_format)}


@app.get("/count")
def get_count():
    registerCall()
    return {"count": counter}


def registerCall():
    global counter
    counter += 1

def getDatetime(alternative_format):
    if(alternative_format):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        return datetime.now().strftime("%Y-%d-%m")


def getCount():
    return counter
