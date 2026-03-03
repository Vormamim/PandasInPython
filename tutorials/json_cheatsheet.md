# JSON Cheat Sheet

A concise reference to the most frequently used operations with Python's
`json` module.  This is intended as a quick lookup for learners who have
already read the full JSON tutorial.

---

## Imports

```python
import json
```

(No other packages are required.)

---

## Loading / parsing

```python
# from string
obj = json.loads(text)

# from file
with open('file.json') as f:
    obj = json.load(f)
```

The result is a Python value (dict, list, str, int, float, bool, None).

---

## Writing / serializing

```python
# to string
text = json.dumps(obj)

# with indentation for readability
text = json.dumps(obj, indent=2)

# to file
with open('out.json', 'w') as f:
    json.dump(obj, f, indent=2)
```

Common arguments:
* `indent` – number of spaces, or `None` for compact output
* `sort_keys=True` – sort dictionary keys alphabetically
* `separators=(',', ':')` – remove spaces after commas/colons for compactness
* `default=func` – custom serializer for unsupported objects

---

## Handling errors

```
from json import JSONDecodeError

try:
    data = json.loads(bad_text)
except JSONDecodeError as exc:
    print('invalid JSON:', exc)
```

`JSONDecodeError` has attributes `lineno`, `colno` and `msg`.

---

## Streams and incremental parsing

```python
# load line-delimited JSON
with open('lines.json') as f:
    for line in f:
        record = json.loads(line)
        # process record
```

## Non-serializable types

```python
import datetime

def default(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()
    raise TypeError

json.dumps({'now': datetime.datetime.now()}, default=default)
```

---

## Practical tips

* Use `json.dumps(obj, ensure_ascii=False)` to preserve non-ASCII characters
* For large files, use a buffered reader and `json.load` to avoid memory spikes
* Many web APIs return HTTP responses with `.json()` method – equivalent
  to `json.loads(response.text)`
* `pandas.read_json()` is handy for directly ingesting many JSON formats

---

## Example quick reference

```python
# convert back and forth
mydict = {'a': 1}
text = json.dumps(mydict)
copy = json.loads(text)
```

This cheat sheet strips away verbose explanation and lets you glance at
the syntax when writing or reviewing code.