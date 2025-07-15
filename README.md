# Student-Assessment
Guvi Student Assessment
# 🧠 Student Database Management with MySQL and Faker

This project demonstrates how to create a **student performance tracking system** using **Python**, **MySQL**, and **Faker**. It auto-generates realistic data for 500 students and organizes it across multiple normalized tables: academic records, programming skills, soft skills, and placement records.



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


















***************************************************************************************************************************************************************
STUDENT PROJECT
***************************************************************************************************************************************************

Connects to a TiDB Cloud MySQL database

Creates a database (Students_project)

Creates 4 tables:

student_records

programming_skills

soft_skills

placements

Generates 500 fake students using the Faker library

Inserts the data into the 4 tables

Commits the data and closes the connection




🔹 Step 1: Connect WITHOUT database to create one
python
Copy
Edit
init_conn = mysql.connector.connect(...)
init_cursor.execute("CREATE DATABASE IF NOT EXISTS Students_project")
This connects to the MySQL server (without specifying a database).

It runs an SQL command to create the database only if it doesn't already exist.

Then, it closes the initial connection.



🔹 Step 2: Connect to the newly created database
python
Copy
Edit
conn = mysql.connector.connect(..., database="Students_project")
cursor = conn.cursor()
Now, you connect specifically to the Students_project database.

You create a cursor (cursor) to run SQL commands on this database.



🔹 Step 3: Create Tables
You define the structure of each table.

📄 Table 1: student_records
Stores basic student info:

Column	Type	Notes
student_id	INT	Primary Key
student_name	VARCHAR	Student’s full name
student_age	INT	Age between 18 and 25
student_gender	VARCHAR	'Male' or 'Female'
student_email	VARCHAR	Fake email
student_phone	BIGINT	10-digit phone number
enrollment_year	INT	From 2019 to 2023
course_batch	VARCHAR	Random batch like 'A1'
student_city	VARCHAR	Random city
graduation_year	INT	Enrollment + 4



📄 Table 2: programming_skills
Each student has one row here with their coding performance:

Column	Type	Notes
student_id	INT	Foreign key → student_records
language	VARCHAR	Random: Python, Java, C++
problems_solved	INT	Random value (10–300)
assessments_completed	INT	Random value (5–20)
mini_projects	INT	0–5
certifications_earned	INT	0–5
latest_project_score	FLOAT	40.00–100.00




📄 Table 3: soft_skills
Each student gets a soft skill rating from 1 to 10:

Column	Type	Notes
soft_skill_id	INT	Auto-increment, Primary Key
student_id	INT	Foreign key
communication	INT	Rating 1–10
teamwork	INT	Rating 1–10
presentation	INT	Rating 1–10
leadership	INT	Rating 1–10
critical_thinking	INT	Rating 1–10
interpersonal_skills	INT	Rating 1–10

📄 Table 4: placements
Placement data for each student:

Column	Type	Notes
placement_id	INT	Auto-increment, Primary Key
student_id	INT	Foreign key
mock_interview_score	INT	40–100
internships_completed	INT	0–3
placement_status	VARCHAR	'Placed' or 'Not Placed'
company_name	VARCHAR	Only if 'Placed'
placement_package	FLOAT	Only if 'Placed'
interview_rounds_cleared	INT	1–5 or 0 if not placed
placement_date	DATE	Random date in past 2 years

🔹 Step 4: Insert 500 Fake Students
python
Copy
Edit
for sid in range(1, 501):
    name = faker.name()
    age = random.randint(18, 25)
    ...
Loop generates 500 students with unique student_id from 1 to 500.

faker generates fake name, email, phone, city.

Each student is stored in a list students[].

Then the list is inserted using executemany() into student_records.

🔹 Step 5: Insert Programming Skills
python
Copy
Edit
for s in students:
    sid = s[0]
    lang = random.choice(['Python', 'Java', 'C++'])
    ...
For each student, randomly assign:

A language

Problem-solving metrics

Stored in prog_data[] and inserted into programming_skills.

🔹 Step 6: Insert Soft Skills
python
Copy
Edit
for s in students:
    sid = s[0]
    ...
Each skill (like communication, leadership) is randomly rated (1–10).

Inserted into soft_skills table.

🔹 Step 7: Insert Placement Data
python
Copy
Edit
for s in students:
    sid = s[0]
    status = random.choice(['Placed', 'Not Placed'])
Only if the student is "Placed":

Assign company name, package, rounds, date

If not placed, set those fields as None or 0

Inserted into placements table



✅ Final Step: Commit & Close
python
Copy
Edit
conn.commit()
cursor.close()
conn.close()
commit() saves all the changes

