from sqlalchemy import Column,String,ForeignKey,DateTime,UUID,Text,func
import uuid
from core.database import Base

class Specialization(Base):
    __tablaname__='specialization'
    specialization_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name=Column(String(200),nullable=False)
    description=Column(Text,nullable=False)

class Docotr(Base):
    __tablename__='doctor'
    doctor_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name=Column(String(225),nullable=False)
    specialization=Column(UUID(as_uuid=True),ForeignKey('specialization.specialization_id'))
    phone=Column(String(10),nullable=False,unique=True)
    email=Column(String(225),nullable=False,unique=True)
    qualification=Column(String(100),nullable=False)
    status=Column(String(25),nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

class Patient