# pandas Cheat Sheet

This quick reference covers common `pandas` operations that are useful
when working with tabular data.  It is intended as a companion to the
API and JSON tutorials; you can copy snippets into a REPL or script.

---

## Importing and creating dataframes

```python
import pandas as pd

# from a list of dicts
records = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
df = pd.DataFrame(records)

# from a CSV file
df = pd.read_csv('file.csv')

# from Excel
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
```

---

## Inspecting the data

```python
df.head()          # first 5 rows
df.tail(3)         # last 3 rows
len(df)            # number of rows
df.shape           # (rows, columns)
df.columns         # column names
df.dtypes          # data types of each column

df.info()          # summary of dataframe
```

---

## Selecting columns / rows

```python
# single column → Series
temp = df['temperature']

# multiple columns
df[['userId', 'id']]

# use .loc for label-based indexing
df.loc[0, 'userId']          # value at row 0, column 'userId'

# , separated slices
df.loc[0:4, ['userId', 'id']]

# .iloc for positional indexing
df.iloc[0, 1]
```

---

## Boolean filtering

```python
# keep rows where userId <= 5
df[df['userId'] <= 5]

# combine conditions
mask = (df['userId'] <= 5) & (df['id'] > 10)
df[mask]
```

---

## Adding / transforming columns

```python
df['new'] = df['userId'] * 10

df = df.assign(flag = df['userId'] > 3)
```

---

## Aggregations

```python
df['userId'].mean()
df['userId'].value_counts()
df.groupby('userId').size()
df.groupby('userId')['id'].max()
```

---

## Sorting

```python
df.sort_values('id')
df.sort_values(['userId','id'], ascending=[True, False])
```

---

## Handling missing data

```python
df.dropna()           # drop rows with any NaNs
df.fillna(0)          # replace NaN with 0
df['col'].isna()      # boolean mask where NaN
```

---

## Exporting results

```python
df.to_csv('out.csv', index=False)
df.to_json('out.json', orient='records')
```

---

## Miscellaneous tips

* Use `pd.to_datetime()` to convert strings to datetime dtype.
* `df.describe()` gives summary statistics for numeric columns.
* `df.sample(n=5)` returns a random subset of rows.
* Use `%%time` or `%timeit` in Jupyter to time operations.

This cheat sheet is not exhaustive, but covers the operations
commonly used during the tutorial workflow.  Refer to the
[pandas documentation](https://pandas.pydata.org/docs/) for more details.