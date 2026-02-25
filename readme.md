# 🚆 Public Transit Demand & Delay Analytics

## 📌 Overview

Urban public transportation systems exhibit dynamic passenger demand patterns and complex network interactions that influence operational efficiency and service reliability. Understanding these patterns is essential for identifying congestion hotspots, structural hubs, and potential vulnerability points within transit systems.

This project analyzes General Transit Feed Specification (GTFS) data to explore **temporal demand variability**, **spatial congestion distribution**, and **network topology characteristics**. By integrating time-series, spatial, and graph-based analytics, the project constructs a multi-dimensional framework for evaluating station importance within an urban transit network.

---

## 🎯 Objectives

* Analyze temporal demand patterns across the transit system
* Identify spatial congestion hotspots at station level
* Construct a transit network graph from vehicle movement sequences
* Detect connectivity hubs and flow bridge stations using network metrics
* Integrate operational and structural indicators to reveal heterogeneous station roles

---

## 📂 Dataset

The project utilizes a **GTFS transit feed**, including:

* **stops.txt** → Station metadata and geographic coordinates
* **trips.txt** → Vehicle journey information
* **stop_times.txt** → Temporal vehicle movement across stations

GTFS represents the industry standard format used in mobility analytics and transportation research.

---

## ⚙️ Methodology

### 🟢 1. Data Engineering

* Ingested and validated GTFS tables
* Performed schema inspection and missing value analysis
* Generated temporal features from arrival timestamps

### 🟢 2. Temporal Analytics

* Aggregated arrival frequency by hour
* Visualized demand seasonality
* Identified peak operational periods

### 🟢 3. Spatial Analytics

* Computed station-level arrival frequency as demand proxy
* Ranked congestion hotspots
* Produced geographic congestion visualization

### 🟢 4. Network Analytics

* Constructed station adjacency graph from trip sequences
* Computed **degree centrality** to identify connectivity hubs
* Computed **betweenness centrality** to detect flow bridge stations
* Integrated demand and network metrics into a unified importance dataset

---

## 📊 Key Findings

### ⭐ Commuter-driven temporal demand

Temporal aggregation revealed pronounced morning and evening peaks consistent with commuter behavior, alongside minimal late-night activity.

### ⭐ Corridor-based congestion clustering

Spatial visualization showed congestion concentrated along primary transit corridors rather than uniformly distributed across the network.

### ⭐ Structural connectivity hubs

Degree centrality analysis identified stations serving as transfer points with high connectivity across routes.

### ⭐ Bridge stations as vulnerability points

Betweenness centrality highlighted stations critical for maintaining network flow, indicating potential fragmentation risk during disruptions.

### ⭐ Heterogeneous station roles

Combining operational and network metrics revealed diverse station roles, including high-demand hubs, congestion bottlenecks, structural connectors, and peripheral coverage nodes.

---

## 📈 Visual Outputs

### 🕒 Hourly Demand Pattern

* Temporal arrival frequency curve
* Peak hour identification

### 📍 Congestion Hotspots

* Station demand ranking
* Geographic congestion scatter map

### 🕸️ Network Intelligence

* Connectivity hub detection
* Demand vs connectivity scatter visualization

---

## 🗂️ Project Structure

```
Public-Transit-Demand-and-Delay-Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data_processing/
│   ├── analysis/
│   └── network/
│
├── outputs/
│   ├── figures/
│   └── tables/
│
├── dashboard/
├── docs/
├── main.py
└── config.py
```

---

## 🧠 Technologies Used

* Python
* Pandas & NumPy
* Matplotlib & Seaborn
* NetworkX
* Power BI (dashboard layer)

---

## 📦 Generated Artifacts

* Hourly demand feature table
* Station congestion dataset
* Network demand integration dataset
* Multi-dimensional station importance dataset
* Analytical visualizations for temporal, spatial, and network insights

---

## 🚀 Future Work

* Delay propagation modeling
* Temporal network centrality analysis
* Demand anomaly detection
* Integration of weather and event data
* Predictive congestion forecasting

---

