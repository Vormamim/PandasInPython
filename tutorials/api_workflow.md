# API Workflow Tutorial

This step-by-step guide walks through the entire project using the
helper modules in `src/`. It replicates the logic executed by
`main.py` so beginners can read and run the examples interactively.

---

## 1. Setup

Make sure you have the required packages installed:

```bash
pip install -r requirements.txt
```

You can run the examples in a Python REPL or execute the entire
script at the end of the file.

---

## 2. Checking the API

The `api_handler` module contains a small helper named
`check_api(url)` which performs a GET request and prints the status code.
This lets you verify that the remote service is reachable before
attempting to use its data.

```python
from src import api_handler

url = "https://jsonplaceholder.typicode.com/posts"
api_handler.check_api(url)
```

If the API returns `200`, you can proceed. In network-restricted
environments the function silently disables SSL verification so it
won't fail on self-signed certificates.

---

## 3. Fetching data and importing into pandas

Once the API is known to work, use `fetch_posts()` to retrieve a list of
post objects.  The helper fetches from the public JSONPlaceholder
service and returns a normal Python list of dictionaries.

```python
posts = api_handler.fetch_posts()

import pandas as pd

df = pd.DataFrame(posts)
print(df.shape)
print(df.head())
```

You now have a `DataFrame` with columns `userId`, `id`, `title`, and
`body`.

---

## 4. Filtering the data

The `data_filter` module provides simple predicates that operate on
`DataFrame`s.  For example, to keep only posts authored by users with
`userId` less than or equal to 5, use:

```python
from src import data_filter

df = data_filter.filter_by_column_threshold(df, "userId", 5)
print(df["userId"].unique())
```

You could combine filters by calling them sequentially.

---

## 5. Displaying results

`display_raw_data` in `api_handler` can print a short summary of
any list or dict structure.  Here we convert the filtered DataFrame back
into records and show the first few items:

```python
api_handler.display_raw_data(df.to_dict(orient="records"), max_items=3)
```

This is useful for quickly inspecting nested JSON-like objects.

---

## 6. Visualizing with matplotlib

The `visualizations.plot_line` function wraps a simple line chart. Use
it to plot `id` vs `userId`:

```python
from src import visualizations

visualizations.plot_line(df, "id", "userId")
```

When run in a normal environment a window will pop up.  If you pass a
`filename` argument the chart will be saved as a PNG instead.

---

## 7. Saving the session

Finally, the `session` module can persist your work.  DataFrames are
automatically converted to a list of records during saving so they can
be reloaded later and reconstructed.

```python
from src import session

session.save_session("posts_example", {"df": df, "notes": "Filtered userId<=5"})
```

To load the session again:

```python
data = session.load_session("posts_example")
df = pd.DataFrame(data["df"])
print(df.head())
print(data.get("notes"))
```

---

## 8. Running the full example

All of the above steps are orchestrated in `main.py`. To execute the
complete workflow from start to finish, simply run:

```bash
python main.py
```

The console output mirrors the snippets above and demonstrates how the
different modules collaborate.

---

Feel free to edit the examples in this tutorial or the helpers in
`src/` to experiment further. The goal is to make each step explicit so
learners can understand how to work with real-world APIs and pandas.
