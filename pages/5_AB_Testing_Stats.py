import streamlit as st
import numpy as np
import scipy.stats as stats
import plotly.graph_objects as go

st.set_page_config(page_title="A/B Testing", page_icon="📊", layout="wide")

st.markdown("# 📊 A/B Testing & Statistics")
st.markdown("### Experimentation Rigor")

tab1, tab2 = st.tabs(["🟢 Hypothesis Testing", "🔴 Sample Size Calculator"])

with tab1:
    st.header("T-Test Simulation")
    st.markdown("Visualizing the difference between Control and Treatment groups.")
    
    col1, col2 = st.columns(2)
    with col1:
        mean_c = st.slider("Control Mean", 1.0, 10.0, 5.0)
        std_c = st.slider("Control Std", 0.1, 5.0, 1.0)
    with col2:
        mean_t = st.slider("Treatment Mean", 1.0, 10.0, 5.5)
        std_t = st.slider("Treatment Std", 0.1, 5.0, 1.0)
        
    n = st.number_input("Sample Size per Group", 100, 10000, 1000)
    
    if st.button("Run Simulation"):
        # Generate data
        c_data = np.random.normal(mean_c, std_c, n)
        t_data = np.random.normal(mean_t, std_t, n)
        
        t_stat, p_val = stats.ttest_ind(c_data, t_data)
        
        st.metric("P-Value", f"{p_val:.4f}", delta=f"{'Significant' if p_val < 0.05 else 'Not Significant'}")
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=c_data, name='Control', opacity=0.7))
        fig.add_trace(go.Histogram(x=t_data, name='Treatment', opacity=0.7))
        fig.update_layout(barmode='overlay', title="Distribution Overlay")
        st.plotly_chart(fig)

with tab2:
    st.header("Effect Size & Power")
    st.markdown("Calculate the minimum sample size required.")
    
    alpha = st.slider("Alpha (Type I Error)", 0.01, 0.10, 0.05)
    power = st.slider("Power (1 - Type II Error)", 0.5, 0.99, 0.80)
    mde = st.number_input("Minimum Detectable Effect (Absolute)", 0.01, 1.0, 0.1)
    
    # Simple approx for binary metric
    p = 0.5
    delta = mde
    if delta > 0:
        n_req = (15.7 * p * (1-p)) / (delta**2) # Very rough approximation rule of thumb
        st.info(f"Approximate Sample Size per Variation: {int(n_req):,}")
        st.markdown("*Note: This is a simplified Evan Miller heuristic for P=0.5.*")
