from sqlalchemy import Column,String,Boolean,ForeignKey,DateTime,UUID,Text,func,Date
import uuid
from core.database import Base

class Doctor_Availability (Base):
    __tablename__='doctor_availability'
    availability_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    doctor_id=Column(UUID(as_uuid=True),ForeignKey('doctor.doctor_id'))
    day_of_week=Column(String(25),nullable=False)
    start_time=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    end_time=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    is_break=Column(Boolean,nullable=False,default=False)
    is_leave=Column(Boolean,nullable=False,default=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)



class Leave (Base):
    __tablename__='leave'
    leave_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    doctor_id=Column(UUID(as_uuid=True),ForeignKey('doctor.doctor_id'))
    start_date=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    end_date=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    reason=Column(String(25),nullable=False)
    status=Column(String(25),nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)