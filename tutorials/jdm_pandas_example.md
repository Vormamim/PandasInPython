# JDM Cars: Loading JSON into pandas

This very simple walkthrough shows how to read the `jdm_cars.json` file
located in the `tutorials/` directory, convert it to a `pandas` DataFrame,
and perform a couple of basic operations.  It is intended for absolute
beginners who have never combined JSON with pandas before.

## 1. Open a Python shell or create a new script

Make sure your virtual environment is active and run:

```bash
python -i
```

or create a file `example.py` and run it later.

## 2. Import the required modules

```python
import json
import pandas as pd
```

The `json` module reads the file, and `pandas` will manage the tabular data.

## 3. Load the JSON file

```python
with open('tutorials/jdm_cars.json', 'r', encoding='utf-8') as f:
    cars = json.load(f)

print(type(cars))          # should be a list
print(len(cars), 'records')
print(cars[0])             # look at the first dictionary
```

`cars` is now a list of dictionaries – each dictionary represents one car.

## 4. Create a DataFrame

```python
df = pd.DataFrame(cars)
print(df.head())
print(df.dtypes)
```

You now have a DataFrame with columns `make`, `model`, `year`, `region`,
`horsepower`, and `notes`.  Use `df.dtypes` to check their data types.

## 5. Basic exploration

```python
# filter to cars with horsepower above 270
powerful = df[df['horsepower'] > 270]
print(powerful)

# sort by year ascending
df_sorted = df.sort_values('year')
print(df_sorted)
```

## 6. Save a filtered subset

```python
powerful.to_csv('tutorials/powerful_jdm.csv', index=False)
```

You can now open `powerful_jdm.csv` in Excel or another tool.

## 7. Wrap-up

This example demonstrates the minimal steps:

1. read JSON, 2. convert to `DataFrame`, 3. inspect/filter, 4. export.

Feel free to modify the JSON file and repeat the steps to see how pandas
responds.  The JSON and cheat sheet tutorials explain the underlying concepts
in more depth.
