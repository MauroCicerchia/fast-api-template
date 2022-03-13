from pydantic import BaseModel
from typing import Optional


class DatetimeOptions(BaseModel):
    alternative_format: Optional[bool] = False
