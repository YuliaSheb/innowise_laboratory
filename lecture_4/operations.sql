--Create tables--
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(id)
);

--insert values to tables--
INSERT INTO Students (full_name, birth_year) VALUES
('Alice Johnson',2005),
('Brian Smith',2004),
('Carla Reyes',2006),
('Daniel Kim',2005),
('Eva Thompson',2003),
('Felix Nguyen',2007),
('Grace Patel',2005),
('Henry Lopez',2004),
('Isabella Martinez',2006);

INSERT INTO Grades (student_id, subject, grade) VALUES
(1,'Math',88),
(1,'English',92),
(1,'Science',85),
(2,'Math',75),
(2,'History',83),
(2,'English',79),
(3,'Science',95),
(3,'Math',91),
(3,'Art',89),
(4,'Math',84),
(4,'Science',88),
(4,'Physical Education',93),
(5,'English',90),
(5,'History',85),
(5,'Math',88),
(6,'Science',72),
(6,'Math',78),
(6,'English',81),
(7,'Art',94),
(7,'Science',87),
(7,'Math',90),
(8,'History',77),
(8,'Math',83),
(8,'Science',80),
(9,'English',96),
(9,'Math',89),
(9,'Art',92);

--create indexes for optimize--
CREATE INDEX IF NOT EXISTS idx_grades_student_id
    ON Grades(student_id);

CREATE INDEX IF NOT EXISTS idx_students_full_name
    ON Students(full_name);

CREATE INDEX IF NOT EXISTS idx_grades_grade
    ON Grades(grade);

--find all grades for Alice Johnson--
SELECT grade FROM Grades
WHERE student_id = (SELECT id FROM Students WHERE full_name = 'Alice Johnson');

--Calculate the average grade per student--
SELECT Students.full_name, AVG(GRADES.grade) as avg_grade FROM Grades
JOIN Students ON Students.id = Grades.student_id GROUP BY Students.full_name;

--list all student born after 2004--
SELECT id, full_name, birth_year from Students where birth_year > 2004;

--create a query that lists all subjects and their average grades--
SELECT subject, AVG(grade) as avg_grade FROM Grades
GROUP BY subject;

--find the top 3 students--
SELECT Students.full_name, AVG(GRADES.grade) as avg_grade FROM Grades
JOIN Students ON Students.id = Grades.student_id GROUP BY Students.full_name ORDER BY avg_grade DESC LIMIT 3;

--all students who scored below 80 in any subject--
SELECT DISTINCT full_name FROM Students WHERE id IN (SELECT student_id FROM Grades WHERE grade < 80);