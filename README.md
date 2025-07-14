# Student-Assessment
Guvi Student Assessment
# 🧠 Student Database Management with MySQL and Faker

This project demonstrates how to create a **student performance tracking system** using **Python**, **MySQL**, and **Faker**. It auto-generates realistic data for 500 students and organizes it across multiple normalized tables: academic records, programming skills, soft skills, and placement records.

---

## 📌 Features

- Automatically connects to a TiDB (MySQL-compatible) cloud database.
- Creates a new database `Students_project` if it doesn't already exist.
- Defines 4 interlinked tables with proper relationships:
  - `student_records`
  - `programming_skills`
  - `soft_skills`
  - `placements`
- Inserts **500 fake student records** using the [Faker](https://faker.readthedocs.io/) library.
- Each student has related entries in all other tables, simulating a real-world data model.
- Supports reproducible testing, analytics, and training use cases.

---

## 🧱 Database Schema Overview

### `student_records`

| Column           | Type        | Description                  |
|------------------|-------------|------------------------------|
| student_id       | INT         | Primary key                  |
| student_name     | VARCHAR(100)| Full name                    |
| student_age      | INT         | Age                          |
| student_gender   | VARCHAR(10) | Male / Female                |
| student_email    | VARCHAR(100)| Email address                |
| student_phone    | BIGINT      | Phone number                 |
| enrollment_year  | INT         | Year joined                  |
| course_batch     | VARCHAR(10) | Batch code (A1, B2, etc.)    |
| student_city     | VARCHAR(50) | City                         |
| graduation_year  | INT         | Year of graduation           |

### `programming_skills`

| Column                | Type     |
|------------------------|----------|
| student_id (FK)       | INT      |
| language              | VARCHAR  |
| problems_solved       | INT      |
| assessments_completed | INT      |
| mini_projects         | INT      |
| certifications_earned | INT      |
| latest_project_score  | FLOAT    |

### `soft_skills`

| Column              | Type     |
|----------------------|----------|
| soft_skill_id (PK)  | INT AUTO_INCREMENT |
| student_id (FK)     | INT      |
| communication       | INT (1-10)|
| teamwork            | INT (1-10)|
| presentation        | INT (1-10)|
| leadership          | INT (1-10)|
| critical_thinking   | INT (1-10)|
| interpersonal_skills| INT (1-10)|

### `placements`

| Column                  | Type     |
|--------------------------|----------|
| placement_id (PK)       | INT AUTO_INCREMENT |
| student_id (FK)         | INT      |
| mock_interview_score    | INT      |
| internships_completed   | INT      |
| placement_status        | VARCHAR  |
| company_name            | VARCHAR (Nullable) |
| placement_package       | FLOAT (Nullable)   |
| interview_rounds_cleared| INT      |
| placement_date          | DATE (Nullable)    |

---

## 🚀 How to Run

### ✅ Prerequisites

- Python 3.8+
- MySQL Server or TiDB Cloud
- Required libraries:

```bash
pip install mysql-connector-python faker
