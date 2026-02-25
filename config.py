# config.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")

FIGURES = os.path.join(BASE_DIR, "outputs", "figures")
TABLES = os.path.join(BASE_DIR, "outputs", "tables")