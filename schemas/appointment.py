from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    date_time: datetime
    description: str

class AppointmentCreate(AppointmentBase):
    id_customer: int
    id_user: int

class Appointment(AppointmentBase):
    id_appointment: int
    id_customer: int
    id_user: int

    class Config:
        orm_mode = True
