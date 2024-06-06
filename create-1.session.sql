-- CREATE TABLE Student(
--     FirstName VARCHAR(50),
--     LastName VARCHAR(50),
--     RollNo INT NOT NULL,
--     GRADE VARCHAR(10),
--     DOB DATE,
--     PRIMARY KEY (RollNo)
-- );
-- INSERT INTO Student (FirstName, LastName, RollNo, GRADE, DOB)
-- VALUES ('Mishti', 'Sethi', 1, 'A', '2015-12-23');
-- INSERT INTO Student (FirstName, LastName, RollNo, GRADE, DOB)
-- VALUES ('Ravi', 'Kumar', 2, 'B', '2016-03-15'),
--     ('Anya', 'Sharma', 3, 'A', '2015-07-19'),
--     ('Rahul', 'Verma', 4, 'C', '2016-11-25'),
--     ('Sneha', 'Patel', 5, 'B', '2015-09-30');
-- INSERT INTO Student
-- VALUES('Smita', 'Salvi', 6, 'A', '2015-12-12');
INSERT INTO Student
VALUES('Tejas', 'Chapake', 7, 'C', '2016-06-12'),
    ('Manoj', 'Chandu', 8, 'B', '2015-06-1');
SELECT *
FROM Student