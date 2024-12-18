# from fastapi import APIRouter, Depends, HTTPException
# from typing import List
# from sqlalchemy.orm import Session
# from schemas.appointment import AppointmentSchema
# from schemas.customer import ClientSchema
# from services.rendezvous import AppointmentHandler
# from db.database import get_db

# router = APIRouter()

# @router.post("/rdv/")
# def create_appointment(rdv:AppointmentSchema, db : Session = Depends(get_db)):
#     service = AppointmentHandler(db)
#     try:
#         new_rdv = service.schedule_appointment(rdv)
#         return {"message" : "rdv ajouté avec succès", "rdv": new_rdv}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail="Erreur lors de l'ajout du rdv")

# @router.get("/rdv/list/")
# def list_appointments_by_client(nom: str, prenom: str, db: Session = Depends(get_db)):
#     service = AppointmentHandler(db)
#     try:
#         appointments = service.list_appointments_by_client(nom, prenom)
#         if isinstance(appointments, list):
#             return {"message": "Rendez-vous récupérés avec succès", "appointments": appointments}
#         else:
#             return {"message": appointments}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Erreur lors de la récupération des rendez-vous: {str(e)}")
