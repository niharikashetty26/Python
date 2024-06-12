-- CREATE TABLE Projects (
--     project_id INT PRIMARY KEY,
--     project_name VARCHAR(100),
--     start_date DATE,
--     end_date DATE,
--     budget DECIMAL(10, 2)
-- );
-- CREATE TABLE Teams (
--     team_id INT PRIMARY KEY,
--     project_id INT,
--     team_name VARCHAR(100),
--     team_lead VARCHAR(100),
--     members_count INT,
--     FOREIGN KEY (project_id) REFERENCES Projects(project_id)
-- );
-- INSERT INTO Projects (project_id, project_name, start_date, end_date, budget) VALUES
-- (1, 'Project Alpha', '2024-01-01', '2024-06-01', 50000.00),
-- (2, 'Project Beta', '2024-02-15', '2024-08-15', 75000.00),
-- (3, 'Project Gamma', '2024-03-01', '2024-09-01', 60000.00),
-- (4, 'Project Delta', '2024-04-01', '2024-10-01', 80000.00),
-- (5, 'Project Epsilon', '2024-05-01', '2024-11-01', 55000.00),
-- (6, 'Project Zeta', '2024-06-01', '2024-12-01', 90000.00),
-- (7, 'Project Eta', '2024-07-01', '2024-12-31', 100000.00),
-- (8, 'Project Theta', '2024-08-01', '2025-01-31', 120000.00),
-- (9, 'Project Iota', '2024-09-01', '2025-02-28', 110000.00),
-- (10, 'Project Kappa', '2024-10-01', '2025-03-31', 130000.00);
-- INSERT INTO Teams (team_id, project_id, team_name, team_lead, members_count) VALUES
-- (1, 1, 'Alpha Team', 'Alice', 10),
-- (2, 1, 'Beta Team', 'Bob', 8),
-- (3, 2, 'Gamma Team', 'Charlie', 12),
-- (4, 3, 'Delta Team', 'David', 9),
-- (5, 4, 'Epsilon Team', 'Eve', 7),
-- (6, 5, 'Zeta Team', 'Frank', 6),
-- (7, 6, 'Eta Team', 'Grace', 11),
-- (8, 7, 'Theta Team', 'Heidi', 5),
-- (9, 8, 'Iota Team', 'Ivan', 8),
-- (10, 10, 'Kappa Team', 'Judy', 4);
SELECT *
FROM Projects;
SELECT *
FROM Teams;
SELECT Projects.project_id,
    Projects.project_name,
    Teams.team_name
FROM Projects
    INNER JOIN Teams ON Projects.project_id = Teams.project_id;
SELECT p.project_name,
    t.team_name,
    t.team_lead
FROM Projects p
    LEFT JOIN Teams t ON p.project_id = t.project_id;
SELECT p.project_name,
    t.team_name,
    t.team_lead
FROM Projects p
    RIGHT JOIN Teams t ON p.project_id = t.project_id;
SELECT p.project_name,
    t.team_name
FROM Projects p
    CROSS JOIN Teams t;
-- Find all projects along with their respective teams, 
-- if any. List project names and team names.
SELECT p.project_name,
    t.team_name
FROM Projects AS p
    LEFT JOIN Teams AS t ON p.project_id = t.team_id;
-- Find all teams and their respective projects, 
-- including those projects which don't have any teams assigned yet.
SELECT t.team_name,
    p.project_name
FROM Teams t
    RIGHT JOIN Projects p ON t.project_id = p.project_id;
-- List all projects that do not have any teams assigned to them.
SELECT p.project_name
FROM Projects p
    LEFT JOIN Teams t ON p.project_id = t.project_id
WHERE t.team_id IS NULL;
-- Find projects and their teams where the project budget is greater than $80,000.
SELECT p.project_name,
    t.team_name
FROM Projects p
    INNER JOIN Teams t ON p.project_id = t.project_id
WHERE p.budget > 80000.00;