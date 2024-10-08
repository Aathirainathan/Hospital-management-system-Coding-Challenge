from abc import ABC, abstractmethod
from typing import List
from entity.appointment import Appointment
from entity.doctor import Doctor
from entity.patient import Patient

class IHospitalService(ABC):
    @abstractmethod
    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        pass

    @abstractmethod
    def get_appointments_for_patient(self, patient_id: str) -> List[Appointment]:
        pass

    @abstractmethod
    def get_appointments_for_doctor(self, doctor_id: str) -> List[Appointment]:
        pass

    @abstractmethod
    def schedule_appointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def update_appointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancel_appointment(self, appointment_id: int) -> bool:
        pass

    @abstractmethod
    def add_patient(self, patient: Patient) -> bool:
        pass

    @abstractmethod
    def add_doctor(self, doctor: Doctor) -> bool:
        pass

    @abstractmethod
    def get_patient_id_by_first_name(self, first_name: str) -> int:
        pass

    @abstractmethod
    def get_doctor_id_by_first_name(self, first_name: str) -> int:
        pass
