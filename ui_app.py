
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import os

st.set_page_config(layout="wide")
st.title("🚀 TRSIM UAV | Unified Trust & ML Simulator")

# Session states
if "show_attack_graph" not in st.session_state:
    st.session_state.show_attack_graph = False
if "show_ml_graph" not in st.session_state:
    st.session_state.show_ml_graph = False

# Load data
DATA_PATH = "data/SwarmCoordinationData.csv"
try:
    df = pd.read_csv(DATA_PATH)
except:
    st.warning("⚠️ Please place SwarmCoordinationData.csv in the /data folder to enable graphs.")
    df = pd.DataFrame()

# Sidebar panels
with st.sidebar:
    st.header("🛩 Drone Control")
    st.info("Total drones: 4")
    if st.button("Show Swarm Network"):
        st.session_state.show_attack_graph = False
        st.session_state.show_ml_graph = False

    st.markdown("---")
    st.header("⚔️ Apply Attack")
    attack_type = st.radio("Select Attack", ["None", "CNA", "DMA", "MITM", "SA"])
    target_drone = st.selectbox("Target Drone", ["Drone1", "Drone2", "Drone3", "Drone4"])
    if st.button("Apply Attack"):
        st.success(f"{attack_type} applied to {target_drone}")

    st.markdown("---")
    st.header("📊 Attack Graph Preview")
    if st.button("Show Attack Coordination Graph"):
        st.session_state.show_attack_graph = True
        st.session_state.show_ml_graph = False

    st.markdown("---")
    st.header("🧠 ML Model Selector")
    ml_model = st.radio("Select ML Model", ["Random Forest", "SVM", "CNN"])
    if st.button("Show ML Prediction Graph"):
        st.session_state.show_ml_graph = True
        st.session_state.show_attack_graph = False

# Trust table
trust_data = pd.DataFrame({
    "name": ["Drone1", "Drone2", "Drone3", "Drone4"],
    "cluster": ["Cluster A", "Cluster A", "Cluster B", "Cluster A"],
    "trust_score": [0.5 if attack_type != "None" and target_drone == "Drone1" else 1.0]*4,
    "status": ["Under Attack" if attack_type != "None" and target_drone == "Drone1" else "Trustworthy"]*4,
    "latency": [0.05]*4,
    "packet_loss": [0.01]*4,
    "battery": [100]*4
})
st.subheader("📋 Trust & Prediction Status")
st.dataframe(trust_data)

# Swarm graph
st.subheader("🕸 Swarm Network")
G = nx.Graph()
for i in range(4):
    G.add_node(f"Drone{i+1}")
G.add_edges_from([(f"Drone{i}", f"Drone{i+1}") for i in range(1,4)])
colors = ["red" if drone==target_drone and attack_type!="None" else "green" for drone in trust_data.name]
pos = nx.spring_layout(G)
fig1, ax1 = plt.subplots()
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1000, ax=ax1)
st.pyplot(fig1)

# attack preview graph
if st.session_state.show_attack_graph and not df.empty:
    st.subheader(f"📊 Coordination Rate Predictions - {attack_type} Attack")
    fig2, ax2 = plt.subplots()
    x = df["Iteration"]
    y_rf = df["cna_rf"]
    y_svm = df["cna_svm"]
    y_cnn = df["cna_cnn"]
    ax2.plot(x, y_rf, label="Random Forest")
    ax2.plot(x, y_svm, label="SVM")
    ax2.plot(x, y_cnn, label="CNN")
    ax2.legend()
    st.pyplot(fig2)

# ml preview graph
if st.session_state.show_ml_graph and not df.empty:
    st.subheader(f"🤖 ML Model Prediction - {ml_model}")
    fig3, ax3 = plt.subplots()
    x = df["Iteration"]
    if ml_model=="Random Forest":
        y = df["cna_rf"]
    elif ml_model=="SVM":
        y = df["cna_svm"]
    else:
        y = df["cna_cnn"]
    ax3.plot(x,y,label=ml_model)
    ax3.legend()
    st.pyplot(fig3)

st.info("✅ Ready to test!")
