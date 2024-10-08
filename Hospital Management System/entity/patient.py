class Patient:
    def __init__(self, patient_id, first_name, last_name, address, dob, phone, gender):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__dob = dob
        self.__phone = phone
        self.__gender = gender  # Added gender attribute

    def get_patient_id(self):
        return self.__patient_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_dob(self):
        return self.__dob

    def get_phone(self):
        return self.__phone

    def get_gender(self):
        return self.__gender

    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number
        
    def set_gender(self, gender):
        self.__gender = gender
