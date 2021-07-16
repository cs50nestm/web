-- people
CREATE TABLE people (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

-- courses
CREATE TABLE courses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT NOT NULL,
  title TEXT NOT NULL
);

-- students
CREATE TABLE students (
  person_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL
);

-- instructors
CREATE TABLE instructors (
  person_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL
);
