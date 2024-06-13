-- CREATE TABLE Students (
--     StudentID INT PRIMARY KEY,
--     FirstName VARCHAR(50),
--     LastName VARCHAR(50),
--     Major VARCHAR(50),
--     Year INT
-- );
-- CREATE TABLE Subjects (
--     CourseID INT PRIMARY KEY,
--     CourseName VARCHAR(100),
--     Department VARCHAR(50),
--     Credits INT
-- );
-- CREATE TABLE Enrollments (
--     EnrollmentID INT PRIMARY KEY,
--     StudentID INT,
--     CourseID INT,
--     Grade CHAR(2),
--     FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
--     FOREIGN KEY (CourseID) REFERENCES Subjects(CourseID)
-- );
-- INSERT INTO Students (StudentID, FirstName, LastName, Major, Year) VALUES
-- (1, 'Alice', 'Johnson', 'Computer Science', 3),
-- (2, 'Bob', 'Smith', 'Mathematics', 2),
-- (3, 'Charlie', 'Brown', 'Physics', 4),
-- (4, 'David', 'Williams', 'Engineering', 1);
-- INSERT INTO Subjects (CourseID, CourseName, Department, Credits) VALUES
-- (101, 'Introduction to Computer Science', 'Computer Science', 4),
-- (102, 'Calculus I', 'Mathematics', 3),
-- (103, 'General Physics', 'Physics', 4),
-- (104, 'Engineering Mechanics', 'Engineering', 3);
-- INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, Grade) VALUES
-- (1, 1, 101, 'A'),
-- (2, 1, 102, 'B'),
-- (3, 2, 102, 'A'),
-- (4, 3, 103, 'C'),
-- (5, 4, 104, 'B');
SELECT *
FROM Students;
SELECT *
FROM Subjects;
SELECT *
FROM Enrollments;
-- 1. Find the names of students who are enrolled in the 'Computer Science' department courses.
SELECT FirstName,
    LastName
FROM Students
WHERE studentid IN(
        SELECT studentid
        FROM Enrollments
        WHERE courseid IN(
                SELECT CourseId
                FROM Subjects
                WHERE department = 'Computer Science'
            )
    );
-- 2. List the course names 
-- and departments of courses that have more than one student enrolled.
SELECT CourseName,
    Department
FROM Subjects
WHERE CourseId IN (
        SELECT CourseID
        FROM Enrollments
        GROUP BY CourseID
        HAVING COUNT(StudentID) > 1
    );
-- 3. Find the students who have a grade 'A' in any course.
SELECT FirstName,
    LastName
FROM Students
WHERE StudentId IN (
        SELECT studentid
        FROM Enrollments
        WHERE Grade = 'A'
    );
-- 4. Find the names of students who are not enrolled in any courses.
SELECT FirstName,
    LastName
FROM Students
WHERE StudentID NOT IN (
        SELECT StudentID
        FROM Enrollments
    );
-- 5. List the courses that are taken by students majoring in 'Mathematics'.
SELECT CourseName
FROM Subjects
WHERE CourseID IN (
        SELECT CourseID
        FROM Enrollments
        WHERE StudentID IN (
                SELECT StudentID
                FROM Students
                WHERE Major = 'Mathematics'
            )
    );