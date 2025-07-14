import mysql.connector
from faker import Faker
import random

# ✅ Step 1: Connect WITHOUT database to create one
init_conn = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="3T8D8cjPqdd2sCi.root",
    password="kreDkHwCv0qYVB6G",
    port=4000
)
init_cursor = init_conn.cursor()
init_cursor.execute("CREATE DATABASE IF NOT EXISTS Students_project")
init_cursor.close()
init_conn.close()

# ✅ Step 2: Connect to the database
conn = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="3T8D8cjPqdd2sCi.root",
    password="kreDkHwCv0qYVB6G",
    port=4000,
    database="Students_project"
)
cursor = conn.cursor()
faker = Faker()

# ✅ Step 3: Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_records (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    student_age INT,
    student_gender VARCHAR(10),
    student_email VARCHAR(100),
    student_phone BIGINT,
    enrollment_year INT,
    course_batch VARCHAR(10),
    student_city VARCHAR(50),
    graduation_year INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS programming_skills (
    student_id INT,
    language VARCHAR(50),
    problems_solved INT,
    assessments_completed INT,
    mini_projects INT,
    certifications_earned INT,
    latest_project_score FLOAT,
    FOREIGN KEY (student_id) REFERENCES student_records(student_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS soft_skills (
    soft_skill_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    communication INT,
    teamwork INT,
    presentation INT,
    leadership INT,
    critical_thinking INT,
    interpersonal_skills INT,
    FOREIGN KEY (student_id) REFERENCES student_records(student_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS placements (
    placement_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    mock_interview_score INT,
    internships_completed INT,
    placement_status VARCHAR(20),
    company_name VARCHAR(100),
    placement_package FLOAT,
    interview_rounds_cleared INT,
    placement_date DATE,
    FOREIGN KEY (student_id) REFERENCES student_records(student_id)
)
""")

# ✅ Step 4: Insert 500 fake students
students = []
for sid in range(1, 501):
    name = faker.name()
    age = random.randint(18, 25)
    gender = random.choice(['Male', 'Female'])
    email = faker.email()
    phone = int(faker.msisdn()[0:10])
    enroll = random.randint(2019, 2023)
    batch = random.choice(['A1', 'B2', 'C3', 'D4'])
    city = faker.city()
    grad = enroll + 4
    students.append((sid, name, age, gender, email, phone, enroll, batch, city, grad))

cursor.executemany("""
INSERT INTO student_records (
    student_id, student_name, student_age, student_gender, student_email,
    student_phone, enrollment_year, course_batch, student_city, graduation_year
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", students)
print("✅ Inserted 500 students into student_records.")

# ✅ Insert into programming_skills
prog_data = []
for s in students:
    sid = s[0]
    lang = random.choice(['Python', 'Java', 'C++'])
    solved = random.randint(10, 300)
    assess = random.randint(5, 20)
    mini = random.randint(0, 5)
    cert = random.randint(0, 5)
    score = round(random.uniform(40, 100), 2)
    prog_data.append((sid, lang, solved, assess, mini, cert, score))

cursor.executemany("""
INSERT INTO programming_skills (
    student_id, language, problems_solved, assessments_completed,
    mini_projects, certifications_earned, latest_project_score
) VALUES (%s, %s, %s, %s, %s, %s, %s)
""", prog_data)
print("✅ Inserted programming_skills.")

# ✅ Insert into soft_skills
soft_data = []
for s in students:
    sid = s[0]
    soft_data.append((
        sid,
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10)
    ))

cursor.executemany("""
INSERT INTO soft_skills (
    student_id, communication, teamwork, presentation,
    leadership, critical_thinking, interpersonal_skills
) VALUES (%s, %s, %s, %s, %s, %s, %s)
""", soft_data)
print("✅ Inserted soft_skills.")

# ✅ Insert into placements
placement_data = []
for s in students:
    sid = s[0]
    status = random.choice(['Placed', 'Not Placed'])
    company = faker.company() if status == 'Placed' else None
    package = round(random.uniform(3.0, 15.0), 2) if status == 'Placed' else None
    rounds = random.randint(1, 5) if status == 'Placed' else 0
    date = faker.date_between(start_date='-2y', end_date='today') if status == 'Placed' else None
    placement_data.append((
        sid,
        random.randint(40, 100),
        random.randint(0, 3),
        status,
        company,
        package,
        rounds,
        date
    ))

cursor.executemany("""
INSERT INTO placements (
    student_id, mock_interview_score, internships_completed,
    placement_status, company_name, placement_package,
    interview_rounds_cleared, placement_date
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""", placement_data)
print("✅ Inserted placements.")

# ✅ Commit and Close
conn.commit()
cursor.close()
conn.close()
print("🎉 All data inserted and connection closed.")







