from pydantic import BaseModel
from datetime import date

class AppointmentBase(BaseModel):
    appointment_date: date
    description: str
    id_customer: int

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(AppointmentBase):
    appointment_date: date = None
    description: str = None

class Appointment(AppointmentBase):
    id_appointment: int

    class Config:
        orm_mode = True
