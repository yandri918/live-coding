import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Pandas Mastery", page_icon="🐼", layout="wide")

st.markdown("# 🐼 Pandas Mastery")
st.markdown("### Data Manipulation & Cleaning Challenges")

# Helper to compare dataframes
def check_dataframe(user_df, expected_df):
    try:
        pd.testing.assert_frame_equal(user_df, expected_df)
        st.success("Correct! DataFrames match.")
        st.balloons()
    except AssertionError as e:
        st.error(f"Mismatch: {e}")
    except Exception as e:
        st.error(f"Error: {e}")

tab1, tab2, tab3 = st.tabs(["🟢 Beginner", "🟡 Intermediate", "🔴 Advanced"])

with tab1:
    st.header("Beginner: Filtering & Selection")
    
    # Sample Data
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Los Angeles', 'New York', 'Chicago'],
        'salary': [70000, 80000, 120000, 90000]
    }
    df = pd.DataFrame(data)
    
    st.markdown("#### Scenario: Employee Filtering")
    st.markdown("Given the dataframe `df`, filter for employees who live in **'New York'** AND identify who has a salary > **100,000**.")
    st.dataframe(df)
    
    user_code = st.text_area("Your Code (assume `df` is loaded):", value="result = df[...]")
    
    if st.button("Run Solution", key="pd_beg_1"):
        try:
            # Safe exec env
            local_vars = {'df': df.copy(), 'pd': pd}
            exec(user_code, {}, local_vars)
            result = local_vars.get('result')
            
            # Expected
            expected = df[(df['city'] == 'New York') & (df['salary'] > 100000)]
            
            if result is not None:
                st.dataframe(result)
                check_dataframe(result, expected)
            else:
                st.error("Variable 'result' not found.")
        except Exception as e:
            st.error(f"Execution Error: {e}")

with tab2:
    st.header("Intermediate: GroupBy & Aggregation")
    st.markdown("#### Scenario: Department Stats")
    
    # More complex data
    dates = pd.date_range('20230101', periods=6)
    df2 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    df2['Category'] = ['A', 'B', 'A', 'B', 'A', 'C']
    
    st.dataframe(df2.head())
    st.markdown("Calculate the **mean** and **sum** of column 'A' for each 'Category'.")
    
    with st.expander("💡 Solution Hint"):
        st.code("df.groupby('Category')['A'].agg(['mean', 'sum'])")

with tab3:
    st.header("Advanced: Windows & Transformations")
    st.markdown("#### Scenario: Rolling Averages & Rank")
    
    st.markdown("Calculate the 3-day rolling average of column 'B', sorting by date first.")
    
    with st.expander("💡 Solution Hint"):
        st.code("df.sort_index()['B'].rolling(window=3).mean()")
