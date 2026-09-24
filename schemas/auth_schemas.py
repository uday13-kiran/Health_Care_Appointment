from pydantic import Field,BaseModel
from datetime import date,datetime
from typing import Optional
from uuid import UUID 

class CreateDoctor(BaseModel):
    name:str = Field(min_length = 1,max_length = 100, description = 'full name of doctor' )
    specialization_id:UUID = Field(...,description='unique id of doctor specializtion')
    phone: str = Field(min_length = 10, max_length = 20,description = ' phone number of doctor')
    email: str = Field(min_length = 19,max_length = 30, description = 'email of the doctor')
    qualification: str = Field(min_length = 20,max_length = 50,description = 'qualification of doctor')
    status:str = Field(min_length = 20,max_length = 40,description = 'current status of doctor')
    
class CreateAppointment(BaseModel):
    patient_id:UUID = Field(...,decription = 'unique id of patient appointment')
    doctor_id:UUID = Field(...,description = 'unique id of doctor appointment' )
    appointment_date:date = Field(...,description = 'date of patient appointment')
    start_time:datetime = Field (...,description = 'starttime of appointment')
    end_time:datetime = Field (...,description = 'endtime of appointment') 
    status:str = Field (min_length = 20,max_length = 40,decription = 'status of the appointment') 
    reason:str = Field (...,description = 'reason for appointment')
    
class CreatePatient(BaseModel):
    name:str = Field(...,description = 'patient full name')
    gender:str = Field(...,description = 'gender of the patient') 
    date_of_birth:date = Field(...,description = 'patient birth date')
    phone:str = Field (...,description = 'patient phone num')
    email:str = Field (...,description = 'patient email')
    address:str = Field (...,description = 'patient address') 
    
class CreateVisit(BaseModel):
    patient_id:UUID = Field(...,description = 'unidue id of patient visit') 
    appointment_id:UUID = Field(...,description = 'unidue id of appointment')
    check_in_time:datetime = Field(...,description = 'appointment check in time')
    check_out_time:datetime = Field(...,description = 'appointment check out time')
    status:str = Field (min_length = 20,max_length = 40,decription = 'status of the visit')
    notes:str = Field (...,description = 'notes of visit') 
    
class CreateQueue(BaseModel):
    visit_id:UUID = Field(...,description = 'visit id queue')
    queue_number:str = Field(...,description = 'queue number')
    status:str = Field(...,description = 'queue status')
    added_at:str = Field(...,description = 'added at queue')
    called_at:str = Field(...,description = 'called at queue')
    priority:str = Field(...,description = 'priority of queue')
    
class CreateStaff(BaseModel):
    name:str = Field(...,description = 'staff names')
    role:str = Field(...,description = 'staff roles') 
    phone:str = Field (...,description = 'staff phone numbers')
    email:str = Field (...,description = 'staff emails')      
    username:str = Field(...,description = 'staff usernames ')
    password_hash:str = Field(...,description = 'staff password hash') 
     
class CreateDoctor_Availability(BaseModel):
    doctor_id:UUID = Field(...,description = 'doctor leaves')
    day_of_week:str = Field(...,description = 'availabity days in week')
    start_time:str = Field(...,description = 'available timings')
    end_time:str = Field(...,description = 'available end timings')
    is_break:str = Field(...,description = 'available breaks')
    is_leave:str = Field(...,description = 'available leaves')
    
    
class CreateLeave(BaseModel):
    doctor_id:UUID = Field(...,description = 'doctor leaves')
    start_date:str = Field(...,description = 'leave starting date') 
    end_date:str = Field(...,description = 'leaves ending date')
    reason:str = Field(...,description = 'reason for leaves')
    status:str = Field(...,description = 'leaves status') 
    
class CreateConsultation(BaseModel):
    visit_id:UUID = Field(...,description = 'visit for consultation')
    doctor_id:UUID = Field(...,description = 'doctor consultation')
    start_time:str = Field(...,description = 'consultation start timings')
    end_time:str = Field(...,description = 'consultation end timing')
    diagnosis:str = Field(...,description = 'consulatation diagnosis')
    prescription:str = Field(...,description = 'prescription ')
    notes:str = Field(...,description = 'notes for consultation')
    status:str = Field(...,description = 'consultation status')
    
class CreateAudit_Log(BaseModel):
    visit_id:UUID = Field(...,description = 'audit_log  visit')
    user_id:UUID = Field(...,description = 'audit_log user')
    action:str = Field(...,description = 'audit_log action')
    details:str = Field(...,description = 'audit_log details') 
    timestamp:str = Field(...,description = 'audit_log timestamp')
          