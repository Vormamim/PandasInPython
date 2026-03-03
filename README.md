# API Data Analysis with Pandas

A simple, console-driven Python project for teaching beginner students how to use pandas to access, filter, visualize, and save data obtained from a public web API.

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
  ├── api_handler.py            # Helpers for checking and calling a sample API
  ├── data_filter.py            # Simple filtering helpers for pandas DataFrames
  ├── visualizations.py         # Create line charts
  └── session.py                # Save/load sessions to disk

sessions/                        # Saved session data (created at runtime)
charts/                          # Generated visualization files
```

## Features

### 1. Access a Public API
The project uses **JSONPlaceholder** (`https://jsonplaceholder.typicode.com/posts`), a free test API with no authentication. You’ll learn how to verify the API is reachable.

### 2. Import into pandas
Convert the JSON response into a `DataFrame` for analysis.

### 3. Filter Data
Use helper functions to subset rows by numeric thresholds or other conditions.

### 4. Visualize
Create simple plots (e.g. post ID vs user ID) using `matplotlib`.

### 5. Save/Load Sessions
Keep your intermediate results by saving DataFrames and notes to disk.

## Dependencies

- **pandas** – Data manipulation and analysis
- **requests** – HTTP requests to APIs
- **matplotlib** – Data visualization
- **json** (built-in) – Session serialization
- **pathlib** (built-in) – File path handling


## Example Workflow

```python
# Start the program
python main.py

# 1. The script will check the sample API and fetch posts

# 2. A pandas DataFrame is created from the JSON response

# 3. Filter the data (e.g. keep only posts by user IDs ≤ 5)

# 4. Visualize post IDs vs user ID, or inspect rows in the console

# 5. Save your filtered dataset to a session file for later use
```

## Learning Resources

Open `main.py` to follow a step-by-step demonstration of each concept.  You can also inspect the helper modules under `src/` for individual examples.

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
