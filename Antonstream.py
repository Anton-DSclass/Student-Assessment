

# DB connection function
def get_connection():
    return mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="3T8D8cjPqdd2sCi.root",
        password="kreDkHwCv0qYVB6G",
        database="Students_project",
        port=4000  # optional
    )

# Query function
def execute_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

import streamlit as st


st.title("PLACEMENT ELIGIBILITY")



import mysql.connector
import pandas as pd
import streamlit as st

# Streamlit UI
st.title("📊 Programming Language - Student Details")

# Sidebar for language filter
st.sidebar.header("Filter")
selected_language = st.sidebar.selectbox(
    "Select Programming Language",
    options=["Python", "Java", "C++"]
)

# MySQL connection
conn = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="3T8D8cjPqdd2sCi.root",
    password="kreDkHwCv0qYVB6G",
    port=4000,
    database="Students_project"
)

query = f"""
SELECT sr.student_id, sr.student_name, sr.student_age, sr.student_gender,
       sr.student_email, ps.language, ps.problems_solved, ps.latest_project_score
FROM student_records sr
JOIN programming_skills ps ON sr.student_id = ps.student_id
WHERE ps.language = %s
"""

df = pd.read_sql(query, conn, params=(selected_language,))
conn.close()

# Show filtered data
st.subheader(f"Students with {selected_language} as Programming Language")
st.dataframe(df)




# top 10 query

queries = {
    "1. View All Students": "SELECT * FROM student_records;",

    "2. Python Programmers Only": """
        SELECT sr.student_id, sr.student_name, ps.language
        FROM student_records sr
        JOIN programming_skills ps ON sr.student_id = ps.student_id
        WHERE ps.language = 'Python';
    """,

    "3. Top 10 by Problem Solving": """
        SELECT sr.student_name, ps.language, ps.problems_solved
        FROM student_records sr
        JOIN programming_skills ps ON sr.student_id = ps.student_id
        ORDER BY ps.problems_solved DESC
        LIMIT 10;
    """,

    "4. Students with Internship Experience": """
        SELECT sr.student_name, p.internships_completed
        FROM student_records sr
        JOIN placements p ON sr.student_id = p.student_id
        WHERE p.internships_completed > 0;
    """,

    "5. Placed Students with Packages > 10 LPA": """
        SELECT sr.student_name, p.company_name, p.placement_package
        FROM student_records sr
        JOIN placements p ON sr.student_id = p.student_id
        WHERE p.placement_status = 'Placed' AND p.placement_package > 10;
    """,

    "6. Students Good at Soft Skills (score > 8 in all)": """
        SELECT sr.student_name
        FROM student_records sr
        JOIN soft_skills ss ON sr.student_id = ss.student_id
        WHERE ss.communication > 8 AND ss.teamwork > 8 AND ss.presentation > 8 AND 
              ss.leadership > 8 AND ss.critical_thinking > 8 AND ss.interpersonal_skills > 8;
    """,

    "7. Final Year Students (Graduation 2023)": """
        SELECT student_name, graduation_year
        FROM student_records
        WHERE graduation_year = 2023;
    """,

    "8. Students Cleared > 3 Interview Rounds": """
        SELECT sr.student_name, p.interview_rounds_cleared
        FROM student_records sr
        JOIN placements p ON sr.student_id = p.student_id
        WHERE p.interview_rounds_cleared > 3;
    """,

    "9. Students with Project Score < 50": """
        SELECT sr.student_name, ps.language, ps.latest_project_score
        FROM student_records sr
        JOIN programming_skills ps ON sr.student_id = ps.student_id
        WHERE ps.latest_project_score < 50;
    """,

    "10. Students from City 'Chennai' Studying Java": """
        SELECT sr.student_name, sr.student_city, ps.language
        FROM student_records sr
        JOIN programming_skills ps ON sr.student_id = ps.student_id
        WHERE sr.student_city = 'Chennai' AND ps.language = 'Java';
    """
}


streamlit
# Connection
def get_connection():
    return mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="3T8D8cjPqdd2sCi.root",
        password="kreDkHwCv0qYVB6G",
        port=4000,
        database="Students_project"
    )

# Execute Query
def execute_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# --- UI ---
st.title("🎓 Student Data Explorer")

# Dropdown
selected_query = st.selectbox("📌 Choose a Report:", list(queries.keys()))

# Button to Run Query
if st.button("Run Query"):
    with st.spinner("Executing..."):
        df = execute_query(queries[selected_query])
        st.success("✅ Query executed successfully!")
        st.dataframe(df)
