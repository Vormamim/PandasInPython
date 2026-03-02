# Weather Data Workflow Tutorial

This tutorial walks through a simple pandas-based workflow using three
support modules in the project:

* `src/api_handler.py`  - fetches forecast JSON from the Open‑Meteo API
* `src/data_cleaner.py` - minimal cleaners for weather DataFrames
* `src/data_filter.py`  - helpers to filter time-series weather data
* `src/visualizations.py` - simple plotting functions

The goal is to show a beginner how to access a free weather API, transform
the data into a pandas DataFrame, clean and filter it, and optionally
export results.

---

## Prerequisites

1. Python 3.8+ installed (workspace already configured).
2. Key packages (from `requirements.txt`):
   - **`pandas`** – Data manipulation and analysis (DataFrames).
   - **`requests`** – HTTP requests for fetching API data.
   - **`matplotlib`** – Plotting and chart creation.
   - **`pickle`** (built-in) – Serializing Python objects for session saving.
   - **`pathlib`** (built-in) – File path handling.
3. The five helper modules should exist in `src/`:
   - `api_handler.py`, `data_cleaner.py`, `data_filter.py`, `visualizations.py`, `session.py`

You can run examples in a normal Python REPL or a script. All output will
appear in the console.

---

## 1. Fetching the Weather JSON

```python
from src import api_handler

# fetch 7-day forecast for Sydney
weather_json = api_handler.fetch_weather(-33.86, 151.20)
# inspect basic structure
print(type(weather_json))
print(weather_json.keys())
```

The returned object is a standard Python `dict` containing metadata and
an `hourly` sub-dictionary with arrays of values.

---

## 2. Converting to a pandas DataFrame

```python
import pandas as pd

hourly = weather_json['hourly']
df = pd.DataFrame(hourly)
print(df.head())
print(df.dtypes)
```

At this point the `time` column is strings and the numeric columns may be
objects. We will apply cleaning helpers next.

---

## 3. Cleaning the Data

Use functions from `data_cleaner.py`:

```python
from src import data_cleaner

# ensure timestamps are true datetimes
df = data_cleaner.ensure_datetime(df)
# convert temperature to numeric float
df = data_cleaner.to_numeric(df, 'temperature_2m')
```

If there were missing or malformed values, you could also call
`data_cleaner.drop_missing(df)` before analysis.

---

## 4. Filtering the Data

The `data_filter` module provides simple predicates:

```python
from src import data_filter

# show only entries on March 2, 2026
march2 = data_filter.filter_by_time_range(df, '2026-03-02', '2026-03-02 23:59')
print(march2)

# find times when temperature exceeded 256C
hot = data_filter.filter_by_temp_range(df, 25, 100)
print(hot[['time', 'temperature_2m']])
```

Combination of filters is as easy as applying them sequentially.

---

## 5. Visualizing the Data

The `visualizations` module has one simple function:

```python
from src import visualizations

# line chart of temperature vs time
data = march2  # reuse filtered dataframe
visualizations.plot_line(data, 'time', 'temperature_2m', filename="charts/march2_temp.png")

# or show humidity on screen
visualizations.plot_line(data, 'time', 'relative_humidity_2m')
```

Passing `filename` saves as PNG; omitting it shows the chart.

---

## 6. Exporting Results

Once filtered or cleaned, the dataframe can be written to disk:

```python
march2.to_csv('charts/march2_weather.csv', index=False)
```

Or you could save just the temperature series, etc.

---

## 7. Saving Your Session

The `session` module (in `src/session.py`) saves your work to human-readable **txt files** (JSON format).
It uses:

- **`json`** (built-in) – Serializes Python dicts and lists as plain text.
- **`pathlib`** (built-in) – Manages file paths.

Example workflow:

```python
from src import session

# package your work into a dict
my_session = {
    'df': df,
    'march2_data': march2,
    'notes': 'Filtered Sydney weather for March 2, 2026'
}

# save it (creates sessions/sydney_march2.txt in JSON format)
session.save_session('sydney_march2', my_session)

# later, load it back
loaded = session.load_session('sydney_march2')
df = loaded['df']  # note: now a list of dicts, convert back if needed
print(loaded['notes'])

# see all saved sessions
session.list_sessions()
```

Txt files are human-readable and viewable in any text editor.
Note: DataFrames are converted to dict format (records), so you may need to
reconvert them back: `df = pd.DataFrame(loaded['df'])`.

---

## 8. Practice Exercises

1. Modify the coordinate values to fetch your own city’s forecast.
2. Add a step in cleaning to rename `temperature_2m` to `temp_C`.
3. Use `pandas` to compute daily mean temperature from the hourly data.

---

This simple workflow demonstrates how the three helper modules interact:
`api_handler` gets the raw data, `data_cleaner` prepares it for analysis,
and `data_filter` makes it easy to focus on interesting subsets.  Students
can now build plots, statistics, and save sessions as needed.