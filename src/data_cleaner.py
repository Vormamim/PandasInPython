"""
Weather Data Cleaning Helpers

A minimal set of functions useful when working with the
`hourly` section returned by the Open‑Meteo API.  These assume you have
converted the JSON to a pandas DataFrame beforehand.
"""

import pandas as pd


def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Drop any rows containing NaN values (common after concatenating fields)."""
    return df.dropna()


def ensure_datetime(df: pd.DataFrame, column: str = "time") -> pd.DataFrame:
    """Convert the named column to pandas datetime dtype and return a copy."""
    new = df.copy()
    new[column] = pd.to_datetime(new[column])
    return new


def to_numeric(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Convert a column to numeric (float) type, coercing errors to NaN."""
    new = df.copy()
    new[column] = pd.to_numeric(new[column], errors="coerce")
    return new
