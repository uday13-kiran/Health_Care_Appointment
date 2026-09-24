from sqlalchemy import Column,String,ForeignKey,DateTime,UUID,Text,func,Date
import uuid
from core.database import Base


class Appointment (Base):
    __tablename__='appointment'
    appointment_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    patient_id=Column(UUID(as_uuid=True),ForeignKey('patient.patient_id'))
    doctor_id=Column(UUID(as_uuid=True),ForeignKey('doctor.doctor_id'))
    appointment_date=Column(Date,nullable=False)
    start_time=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    end_time=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    status=Column(String(25),nullable=False)
    reason=Column(String(25),nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)


class Visit (Base):
    __tablename__='visit'
    visit_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    patient_id=Column(UUID(as_uuid=True),ForeignKey('patient.patient_id'))
    appoint_id=Column(UUID(as_uuid=True),ForeignKey('appointment.appointment_id'))
    check_in_time=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    check_out_time=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    status=Column(String(25),nullable=False)
    notes=Column(Text(250),nullable=False)


class Consultation (Base):
    __tablename__= 'consultation'
    Consultation_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    visit_id=Column(UUID(as_uuid=True),ForeignKey('visit.visit_id'))
    doctor_id=Column(UUID(as_uuid=True),ForeignKey('doctor.doctor_id'))
    start_time=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    end_time=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    diagnosis=Column(String(250),nullable=False)
    prescription=Column(String(250),nullable=False)
    notes=Column(Text(250),nullable=False)
    status=Column(String(25),nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)



class Queue (Base):
    __tablename__='queue'
    queue_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    visit_id=Column(UUID(as_uuid=True),ForeignKey('visit.visit_id'))
    queue_number=Column(String(25),nullable=False)
    status=Column(String(25),nullable=False)
    added_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    called_at=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    priority=Column(String(250),nullable=False)


class Audit_Log (Base):
    log_id=Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    visit_id=Column(UUID(as_uuid=True),ForeignKey('visit.visit_id'))
    action=Column(String(25),nullable=False)
    details=Column(String(25),nullable=False)
    timestamp=Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

