import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(page_title="SQL Integration", page_icon="💾", layout="wide")

st.markdown("# 💾 SQL Integration with DuckDB")
st.markdown("### Live SQL Query Execution")

# Setup Sandbox Database
@st.cache_resource
def get_connection():
    con = duckdb.connect(database=':memory:')
    # Create sample tables
    con.execute("CREATE TABLE employees (id INTEGER, name VARCHAR, department VARCHAR, salary INTEGER)")
    con.execute("INSERT INTO employees VALUES (1, 'Alice', 'HR', 60000), (2, 'Bob', 'Engineering', 120000), (3, 'Charlie', 'Engineering', 130000), (4, 'David', 'HR', 65000), (5, 'Eve', 'Marketing', 90000)")
    
    con.execute("CREATE TABLE sales (id INTEGER, employee_id INTEGER, amount INTEGER, date DATE)")
    con.execute("INSERT INTO sales VALUES (1, 2, 500, '2023-01-01'), (2, 2, 700, '2023-01-02'), (3, 3, 200, '2023-01-01'), (4, 5, 1000, '2023-01-05')")
    return con

con = get_connection()

st.sidebar.markdown("### Schema")
st.sidebar.text("Table: employees\n- id, name, department, salary")
st.sidebar.text("Table: sales\n- id, employee_id, amount, date")

tab1, tab2, tab3 = st.tabs(["🟢 Basic Selects", "🟡 Joins & Aggregates", "🔴 Advanced Window Functions"])

with tab1:
    st.header("Select & Where")
    st.markdown("Find all employees in the **'Engineering'** department with salary > **125000**.")
    
    query = st.text_area("SQL Query:", "SELECT * FROM employees WHERE ...")
    if st.button("Run Query", key="sql_1"):
        try:
            result = con.execute(query).df()
            st.dataframe(result)
        except Exception as e:
            st.error(f"SQL Error: {e}")

with tab2:
    st.header("Joins & Aggregates")
    st.markdown("Calculate **total sales amount** per employee name.")
    
    with st.expander("💡 Solution"):
        st.code("""
SELECT e.name, SUM(s.amount) as total_sales
FROM employees e
JOIN sales s ON e.id = s.employee_id
GROUP BY e.name
        """, language="sql")

with tab3:
    st.header("Window Functions")
    st.markdown("#### Rank Salary per Department")
    st.markdown("Use `RANK()` or `DENSE_RANK()` to rank employees by salary within their department.")
    
    query_adv = st.text_area("Advanced SQL:", """
SELECT 
    name, 
    department, 
    salary,
    RANK() OVER (PARTITION BY ... ORDER BY ...) as rank
FROM employees
    """)
    if st.button("Run Advanced Query", key="sql_adv"):
        try:
            result = con.execute(query_adv).df()
            st.dataframe(result)
        except Exception as e:
            st.error(f"SQL Error: {e}")
