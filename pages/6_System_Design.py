import streamlit as st

st.set_page_config(page_title="ML System Design", page_icon="🏗️", layout="wide")

st.markdown("# 🏗️ Machine Learning System Design")
st.markdown("### Designing Scalable ML Applications")

st.sidebar.markdown("""
**Framework (RIB):**
1. **R**equirements (Business/Tech)
2. **I**nterface (API input/output)
3. **B**uilding Blocks (Data, Model, Online/Offline)
""")

tab1, tab2 = st.tabs(["🟢 Design Pattern: Recommendation", "🔴 Design Pattern: Real-time Fraud"])

with tab1:
    st.header("News Feed Recommendation")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("1. Requirements")
        st.checkbox("Maximize user engagement (Time Spent)")
        st.checkbox("Latency < 200ms")
        st.checkbox("Scale to 100M DAU")
        
        st.subheader("2. Training Data")
        st.markdown("- **User Logs**: Click, Like, Share, Scroll Depth")
        st.markdown("- **Features**: User Demographics, Content Embeddings, Context (Time/Device)")
    
    with col2:
        st.subheader("3. Architecture")
        st.graphviz_chart("""
            digraph {
                rankdir=LR;
                User -> Gateway;
                Gateway -> Retrieval [label="Candidates (1000)"];
                Retrieval -> Ranking [label="LightGBM/NN"];
                Ranking -> ReRanking [label="Diversity/Ads"];
                ReRanking -> User;
                
                LogStore -> FeatureStore;
                FeatureStore -> Training;
                Training -> ModelRegistry;
                ModelRegistry -> Ranking;
            }
        """)

with tab2:
    st.header("Real-time Fraud Detection")
    st.markdown("#### Key Challenge: Feature Freshness")
    
    st.markdown("""
    - **Transaction arrives**: Need decision in < 50ms.
    - **Features**:
        - *Static*: User account age.
        - *Dynamic*: # Multi-window counts (last 1 min, 5 min, 1 hr transaction count).
    """)
    
    st.info("💡 **Interview Tip**: Discuss sliding window aggregation using Flink or Redis.")
