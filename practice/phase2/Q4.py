from pydantic import BaseModel, model_validator
from datetime import date

class Booking(BaseModel):
    start_date: date
    end_date: date

    @model_validator(mode="after")
    def date_check(self):
        if self.end_date <= self.start_date:
            raise ValueError("end_date must be after start_date")
        return self

b1 = Booking(start_date="2026-01-10", end_date="2026-02-05")
print(b1)
b2 = Booking(start_date="2026-05-10", end_date="2026-04-02")