-- CREATE TABLE Courses (
--     CourseID SERIAL PRIMARY KEY,
--     CourseName VARCHAR(100),
--     InstructorName VARCHAR(100),
--     Department VARCHAR(100)
-- );
-- INSERT INTO Courses (CourseName, InstructorName, Department)
-- VALUES (
--         'Introduction to Psychology',
--         'Dr. John Doe',
--         'Psychology'
--     ),
--     ('Calculus I', 'Dr. Jane Smith', 'Mathematics'),
--     ('World History', 'Dr. Alice Johnson', 'History'),
--     (
--         'Organic Chemistry',
--         'Dr. Robert Brown',
--         'Chemistry'
--     ),
--     ('Microeconomics', 'Dr. Emily White', 'Economics');
CREATE OR REPLACE FUNCTION GetCoursesByDepartment(department VARCHAR) RETURNS TABLE(CourseName VARCHAR, InstructorName VARCHAR) AS $$ BEGIN RETURN QUERY
SELECT c.CourseName,
    c.InstructorName
FROM Courses c
WHERE c.Department = GetCoursesByDepartment.department;
END;
$$ LANGUAGE plpgsql;
SELECT *
FROM GetCoursesByDepartment('Psychology');