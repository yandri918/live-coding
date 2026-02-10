import streamlit as st
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="Machine Learning", page_icon="🤖", layout="wide")

st.markdown("# 🤖 Machine Learning Engineering")
st.markdown("### From Scratch Implementation & Pipelines")

tab1, tab2 = st.tabs(["🟢 Custom Transformers", "🔴 Metrics from Scratch"])

with tab1:
    st.header("Build a Custom Transformer")
    st.markdown("Interviewers often ask to implement a custom class compatible with `scikit-learn`.")
    st.markdown("**Task**: Create a `OutlierRemover` transformer that removes rows where a specific column is > `current_mean + 3*std`.")
    
    code = st.text_area("Implementation:", """
from sklearn.base import BaseEstimator, TransformerMixin

class OutlierRemover(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column
        self.upper_bound = None
        
    def fit(self, X, y=None):
        # Calculate stats
        return self
        
    def transform(self, X):
        # Filter data
        return X
    """)
    
    if st.button("Test Transformer", key="ml_trans"):
        try:
            # Mock test
            df = pd.DataFrame({'val': [1, 2, 3, 100, 2, 3]}) # 100 is outlier
            st.write("Original Data:", df)
            
            # Safe exec
            local_vars = {'BaseEstimator': BaseEstimator, 'TransformerMixin': TransformerMixin, 'pd': pd, 'np': np}
            exec(code, {}, local_vars)
            OutlierRemover = local_vars.get('OutlierRemover')
            
            remover = OutlierRemover(column='val')
            res = remover.fit(df).transform(df)
            
            st.write("Transformed Data:", res)
            if len(res) < len(df):
                st.success("Outlier removed!")
            else:
                st.warning("No rows removed. Check logic.")
        except Exception as e:
            st.error(f"Error: {e}")

with tab2:
    st.header("Metrics from Scratch")
    st.markdown("**Task**: Implement **Log Loss** (Binary Cross Entropy) without using `sklearn`.")
    
    st.latex(r"LogLoss = - \frac{1}{N} \sum_{i=1}^{N} [y_i \log(p_i) + (1-y_i) \log(1-p_i)]")
    
    code_metric = st.text_area("Python Implementation:", """
import numpy as np

def log_loss(y_true, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    # Finish the math
    return 0
    """)
    
    if st.button("Test Metric", key="ml_metric"):
        y_true = np.array([1, 0, 1, 1])
        y_pred = np.array([0.9, 0.1, 0.8, 0.4])
        
        try:
            local_vars = {'np': np}
            exec(code_metric, {}, local_vars)
            user_func = local_vars.get('log_loss')
            
            score = user_func(y_true, y_pred)
            st.write(f"Your Result: {score}")
            st.write(f"Expected: {0.1738}") # Approx
        except Exception as e:
            st.error(f"Error: {e}")
