# main.py

from src.data_processing.load_data import load_gtfs_data
from src.data_processing.inspect_data import inspect_dataframe
from src.data_processing.time_features import add_time_features

# Analysis
from src.analysis.demand_analysis import (
    compute_hourly_demand,
    plot_hourly_demand,
    save_hourly_outputs,
    compute_station_demand,
    plot_top_stations,
    plot_station_map,
    merge_network_demand,
    plot_demand_vs_centrality,
    save_station_outputs,
    save_merged_outputs,
    merge_betweenness
)

# Network
from src.network.network_builder import (
    build_transit_graph,
    compute_degree_centrality,
    compute_betweenness_centrality
)

def main():

    print("Pipeline started")

    # ---------- DATA ----------
    stops, trips, stop_times = load_gtfs_data()
    inspect_dataframe(stops, "STOPS")
    inspect_dataframe(trips, "TRIPS")
    inspect_dataframe(stop_times, "STOP_TIMES")
    stop_times = add_time_features(stop_times)

    # ---------- TEMPORAL ----------
    hourly = compute_hourly_demand(stop_times)
    plot_hourly_demand(hourly)
    save_hourly_outputs(hourly)

    # ---------- SPATIAL ----------
    station = compute_station_demand(stop_times, stops)
    plot_top_stations(station)
    plot_station_map(station)

    # ---------- NETWORK ----------
    G = build_transit_graph(stop_times)
    centrality_df = compute_degree_centrality(G)

    # ---------- INTEGRATION ----------
    merged = merge_network_demand(station, centrality_df)
    plot_demand_vs_centrality(merged)
    save_station_outputs(station)
    save_merged_outputs(merged)

    # ---------- ADVANCED ----------
    bc_df = compute_betweenness_centrality(G)
    final_df = merge_betweenness(merged, bc_df)
    final_df.to_csv("outputs/tables/final_station_importance.csv", index=False)

    print("\nPipeline step complete")


if __name__ == "__main__":
    main()