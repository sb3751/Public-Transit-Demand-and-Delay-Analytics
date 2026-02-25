# src/data_processing/load_data.py

import os
import pandas as pd
from config import DATA_RAW


def load_gtfs_data():
    gtfs_path = os.path.join(DATA_RAW, "gtfs")

    stops = pd.read_csv(os.path.join(gtfs_path, "stops.txt"))
    trips = pd.read_csv(os.path.join(gtfs_path, "trips.txt"))
    stop_times = pd.read_csv(os.path.join(gtfs_path, "stop_times.txt"))

    print("Stops shape:", stops.shape)
    print("Trips shape:", trips.shape)
    print("Stop_times shape:", stop_times.shape)

    return stops, trips, stop_times