from pydantic import BaseModel
from typing import Optional


class CompanyCreate(BaseModel):
    name: str

class GroupCreate(BaseModel):
    name: str
    nature: str
    company_id: int
    
class GroupResponse(BaseModel):
    id: int
    name: str
    nature: str
    company_id: int

    class Config:
        orm_mode = True
        