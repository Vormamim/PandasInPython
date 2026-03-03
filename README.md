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

### 4. Visualise
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

# Pandas & API Tutorial — Student Guide

Welcome! This project is a hands‑on introduction to working with web data
and pandas. It takes you from fetching JSON from a simple public API to
loading, filtering, visualising, and saving your results. Everything is
kept small and explicit so you can follow along in a REPL or a script.

## Learning outcomes

- Check whether an API is reachable
- Convert JSON into a `pandas.DataFrame`
- Filter and inspect tabular data
- Create a simple plot with `matplotlib`
- Save and reload your analysis session

## Quick start

1. Create and activate your virtual environment (recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the example workflow:

```bash
python main.py
```

## Files to inspect first

- `main.py` — runs a short, linear example covering all learning outcomes
- `src/api_handler.py` — shows how we check an API and fetch JSON
- `src/data_filter.py` — tiny helpers for selecting rows
- `src/visualizations.py` — a simple `plot_line()` wrapper
- `src/session.py` — save/load DataFrame snapshots in `sessions/`
- `tutorials/` — contains short guides and cheat sheets (JSON, pandas)

## Tutorials and examples

The `tutorials/` folder includes:

- `api_workflow.md`        — step-by-step example mirroring `main.py`
- `json_basics.md`        — textbook-style JSON tutorial
- `json_cheatsheet.md`    — quick reference for Python `json`
- `pandas_cheatsheet.md`  — common `pandas` commands and patterns
- `jdm_cars.json`         — small sample dataset for exercises
- `jdm_pandas_example.md` — super-basic example loading that sample

## Suggested exercises (for students)

1. Open `tutorials/jdm_cars.json` and load it into pandas. Try filtering
   by `horsepower` and saving the result as CSV. (See `jdm_pandas_example.md`.)
2. Modify `main.py` to fetch a different endpoint from JSONPlaceholder
   (e.g. `/users`) and inspect the returned columns.
3. Use `pandas_cheatsheet.md` to practice grouping and aggregation.

## Tips for students

- Work one step at a time: fetch → inspect → filter → visualise → save.
- If a network request fails, check your internet connection and try
  again; the helpers print status codes to help debug.
- Use the cheat sheets in `tutorials/` while you type commands.

## Need help?

- Open an issue in the repo or contact your instructor with the file and
  a short description of the problem (include console output if possible).

Enjoy exploring data with pandas!
