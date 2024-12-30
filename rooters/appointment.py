from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.appointment import AppointmentCreate, Appointment
from services.appointment import AppointmentService
router = APIRouter()

@router.post("/appointments/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    created_appointment = AppointmentService.create_appointment(db=db, appointment=appointment)
    return Appointment.from_orm(created_appointment)

@router.get("/appointments/{customer_id}", response_model=list[Appointment])
def get_appointments(customer_id: int, db: Session = Depends(get_db)):
    appointments = AppointmentService.get_appointments_by_customer(db=db, customer_id=customer_id)
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found for this customer")
    return [Appointment.from_orm(appointment) for appointment in appointments]

@router.put("/appointments/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: AppointmentCreate, db: Session = Depends(get_db)):
    updated_appointment = AppointmentService.update_appointment(db=db, appointment_id=appointment_id, appointment=appointment)
    if not updated_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return Appointment.from_orm(updated_appointment)

@router.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    deleted_appointment = AppointmentService.delete_appointment(db=db, appointment_id=appointment_id)
    if not deleted_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted successfully"}