Connection is safely closed

🧠 Summary of Tables with Dependencies:
lua
Copy
Edit
student_records  <-- main table
    |
    |-- programming_skills (1:1)
    |-- soft_skills (1:1)
    |-- placements (1:1)
Each student has:

1 programming_skills record

1 soft_skills record

1 placements record



*******************************************************************************************************************************************
Stdent Assessment -Streamlit
************************************************************************************************************************************************






🔧 1. Database Connection Setup
You’ve defined a function to connect to the TiDB MySQL-compatible database:

python
Copy
Edit
def get_connection():
    return mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="3T8D8cjPqdd2sCi.root",
        password="kreDkHwCv0qYVB6G",
        database="Students_project",
        port=4000
    )
🔍 What it does:
This function uses the mysql.connector library to connect to your remote MySQL database.

Whenever you want to run a query, call this function to get a fresh connection.

Security Note: Never expose passwords or credentials in public code. Use .env files or Streamlit secrets.

📥 2. Query Execution Function
python
Copy
Edit
def execute_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df
🔍 What it does:
Accepts an SQL query as input.

Calls get_connection() to get a database connection.

Uses pandas.read_sql() to run the query and return a DataFrame (df) which is easier to display and manipulate in Streamlit.

Finally, it closes the connection.

⚠️ This function doesn’t currently support parameters like placeholders (e.g., %s). But one version of your code below does.

🌐 3. Sidebar Language Filter + Data Display
python
Copy
Edit
selected_language = st.sidebar.selectbox(
    "Select Programming Language",
    options=["Python", "Java", "C++"]
)
🔍 What it does:
Displays a dropdown menu on the sidebar to choose a programming language.

Based on this selection, it executes a query with a filter:

python
Copy
Edit
query = """
SELECT ...
FROM student_records sr
JOIN programming_skills ps ON sr.student_id = ps.student_id
WHERE ps.language = %s
"""

df = pd.read_sql(query, conn, params=(selected_language,))
✅ This version uses parameterized queries, which is safer and prevents SQL injection attacks.

📊 4. Displaying the Filtered Student Data
python
Copy
Edit
st.subheader(f"Students with {selected_language} as Programming Language")
st.dataframe(df)
🔍 What it does:
Displays a sub-header with the selected language.

Shows the filtered students who know that language using st.dataframe(df).

📑 5. Predefined Top 10 SQL Queries
You defined a dictionary with 10 meaningful and powerful SQL reports, like:

All Students

Python Programmers

Top 10 Problem Solvers

Students with Soft Skills > 8

Placed Students with Packages > 10 LPA

python
Copy
Edit
queries = {
    "1. View All Students": "SELECT * FROM student_records;",
    ...
    "10. Students from City 'Chennai' Studying Java": """
        SELECT sr.student_name, sr.student_city, ps.language
        FROM student_records sr
        JOIN programming_skills ps ON sr.student_id = ps.student_id
        WHERE sr.student_city = 'Chennai' AND ps.language = 'Java';
    """
}
✅ Benefits:
Makes your dashboard modular and dynamic.

Users can choose any report and see it instantly.

🧑‍💻 6. Query Selection UI (Dynamic Explorer)
python
Copy
Edit
selected_query = st.selectbox("📌 Choose a Report:", list(queries.keys()))
Displays all the keys (report names) from your queries dictionary as dropdown options.

python
Copy
Edit
if st.button("Run Query"):
    with st.spinner("Executing..."):
        df = execute_query(queries[selected_query])
        st.success("✅ Query executed successfully!")
        st.dataframe(df)
🔍 What it does:
Once the user clicks Run Query, the selected SQL is run.

Shows a spinner during execution, then displays a success message.

Finally, shows the result in a nice scrollable table.

🧠 Summary of Key Concepts
Section	Purpose
get_connection()	Opens a connection to your database
execute_query()	Runs an SQL and returns a DataFrame
st.sidebar.selectbox()	Filters results dynamically (e.g., by language)
queries{}	Collection of useful SQL reports
st.selectbox()	Lets users select a query from the list
st.dataframe()	Displays SQL results in a web table

💡 Suggestions for Improvement
Modularize the code further:

Put DB connection and query functions in a separate module (db_utils.py).

Place all UI in main.py.

Use .env or st.secrets:

Store your DB credentials securely.

Add filters by city, year, placement status, etc.

Add charts:

Use st.bar_chart(df) or altair for visualizations (e.g., placement by city).

Pagination:

Large result sets can be paginated using custom logic or a plugin.
