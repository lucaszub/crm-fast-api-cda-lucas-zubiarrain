from pydantic import BaseModel

class ServiceCreate(BaseModel):
    service_name: str
    description: str
    price: float


class ServiceOut(ServiceCreate):
    id_service: int

    class Config:
        orm_mode = True
