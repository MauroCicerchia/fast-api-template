from fastapi import FastAPI
from datetime import datetime
from schemas import *

app = FastAPI()

counter = 0

@app.post("/datetime")
def process_datetime(options: Optional[DatetimeOptions] = None):
    registerCall()
    if(options and options.alternative_format):
        return {"datetime": datetime.now().strftime("%Y-%d-%m")}
    else:
        return {"datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


@app.get("/count")
def get_count():
    registerCall()
    return {"count": counter}


def registerCall():
    global counter
    counter += 1