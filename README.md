# Weather Data Analysis with Pandas

A simple, console-driven Python project for teaching beginner students how to use pandas to access, clean, filter, and visualize real-world data.

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

## Project Structure

```
main.py                          # Console menu entry point
README.md                        # This file
requirements.txt                 # Python dependencies
src/
  ├── api_handler.py            # Fetch weather data from Open-Meteo API
  ├── data_cleaner.py           # Clean and prepare data
  ├── data_filter.py            # Filter data by time or values
  ├── visualizations.py         # Create line charts
  └── session.py                # Save/load sessions to disk
tutorials/
  ├── weather_workflow.md       # Complete step-by-step guide
  └── tutorial_01_api_basics.py # API basics tutorial
sessions/                        # Saved session data (created at runtime)
charts/                          # Generated visualization files
```

## Features

### 1. Fetch Weather Data
Retrieve hourly weather forecasts from the **Open-Meteo API** (free, no authentication required):
- Temperature, humidity, wind speed, and more
- Any coordinates (latitude/longitude)
- Automatic timezone detection

### 2. Clean Data
Handle missing values, convert data types, ensure datetime formats.

### 3. Filter Data
- Filter by time range
- Filter by temperature range
- Filter by column threshold

### 4. Visualize
Generate line charts and save as PNG files.

### 5. Save/Load Sessions
Store your work as human-readable `.txt` files in JSON format for later analysis.

## Dependencies

- **pandas** – Data manipulation and analysis
- **requests** – HTTP requests to APIs
- **matplotlib** – Data visualization
- **json** (built-in) – Session serialization
- **pathlib** (built-in) – File path handling

## Menu Options

When you run `python main.py`, you'll see:

```
1. Fetch weather data       - Get live weather data from Open-Meteo
2. Clean and prepare data   - Handle missing values and data types
3. Filter data              - Subset data by date or temperature
4. Visualize data           - Create line charts
5. Save session             - Store your dataframe and notes
6. Load session             - Restore a previous session
7. List sessions            - See all saved sessions
0. Exit
```

## Example Workflow

```python
# Start the program
python main.py

# 1. Fetch weather for Sydney
   Option 1 → Latitude: -33.86 → Longitude: 151.20

# 2. Clean the data
   Option 2 → Ensure datetime format

# 3. Filter to March 2nd only
   Option 3 → Filter by time range → 2026-03-02 → 2026-03-03

# 4. Visualize temperature over time
   Option 4 → X: time → Y: temperature_2m

# 5. Save your work
   Option 5 → Session name: sydney_march2 → Notes: Morning data
```

## Learning Resources

See [tutorials/weather_workflow.md](tutorials/weather_workflow.md) for a comprehensive step-by-step guide covering all modules and concepts.

## File Format: Sessions

Sessions are saved as human-readable `.txt` files in JSON format:

```json
{
  "df": [
    {"time": "2026-03-02T00:00", "temperature_2m": 18.5, ...},
    {"time": "2026-03-02T01:00", "temperature_2m": 17.8, ...}
  ],
  "notes": "Your notes here"
}
```

When loading a session, DataFrames stored as dicts are automatically converted back to pandas DataFrames.
