# src/analysis/demand_analysis.py

import os
import pandas as pd
import matplotlib.pyplot as plt
from config import FIGURES, TABLES


# ==============================
# AGGREGATION
# ==============================

def compute_hourly_demand(stop_times):
    """Compute hourly arrival frequency as demand proxy"""
    hourly = (
        stop_times
        .groupby("hour")
        .size()
        .reset_index(name="arrivals")
        .sort_values("hour")
    )

    print("\nHourly demand computed")
    print(hourly.head())
    return hourly


def compute_station_demand(stop_times, stops):
    """Compute arrival frequency per station"""
    station = (
        stop_times
        .groupby("stop_id")
        .size()
        .reset_index(name="arrivals")
        .sort_values("arrivals", ascending=False)
    )

    station = station.merge(stops, on="stop_id", how="left")

    print("\nStation demand computed")
    print(station.head())
    return station


# ==============================
# VISUALIZATION
# ==============================

def plot_hourly_demand(hourly):
    plt.figure(figsize=(10, 5))
    plt.plot(hourly["hour"], hourly["arrivals"], marker="o")
    plt.title("Hourly Transit Demand (Arrival Frequency)")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Arrivals")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    print("\nDemand plot displayed")


def plot_top_stations(station, top_n=10):
    top = station.head(top_n)

    plt.figure(figsize=(10, 6))
    plt.barh(top["stop_name"], top["arrivals"])
    plt.gca().invert_yaxis()
    plt.title("Top Congestion Stations")

    path = os.path.join(FIGURES, "top_stations.png")
    plt.savefig(path)
    plt.show()
    plt.close()


def plot_station_map(station, top_n=200):
    subset = station.head(top_n)

    plt.figure(figsize=(8, 8))
    plt.scatter(subset["stop_lon"], subset["stop_lat"], s=subset["arrivals"] * 2, alpha=0.6)

    path = os.path.join(FIGURES, "station_map.png")
    plt.savefig(path)
    plt.show()
    plt.close()


def plot_demand_vs_centrality(merged):
    plt.figure(figsize=(8, 6))
    plt.scatter(merged["degree_centrality"], merged["arrivals"], alpha=0.5)

    path = os.path.join(FIGURES, "demand_vs_centrality.png")
    plt.savefig(path)
    plt.show()
    plt.close()


# ==============================
# IO
# ==============================

def save_hourly_outputs(hourly):
    hourly.to_csv(os.path.join(TABLES, "hourly_demand.csv"), index=False)

    plt.figure(figsize=(10, 5))
    plt.plot(hourly["hour"], hourly["arrivals"], marker="o")
    plt.title("Hourly Transit Demand")
    plt.grid(True)

    plt.savefig(os.path.join(FIGURES, "hourly_demand.png"))
    plt.close()

    print("\nOutputs saved")


def save_station_outputs(station):
    station.to_csv(os.path.join(TABLES, "station_demand.csv"), index=False)
    print("Station demand saved")


def save_merged_outputs(merged):
    merged.to_csv(os.path.join(TABLES, "network_demand_merged.csv"), index=False)
    print("Merged dataset saved")


# ==============================
# INTEGRATION
# ==============================

def merge_network_demand(station, centrality_df):
    merged = station.merge(centrality_df, on="stop_id", how="left")
    merged = merged.sort_values("arrivals", ascending=False)

    print("\nDemand + network merged")
    print(merged.head())
    return merged


def merge_betweenness(merged, bc_df):
    final = merged.merge(bc_df, on="stop_id", how="left")

    print("\nFinal importance dataset created")
    print(final.head())
    return final