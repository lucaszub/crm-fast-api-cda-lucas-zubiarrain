from sqlalchemy.orm import Session
from models import Appointment
from schemas.appointment import AppointmentCreate
from datetime import datetime

class AppointmentService:
    @staticmethod
    def create_appointment(db: Session, appointment: AppointmentCreate):
        db_appointment = Appointment(
            id_customer=appointment.id_customer,
            id_user=appointment.id_user,
            date_time=appointment.date_time,
            description=appointment.description
        )
        db.add(db_appointment)
        db.commit()
        db.refresh(db_appointment)
        return db_appointment

    @staticmethod
    def get_appointments_by_customer(db: Session, customer_id: int):
        return db.query(Appointment).filter(Appointment.id_customer == customer_id).all()

    @staticmethod
    def update_appointment(db: Session, appointment_id: int, appointment: AppointmentCreate):
        db_appointment = db.query(Appointment).filter(Appointment.id_appointment == appointment_id).first()
        if not db_appointment:
            return None
        db_appointment.date_time = appointment.date_time
        db_appointment.description = appointment.description
        db.commit()
        db.refresh(db_appointment)
        return db_appointment

    @staticmethod
    def delete_appointment(db: Session, appointment_id: int):
        db_appointment = db.query(Appointment).filter(Appointment.id_appointment == appointment_id).first()
        if not db_appointment:
            return None
        db.delete(db_appointment)
        db.commit()
        return db_appointment
