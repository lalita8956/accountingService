from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base   



class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nature = Column(String)  # Asset / Liability / Income / Expense
    company_id = Column(Integer, ForeignKey("companies.id"))