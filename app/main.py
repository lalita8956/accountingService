from fastapi import FastAPI
from app.database import engine, Base
from app.models import Company, Group
from app.schemas import CompanyCreate, GroupCreate
from app.database import SessionLocal

from sqlalchemy.orm import Session

app = FastAPI() 
Base.metadata.create_all(bind=engine)


        
@app.post("/companies/", response_model=CompanyCreate)
def create_company(company: CompanyCreate):
    db: Session = SessionLocal()
    db_company = Company(name=company.name)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    db.close()
    return db_company

@app.post("/groups/", response_model=GroupCreate)
def create_group(group: GroupCreate):
    db: Session = SessionLocal()
    db_group = Group(name=group.name, nature=group.nature, company_id=group.company_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    db.close()
    return db_group

@.get("/companies/{company_id}/groups/", response_model=list[GroupCreate])
def get_groups_by_company(company_id: int):
    db: Session = SessionLocal()
    groups = db.query(Group).filter(Group.company_id == company_id).all()
    db.close()
    return groups
