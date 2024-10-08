from typing import List
from entity.appointment import Appointment
from entity.doctor import Doctor
from entity.patient import Patient
from dao.hospital_service import IHospitalService
from exception.patient_number_not_found_exception import PatientNumberNotFoundException

class HospitalServiceImpl(IHospitalService):
    def __init__(self, conn):
        self.conn = conn

    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        cursor = self.conn.cursor()
        query = """SELECT a.AppointmentId, a.PatientId, a.DoctorId, a.AppointmentDate, a.Description
                   FROM Appointments a
                   WHERE a.AppointmentId = ?"""
        cursor.execute(query, (appointment_id,))
        row = cursor.fetchone()
        return Appointment(*row) if row else None

    def get_appointments_for_patient(self, patient_id: str) -> List[Appointment]:
        cursor = self.conn.cursor()
        query = """SELECT a.AppointmentId, a.PatientId, a.DoctorId, a.AppointmentDate, a.Description
                   FROM Appointments a
                   JOIN Patients p ON a.PatientId = p.PatientId
                   WHERE p.FirstName = ?"""
        cursor.execute(query, (patient_id,))
        rows = cursor.fetchall()


        if not rows:
            raise PatientNumberNotFoundException()


        return [Appointment(*row) for row in rows]

    def get_appointments_for_doctor(self, doctor_id: str) -> List[Appointment]:
        cursor = self.conn.cursor()
        query = """SELECT a.AppointmentId, a.PatientId, a.DoctorId, a.AppointmentDate, a.Description
                   FROM Appointments a
                   JOIN Doctors d ON a.DoctorId = d.DoctorId
                   WHERE d.FirstName = ?"""
        cursor.execute(query, (doctor_id,))
        rows = cursor.fetchall()
        return [Appointment(*row) for row in rows]

    def schedule_appointment(self, appointment: Appointment) -> bool:
        cursor = self.conn.cursor()
        query = """INSERT INTO Appointments (PatientId, DoctorId, AppointmentDate, Description)
                   VALUES (?, ?, ?, ?)"""
        try:
            cursor.execute(query, (appointment.get_patient_id(), appointment.get_doctor_id(),
                                   appointment.get_appointment_date(), appointment.get_description()))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error while scheduling appointment: {e}")
            return False

    def update_appointment(self, appointment: Appointment) -> bool:
        cursor = self.conn.cursor()
        query = """UPDATE Appointments
                   SET DoctorId = ?, AppointmentDate = ?, Description = ?
                   WHERE AppointmentId = ?"""
        try:
            cursor.execute(query, (appointment.get_doctor_id(), appointment.get_appointment_date(),
                                   appointment.get_description(), appointment.get_appointment_id()))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error while updating appointment: {e}")
            return False

    def cancel_appointment(self, appointment_id: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Appointments WHERE AppointmentId = ?", (appointment_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def add_patient(self, patient: Patient) -> bool:
        cursor = self.conn.cursor()
        query = """INSERT INTO Patients (FirstName, LastName, Address, DateOfBirth, ContactNumber, Gender) 
                   VALUES (?, ?, ?, ?, ?, ?)"""
        try:
            cursor.execute(query, (patient.get_first_name(), patient.get_last_name(),
                                   patient.get_address(), patient.get_dob(), 
                                   patient.get_phone(), patient.get_gender()))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error while adding patient: {e}")
            return False

    def add_doctor(self, doctor: Doctor) -> bool:
        cursor = self.conn.cursor()
        query = """INSERT INTO Doctors (FirstName, LastName, Specialization, ContactNumber) 
                   VALUES (?, ?, ?, ?)"""
        try:
            cursor.execute(query, (doctor.get_first_name(), doctor.get_last_name(),
                                   doctor.get_specialization(), doctor.get_contact_number()))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error while adding doctor: {e}")
            return False

    def get_patient_id_by_first_name(self, first_name: str) -> int:
        cursor = self.conn.cursor()
        query = """SELECT PatientId FROM Patients WHERE FirstName = ?"""
        cursor.execute(query, (first_name,))
        row = cursor.fetchone()
        if not row:
            raise PatientNumberNotFoundException(f"Patient with name {first_name} not found.")
        return row[0]

    def get_doctor_id_by_first_name(self, first_name: str) -> int:
        cursor = self.conn.cursor()
        query = """SELECT DoctorId FROM Doctors WHERE FirstName = ?"""
        cursor.execute(query, (first_name,))
        row = cursor.fetchone()
        if not row:
            raise PatientNumberNotFoundException(f"Doctor with name {first_name} not found.")
        return row[0]
