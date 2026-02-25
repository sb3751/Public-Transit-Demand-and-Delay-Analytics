# src/data_processing/time_features.py

import pandas as pd


def add_time_features(stop_times):
    """
    Convert arrival_time to useful time features
    """

    # Convert to timedelta (GTFS safe approach)
    stop_times["arrival_td"] = pd.to_timedelta(stop_times["arrival_time"])

    # Extract components
    stop_times["hour"] = stop_times["arrival_td"].dt.components.hours
    stop_times["minute"] = stop_times["arrival_td"].dt.components.minutes
    stop_times["second"] = stop_times["arrival_td"].dt.components.seconds

    print("\nTime features added")

    return stop_times