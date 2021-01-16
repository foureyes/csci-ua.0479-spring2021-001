DROP TABLE IF EXISTS student;
CREATE TABLE student(
	netid varchar(20) PRIMARY KEY,
	first varchar(255) NOT NULL,
	last varchar(255) NOT NULL,
	midterm numeric,
	registered timestamptz DEFAULT NOW()
);

INSERT INTO student
	VALUES
		('aa1', 'Alice', 'Awad', 92),
		('aba20', 'Alice', 'Anderson', 70),
		('aca33', 'Alice', 'Alvarez', 70),
		('bb123', 'Bob', 'Beasley', 83),
		('bab456', 'Bob', 'Bernstein', 67),
		('cc78', 'Carol', 'Cavil', 92),
		('dd9', 'Daniel', 'Davidson', 70);
