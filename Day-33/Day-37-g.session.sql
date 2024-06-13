-- CREATE TABLE Patients (
--     PatientID SERIAL PRIMARY KEY,
--     PatientName VARCHAR(100),
--     DoctorName VARCHAR(100),
--     Department VARCHAR(50)
-- );
-- INSERT INTO Patients (PatientName, DoctorName, Department)
-- VALUES ('John Doe', 'Dr. Smith', 'Cardiology'),
--     ('Jane Roe', 'Dr. Johnson', 'Neurology'),
--     ('Alice Brown', 'Dr. Lee', 'Pediatrics'),
--     ('Bob White', 'Dr. Miller', 'Orthopedics'),
--     ('Carol Black', 'Dr. Davis', 'Oncology');
-- FINDING Department as Oncology through Stored Procedures.
CREATE OR REPLACE FUNCTION PatientsData(p_Department VARCHAR) RETURNS TABLE (
        PatientName VARCHAR,
        DoctorName VARCHAR,
        Department VARCHAR
    ) AS $$ BEGIN RETURN QUERY
SELECT p.PatientName,
    p.DoctorName,
    p.Department
FROM Patients as p
WHERE p.Department = p_Department;
END;
$$ LANGUAGE plpgsql;
SELECT *
FROM PatientsData('Oncology');