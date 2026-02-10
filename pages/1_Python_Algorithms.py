import streamlit as st
import time

st.set_page_config(page_title="Python Algorithms", page_icon="🐍", layout="wide")

st.markdown("# 🐍 Python Algorithms & Data Structures")
st.markdown("### Master Common Interview Patterns")

# Tabs for Difficulty Levels
tab1, tab2, tab3 = st.tabs(["🟢 Beginner", "🟡 Intermediate", "🔴 Advanced"])

def check_solution(user_code, test_cases):
    """
    A simple helper to simulate running user code against test cases.
    In a real app, use `exec` carefully or a sandbox.
    Here we just show a success message for demo purposes.
    """
    try:
        # Dangerous in production, okay for local protected demo
        # exec(user_code) 
        st.success("Code executed successfully! All test cases passed. (Simulation)")
        st.balloons()
    except Exception as e:
        st.error(f"Error: {e}")

with tab1:
    st.header("Beginner: Arrays & Hashing")
    st.markdown("**Pattern**: Hash Maps are your best friend for O(n) lookups.")
    
    with st.expander("📝 Problem: Two Sum (LeetCode #1)", expanded=True):
        st.markdown("""
        **Description**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
        
        **Example**:
        ```python
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        ```
        """)
        
        code = st.text_area("Your Solution:", height=200, value="""def twoSum(nums, target):
    # Write your code here
    pass
""")
        if st.button("Run Code", key="btn_two_sum"):
            check_solution(code, [])
            
        with st.expander("💡 View Solution"):
            st.code("""
def twoSum(nums, target):
    prevMap = {}  # val : index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return []
            """, language="python")
            st.markdown("**Time Complexity**: O(n) | **Space Complexity**: O(n)")

    st.markdown("---")
    
    with st.expander("📝 Problem: Valid Anagram (LeetCode #242)"):
        st.markdown("**Description**: Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.")
        st.code("""
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    # ... finish the logic
        """, language="python")

with tab2:
    st.header("Intermediate: Two Pointers & Sliding Window")
    
    with st.expander("📝 Problem: Container With Most Water (LeetCode #11)", expanded=True):
        st.markdown("Find two lines that together with the x-axis form a container, such that the container contains the most water.")
        st.code("""
def maxArea(height):
    l, r = 0, len(height) - 1
    res = 0
    
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
            
    return res
        """, language="python")

with tab3:
    st.header("Advanced: Dynamic Programming & Graphs")
    st.info("Coming soon: Detailed graph traversal (BFS/DFS) and DP patterns.")

