import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from util.db_conn_util import DBConnUtil
from dao.hospital_service_impl import HospitalServiceImpl
from entity.appointment import Appointment
from entity.doctor import Doctor
from entity.patient import Patient
from exception.patient_number_not_found_exception import PatientNumberNotFoundException

def main():
    connection = None
    try:
        connection = DBConnUtil.get_connection()
        hospital_service = HospitalServiceImpl(connection)

        while True:
            print("\n1. Add Patient")
            print("2. Add Doctor")
            print("3. Schedule Appointment")
            print("4. Update Appointment")
            print("5. Cancel Appointment")
            print("6. Get Appointment by ID")
            print("7. Get Appointments for Patient")
            print("8. Get Appointments for Doctor")
            print("9. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                first_name = input("Enter Patient's First Name: ")
                last_name = input("Enter Patient's Last Name: ")
                address = input("Enter Address: ")
                dob = input("Enter Date of Birth (YYYY-MM-DD): ")
                phone = input("Enter Contact Number: ")
                gender = input("Enter Gender (M/F/Other): ")

                new_patient = Patient(None, first_name, last_name, address, dob, phone, gender)
                if hospital_service.add_patient(new_patient):
                    print("Patient added successfully.")
                else:
                    print("Failed to add patient.")

            elif choice == 2:
                first_name = input("Enter Doctor's First Name: ")
                last_name = input("Enter Doctor's Last Name: ")
                specialty = input("Enter Specialty: ")
                phone = input("Enter Contact Number: ")
                new_doctor = Doctor(None, first_name, last_name, specialty, phone)
                if hospital_service.add_doctor(new_doctor):
                    print("Doctor added successfully.")
                else:
                    print("Failed to add doctor.")

            elif choice == 3:
                patient_first_name = input("Enter Patient's First Name: ")
                doctor_first_name = input("Enter Doctor's First Name: ")
                appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
                description = input("Enter Appointment Description: ")

                try:
                    patient_id = hospital_service.get_patient_id_by_first_name(patient_first_name)
                    doctor_id = hospital_service.get_doctor_id_by_first_name(doctor_first_name)
                    appointment = Appointment(None, patient_id, doctor_id, appointment_date, description)
                    if hospital_service.schedule_appointment(appointment):
                        print("Appointment scheduled successfully.")
                    else:
                        print("Failed to schedule appointment.")
                except PatientNumberNotFoundException as e:
                    print(e)

            elif choice == 4:
                appointment_id = int(input("Enter Appointment ID to update: "))
                doctor_first_name = input("Enter new Doctor's First Name: ")
                appointment_date = input("Enter new Appointment Date (YYYY-MM-DD): ")
                description = input("Enter new Appointment Description: ")

                try:
                    doctor_id = hospital_service.get_doctor_id_by_first_name(doctor_first_name)
                    appointment = Appointment(appointment_id, None, doctor_id, appointment_date, description)
                    if hospital_service.update_appointment(appointment):
                        print("Appointment updated successfully.")
                    else:
                        print("Failed to update appointment.")
                except PatientNumberNotFoundException as e:
                    print(e)

            elif choice == 5:
                appointment_id = int(input("Enter Appointment ID to cancel: "))
                if hospital_service.cancel_appointment(appointment_id):
                    print("Appointment canceled successfully.")
                else:
                    print("Failed to cancel appointment.")

            elif choice == 6:
                appointment_id = int(input("Enter Appointment ID: "))
                appointment = hospital_service.get_appointment_by_id(appointment_id)
                if appointment:
                    print(f"Appointment ID: {appointment.get_appointment_id()}\n"
                          f"Patient ID: {appointment.get_patient_id()}\n"
                          f"Doctor ID: {appointment.get_doctor_id()}\n"
                          f"Appointment Date: {appointment.get_appointment_date()}\n"
                          f"Description: {appointment.get_description()}")
                else:
                    print("Appointment not found.")

            elif choice == 7:
                try:
                    patient_first_name = input("Enter Patient's First Name: ")
                    appointments = hospital_service.get_appointments_for_patient(patient_first_name)
                    if appointments:
                        for appointment in appointments:
                            print(f"Appointment ID: {appointment.get_appointment_id()}\n"
                                f"Patient ID: {appointment.get_patient_id()}\n"
                                f"Doctor ID: {appointment.get_doctor_id()}\n"
                                f"Date: {appointment.get_appointment_date()}\n"
                                f"Description: {appointment.get_description()}")
                            print()
                except PatientNumberNotFoundException as e:
                    print(e)

            elif choice == 8:
                try:
                   doctor_first_name = input("Enter Doctor's First Name: ")
                   appointments = hospital_service.get_appointments_for_doctor(doctor_first_name)
                   if appointments:
                        for appointment in appointments:
                            print(f"Appointment ID: {appointment.get_appointment_id()}\n"
                                f"Patient ID: {appointment.get_patient_id()}\n"
                                f"Doctor ID: {appointment.get_doctor_id()}\n"
                                f"Date: {appointment.get_appointment_date()}\n"
                                f"Description: {appointment.get_description()}")
                            print()
                   else:
                        print("No appointments found for this doctor.")
                except PatientNumberNotFoundException as e:
                    print(e)

            elif choice == 9:
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    main()
