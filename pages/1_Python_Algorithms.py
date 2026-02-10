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
    """
    try:
        # Dangerous in production, okay for local protected demo
        # exec(user_code) 
        st.success("Code executed successfully! All test cases passed. (Simulation)")
        st.balloons()
    except Exception as e:
        st.error(f"Error: {e}")

# BEGINNER
with tab1:
    st.header("🟢 Beginner: Arrays & Hashing")
    st.markdown("**Focus**: Mastering Hash Maps (Dictionaries) for O(1) lookups.")
    
    # Problem 1: Two Sum
    with st.expander("📝 Problem 1: Two Sum (LeetCode #1)", expanded=True):
        st.markdown("""
        **Description**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
        **Constraints**: exactly one solution.
        
        **Example**:
        ```python
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        ```
        """)
        
        code1 = st.text_area("Your Solution:", height=150, key="code_beg_1", value="""def twoSum(nums, target):
    pass
""")
        if st.button("Run Code", key="btn_beg_1"):
            check_solution(code1, [])
            
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach 1: Brute Force**
        - Loop through each element `x` and find if there is another value that equals to `target - x`.
        - **Time**: $O(n^2)$ | **Space**: $O(1)$
        
        **Approach 2: One-pass Hash Map (Optimal)**
        - We iterate through the array once. For each element `n`, we check if `target - n` exists in our hash map.
        - If it does, we found our pair. If not, we store `n` and its index in the map.
        - **Time**: $O(n)$ | **Space**: $O(n)$
        """)
        
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

    st.markdown("---")
    
    # Problem 2: Valid Anagram
    with st.expander("📝 Problem 2: Valid Anagram (LeetCode #242)"):
        st.markdown("""
        **Description**: Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
        
        **Example**:
        ```python
        Input: s = "anagram", t = "nagaram"
        Output: true
        ```
        """)
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach**: Count Character Frequencies
        - Use a hash map (or fixed-size array of 26 integers) to count occurrences of each char in `s`.
        - Decrement counts for `t`. If all counts are zero, it's an anagram.
        - **Time**: $O(n)$ | **Space**: $O(1)$ (since only 26 lowercase chars)
        """)
        st.code("""
def isAnagram(s, t):
    if len(s) != len(t):
        return False
        
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1
        
    return countS == countT
        """, language="python")

    st.markdown("---")

    # Problem 3: Contains Duplicate
    with st.expander("📝 Problem 3: Contains Duplicate (LeetCode #217)"):
        st.markdown("""
        **Description**: Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.
        """)
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach**: Hash Set
        - Iterate through the array, checking if the number is already in a `set`.
        - Sets provide $O(1)$ average time complexity for lookups.
        - **Time**: $O(n)$ | **Space**: $O(n)$
        """)
        st.code("""
def containsDuplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
        """, language="python")

# INTERMEDIATE
with tab2:
    st.header("🟡 Intermediate: Two Pointers & Sliding Window")
    
    # Problem 1: Valid Parentheses (Stack)
    with st.expander("📝 Problem 1: Valid Parentheses (LeetCode #20)", expanded=True):
        st.markdown("""
        **Description**: Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        
        **Example**:
        ```python
        Input: s = "()[]{}"
        Output: true
        ```
        """)
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach**: Stack
        - Use a stack to keep track of opening brackets.
        - When encountering a closing bracket, check if it matches the top of the stack.
        - **Time**: $O(n)$ | **Space**: $O(n)$
        """)
        st.code("""
def isValid(s):
    stack = []
    closeToOpen = { ")": "(", "]": "[", "}": "{" }
    
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
    return True if not stack else False
        """, language="python")
        
    st.markdown("---")

    # Problem 2: Container With Most Water
    with st.expander("📝 Problem 2: Container With Most Water (LeetCode #11)"):
        st.markdown("Find two lines that together with the x-axis form a container, such that the container contains the most water.")
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach**: Two Pointers
        - Start with pointers at the beginning (`l`) and end (`r`) of the array.
        - Calculate area. To potentially maximize area, move the pointer pointing to the *shorter* line inward.
        - **Time**: $O(n)$ | **Space**: $O(1)$
        """)
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

    st.markdown("---")

    # Problem 3: Longest Substring Without Repeating Characters
    with st.expander("📝 Problem 3: Longest Substring Without Repeating Characters (LeetCode #3)"):
        st.markdown("""
        **Description**: Given a string `s`, find the length of the longest substring without repeating characters.
        
        **Example**:
        ```python
        Input: s = "abcabcbb"
        Output: 3  # "abc"
        ```
        """)
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach**: Sliding Window
        - Use a `set` to store characters in the current window.
        - If we see a duplicate, remove characters from the left (`l`) until the duplicate is gone.
        - **Time**: $O(n)$ | **Space**: $O(n)$
        """)
        st.code("""
def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
        """, language="python")

# ADVANCED
with tab3:
    st.header("🔴 Advanced: DP & Graphs")
    
    # Problem 1: Number of Islands
    with st.expander("📝 Problem 1: Number of Islands (LeetCode #200)", expanded=True):
        st.markdown("""
        **Description**: Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.
        """)
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach**: Breadth-First Search (BFS) or DFS
        - Iterate through every cell. If it's a '1' and not visited, trigger a BFS/DFS to mark the entire island as visited.
        - Increment island count.
        - **Time**: $O(m \times n)$ | **Space**: $O(m \times n)$
        """)
        st.code("""
import collections

def numIslands(grid):
    if not grid: return 0
    
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0
    
    def bfs(r, c):
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))
        
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            for dr, dc in directions:
                r_new, c_new = row + dr, col + dc
                if (r_new in range(rows) and 
                    c_new in range(cols) and 
                    grid[r_new][c_new] == "1" and 
                    (r_new, c_new) not in visit):
                    q.append((r_new, c_new))
                    visit.add((r_new, c_new))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands
        """, language="python")

    st.markdown("---")

    # Problem 2: Climbing Stairs (DP)
    with st.expander("📝 Problem 2: Climbing Stairs (LeetCode #70)"):
        st.markdown("""
        **Description**: You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. How many distinct ways can you climb to the top?
        """)
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach**: Dynamic Programming (Bottom-Up)
        - This is essentially the Fibonacci sequence.
        - `ways(n) = ways(n-1) + ways(n-2)`
        - **Time**: $O(n)$ | **Space**: $O(1)$
        """)
        st.code("""
def climbStairs(n):
    one, two = 1, 1
    
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
        
    return one
        """, language="python")

    st.markdown("---")
    
    # Problem 3: Merge K Sorted Lists
    with st.expander("📝 Problem 3: Merge K Sorted Lists (LeetCode #23)"):
        st.markdown("Merge `k` sorted linked lists and return it as one sorted list.")
        st.markdown("### 💡 Comprehensive Solution")
        st.markdown("""
        **Approach**: Min-Heap
        - Push the first node of each list into a Min-Heap.
        - Pop the smallest node, add to result, and push its next node into the heap.
        - **Time**: $O(N \log k)$ where N is total nodes.
        """)
        st.code("""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

def mergeKLists(lists):
    minHeap = []
    
    # Add first node of each list to heap
    for i, l in enumerate(lists):
        if l:
            minHeap.append((l.val, i, l))
    heapq.heapify(minHeap)
    
    dummy = ListNode(0)
    curr = dummy
    
    while minHeap:
        val, i, node = heapq.heappop(minHeap)
        curr.next = node
        curr = node
        
        if node.next:
            heapq.heappush(minHeap, (node.next.val, i, node.next))
            
    return dummy.next
        """, language="python")


