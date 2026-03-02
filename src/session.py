"""
Session management: save and load work to txt files.
"""

import json
from pathlib import Path


def save_session(name, data):
    """Save data dict to sessions/ folder as txt (JSON format)."""
    Path("sessions").mkdir(exist_ok=True)
    # convert DataFrame to dict if present
    if 'df' in data and hasattr(data['df'], 'to_dict'):
        data = data.copy()
        data['df'] = data['df'].to_dict(orient='records')
    
    with open(f"sessions/{name}.txt", 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {name}.txt")


def load_session(name):
    """Load data dict from sessions/ folder."""
    with open(f"sessions/{name}.txt", 'r') as f:
        return json.load(f)


def list_sessions():
    """List all saved sessions."""
    sessions = list(Path("sessions").glob("*.txt"))
    if not sessions:
        print("No sessions.")
        return
    print("Sessions:")
    for s in sorted(sessions):
        print(f"  {s.stem}")


