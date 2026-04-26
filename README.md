# TRSIM UAV ML Simulator

A **Streamlit-based UAV (drone) trust and attack simulation dashboard** that demonstrates how different cyber-attacks can affect trust levels and ML-based predictions in a drone swarm network.

---

## Overview

This project simulates a **multi-drone environment** where:

* Multiple UAVs communicate in a swarm
* Different types of cyber-attacks can be applied
* Trust values are monitored
* Machine Learning model outputs are visualized

⚠️ Note: Current implementation uses **static/demo data** for visualization.

---

## Features

* Interactive **Streamlit dashboard**
* Simulated UAV network graph
* Attack selection:

  * CNA (Communication Network Attack)
  * DMA (Data Manipulation Attack)
  * MITM (Man-in-the-Middle)
  * SA (Spoofing Attack)
* Trust monitoring table
* ML model visualization:

  * Random Forest
  * SVM
  * CNN

---

## Project Structure

```
TRSIM_UAV_ML_Modular_Ready/
│
├── ui_app.py                # Main Streamlit app
├── environment.yml         # Conda environment file
├── README.md               # Project documentation
│
├── data/                   # Dataset files
│   ├── SwarmCoordinationData.csv
│   └── trust_log.csv
│
├── modules/ (if applicable)
│   ├── visualization.py
│   ├── simulation.py
│   └── utils.py
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/TRSIM_UAV_ML.git
cd TRSIM_UAV_ML
```

---

### 2. Create conda environment

```bash
conda env create -f environment.yml
```

---

### 3. Activate environment

```bash
conda activate trsim_fixed_compatible
```

---

### 4. Run the application

```bash
streamlit run ui_app.py
```

---

## Alternative (Your Current Local Method)

```bash
conda activate trsim_fixed_compatible
cd "C:\Users\danis\Downloads\TRSIM_UAV_ML_Modular_Ready"
streamlit run ui_app.py
```

---

## Requirements

Defined in `environment.yml`:

* Python 3.10
* streamlit
* pandas
* matplotlib
* networkx

---

## How It Works

1. The dashboard loads drone and trust data from CSV files
2. A simulated UAV network is displayed using NetworkX
3. Users select:

   * Attack type
   * Target drone
4. The system displays:

   * Trust values
   * Predicted model outputs (static/demo)

---

## Limitations

* ML predictions are **not dynamically computed**
* Attack selection does **not alter real data**
* Models are **not trained or loaded from files**

---

## Future Improvements

* Integrate real trained ML models (`.pkl` / `.h5`)
* Dynamic attack simulation affecting trust scores
* Real-time data updates
* Deployment (Streamlit Cloud / Docker)

---

## License

This project is for educational and research purposes.

---

