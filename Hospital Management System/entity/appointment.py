class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date, description):
        self.__appointment_id = appointment_id
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__appointment_date = appointment_date
        self.__description = description

    def get_appointment_id(self):
        return self.__appointment_id

    def get_patient_id(self):
        return self.__patient_id

    def get_doctor_id(self):
        return self.__doctor_id

    def get_appointment_date(self):
        return self.__appointment_date

    def get_description(self):
        return self.__description
    
    def set_appointment_id(self,appointment_id):
        self.__appointment_id=appointment_id
        
    def set_patient_id(self,patient_id):
        self.__patient_id=patient_id
        
    def set_doctor_id(self,doctor_id):
        self.__doctor_id=doctor_id
    
    def set_appointment_date(self,appointment_date):
        self.__appointment_date=appointment_date
        
    def set_description(self,description):
        self.__description=description
    
