"""
Weather Data Filtering Helpers

Functions tailored to time‑series data produced by Open‑Meteo.  Later
steps of the tutorial will use these to narrow the dataset by time or
numeric thresholds.
"""

import pandas as pd


def filter_by_time_range(df: pd.DataFrame, start, end, time_col="time") -> pd.DataFrame:
    """Return rows whose timestamp lies between `start` and `end`.

    `start`/`end` may be strings parseable by `pd.to_datetime`.
    """
    idx = pd.to_datetime(df[time_col])
    mask = (idx >= pd.to_datetime(start)) & (idx <= pd.to_datetime(end))
    return df[mask]


def filter_by_temp_range(df: pd.DataFrame, low, high, temp_col="temperature_2m") -> pd.DataFrame:
    """Keep rows where temperature is between `low` and `high`."""
    return df[(df[temp_col] >= low) & (df[temp_col] <= high)]


def filter_by_column_threshold(df: pd.DataFrame, column: str, threshold) -> pd.DataFrame:
    """Generic helper: return rows where column value >= threshold."""
    return df[df[column] >= threshold]
