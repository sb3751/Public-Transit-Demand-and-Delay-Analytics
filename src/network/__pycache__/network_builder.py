# src/network/network_builder.py

import networkx as nx


def build_transit_graph(stop_times):
    """
    Build station graph from trip sequences
    """

    G = nx.Graph()

    # Sort for correct sequence
    stop_times_sorted = stop_times.sort_values(["trip_id", "stop_sequence"])

    for trip_id, group in stop_times_sorted.groupby("trip_id"):

        stops = group["stop_id"].tolist()

        # Connect consecutive stops
        for i in range(len(stops) - 1):
            G.add_edge(stops[i], stops[i+1])

    print("\nTransit graph built")
    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())

    return G

def compute_betweenness_centrality(G):
    """
    Compute betweenness centrality of stations
    """

    import pandas as pd
    import networkx as nx

    print("\nComputing betweenness (may take time)...")

    bc = nx.betweenness_centrality(G, k=500, seed=42)  
    # k sampling for speed

    df = pd.DataFrame({
        "stop_id": list(bc.keys()),
        "betweenness": list(bc.values())
    })

    df = df.sort_values("betweenness", ascending=False)

    print("\nBetweenness computed")
    print(df.head())

    return df

def compute_degree_centrality(G):
    """
    Compute degree centrality of stations
    """

    import pandas as pd
    import networkx as nx

    centrality = nx.degree_centrality(G)

    df = pd.DataFrame({
        "stop_id": list(centrality.keys()),
        "degree_centrality": list(centrality.values())
    })

    df = df.sort_values("degree_centrality", ascending=False)

    print("\nDegree centrality computed")
    print(df.head())

    return df