# Hospital-management-system-Coding-Challenge


<h2>Sql Schema</h2>

<h4>-- Table 1 Patients</h4>

CREATE TABLE Patients (
    PatientId INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(100) NOT NULL,
    LastName NVARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender NVARCHAR(10) NOT NULL,
    ContactNumber NVARCHAR(15) NOT NULL,
    Address NVARCHAR(255) NOT NULL
);

<h4>-- Table 2 Doctors</h4>

CREATE TABLE Doctors (
    DoctorId INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(100) NOT NULL,
    LastName NVARCHAR(100) NOT NULL,
    Specialization NVARCHAR(100) NOT NULL,
    ContactNumber NVARCHAR(15) NOT NULL
);

<h4>-- Table 3 Appointments</h4>
CREATE TABLE Appointments (
    AppointmentId INT IDENTITY(1,1) PRIMARY KEY,
    PatientId INT NOT NULL FOREIGN KEY REFERENCES Patients(PatientId),
    DoctorId INT NOT NULL FOREIGN KEY REFERENCES Doctors(DoctorId),
    AppointmentDate DATE NOT NULL,
    Description NVARCHAR(255) NULL
);


<h4>-- Insert Records</h4>

INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, ContactNumber, Address)
VALUES 
('Rahul', 'Sharma', '1992-07-20', 'Male', '9876543210', '123, Sector 15, Gurgaon, Haryana'),
('Anjali', 'Verma', '1988-11-05', 'Female', '8765432109', '45, Main Road, Indore, Madhya Pradesh'),
('Arjun', 'Singh', '1995-01-12', 'Male', '9988776655', '67, Park Street, Kolkata, West Bengal'),
('Sneha', 'Reddy', '1990-03-25', 'Female', '9123456789', '90, MG Road, Bangalore, Karnataka'),
('Vikram', 'Patel', '1985-08-30', 'Male', '8123456789', '34, Ashok Nagar, Ahmedabad, Gujarat'),
('Priya', 'Kumar', '1994-06-15', 'Female', '9321456789', '22, MG Road, Chennai, Tamil Nadu'),
('Mohit', 'Yadav', '1991-10-10', 'Male', '8421356789', '78, Sadar Bazaar, Jaipur, Rajasthan'),
('Tanya', 'Malhotra', '1987-12-28', 'Female', '7321456789', '55, Connaught Place, Delhi'),
('Ravi', 'Nair', '1993-04-18', 'Male', '6521456789', '10, Marine Drive, Mumbai, Maharashtra'),
('Neha', 'Iyer', '1990-09-22', 'Female', '5621456789', '44, M G Road, Pune, Maharashtra');


INSERT INTO Doctors (FirstName, LastName, Specialization, ContactNumber) 
VALUES 
('Amit', 'Sharma', 'Cardiology', '9988776655'),
('Neha', 'Kapoor', 'Dermatology', '9876543210'),
('Raj', 'Mehta', 'Orthopedics', '8765432109'),
('Pooja', 'Desai', 'Pediatrics', '7654321098'),
('Vikram', 'Reddy', 'Neurology', '6543210987'),
('Anjali', 'Joshi', 'General Medicine', '5432109876'),
('Sunil', 'Verma', 'ENT', '4321098765'),
('Kriti', 'Malhotra', 'Gynecology', '3210987654'),
('Arjun', 'Bhatia', 'Oncology', '2109876543'),
('Priya', 'Chopra', 'Psychiatry', '1098765432');

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<h2>Output Screenshots:</h2>
<h4>1. Add Patient to the database:</h4>
   
   ![image](https://github.com/user-attachments/assets/398beee0-ee1d-4f15-9f54-5bb63ae6b289)
   ![image](https://github.com/user-attachments/assets/69974064-2c8a-4a1f-88ca-da4c4ca41516)

<h4>2. Add Doctor to the database:</h4>
   
   ![image](https://github.com/user-attachments/assets/249f8fec-e28d-4f3f-b327-dd03373e2053)
   ![image](https://github.com/user-attachments/assets/98b53687-4527-4a65-bf57-6f9276bf1397)

<h4>3. Schedule Appointment:</h4>
   
   ![image](https://github.com/user-attachments/assets/ae1e552f-46d7-4900-aeda-d03faa08c487)
   ![image](https://github.com/user-attachments/assets/8c4ee3fb-8f56-47d8-8088-41354b6ad70d)

<h4>4. Update Appointment:(Change Appointment Date):</h4>
   
   ![Screenshot 2024-10-08 115539](https://github.com/user-attachments/assets/1d91cb70-4760-41c0-81c2-88d74bb6b47d)
   ![Screenshot 2024-10-08 115625](https://github.com/user-attachments/assets/92769d14-94fa-4a29-ae9a-ae33e4b303ad)

<h4>5. Cancel Appointment:</h4>

   ![image](https://github.com/user-attachments/assets/1b72cab4-261d-4a79-8485-c627dd63e03c)
   
   <h4>Deleted From database</h4>
   
   ![image](https://github.com/user-attachments/assets/3d43c582-3fcc-4195-afa0-1c07f41c4810)
   
<h4>7. Get Appointment by ID:</h4>

   ![image](https://github.com/user-attachments/assets/aadb0dac-a7f6-4951-b9e3-18d6859b385b)

<h4>8. Get Appointments for Patient:</h4>
   
   ![image](https://github.com/user-attachments/assets/20eda319-c69e-460b-8fc9-fa5e462b19c6)

<h4>9. Get Appointments for Doctor:</h4>

   ![image](https://github.com/user-attachments/assets/bc945c9a-b20b-4dff-b8b7-ef0d9d24bb7a)

<h4>10. Patient Number Not Found Exception:</h4>

   ![image](https://github.com/user-attachments/assets/c99b3bc1-85c7-42d2-aa19-b1f3c3c14664)


    






