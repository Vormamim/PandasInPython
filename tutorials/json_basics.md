# JSON Basics Tutorial

JSON stands for **JavaScript Object Notation**.  It is a text-based,
language-independent format designed to store and transport structured
data.  Because of its simplicity and ubiquity, JSON is the de-facto
data interchange format used by nearly every modern web API.  You will
frequently receive JSON when making HTTP requests, and you may need to
produce JSON to send to a service or save your results.

This tutorial provides a gentle, step-by-step introduction to JSON
processing using Python's built-in `json` module.  It combines concise
code examples with explanatory text, similar to what you would find in a
textbook or classroom handout.

---

## 1. Loading JSON from a string or file

To begin working with JSON you must first convert (or *deserialize*) the
text into native Python objects.  The `json` module provides two main
functions for this purpose:

* `json.loads()` – load JSON from a *string*.
* `json.load()`  – load JSON directly from an open *file-like object*.

The resulting Python object uses dictionaries to represent JSON objects,
lists for JSON arrays, and the usual Python primitives for numbers, strings,
booleans and null.

Example of loading from a string literal:

```python
import json

text = '{"name": "Alice", "age": 30, "hobbies": ["reading", "hiking"]}'
data = json.loads(text)   # 'loads' = load string
print(data)
# output: {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'hiking']}
```

Reading from a file is just as simple; open the file in text mode and
pass the handle to `json.load`:

```python
with open('sample.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
```

After either call, `data` behaves like a normal Python collection; you can
index into it, iterate over it, etc.

---

## 2. Writing JSON

The mirror operations for serialization are `json.dumps()` and `json.dump()`.
The former returns a string, while the latter writes directly to a file.

```python
import json
obj = {'status': 'ok', 'results': [1, 2, 3]}

# convert Python object to JSON-formatted string
text = json.dumps(obj)  # 'dumps' = dump string
print(text)
# output: {"status": "ok", "results": [1, 2, 3]}
```

In many cases you will want the output to be human-readable for debugging
or logging.  The `indent` parameter tells the encoder to insert newlines
and indentation:

```python
pretty = json.dumps(obj, indent=2)
print(pretty)
```

```
{
  "status": "ok",
  "results": [
    1,
    2,
    3
  ]
}
```

Other useful options include `separators` (to control the commas/colons)
and `sort_keys=True` (to produce deterministic output by sorting dictionary
keys).

Writing directly to a file avoids the intermediate string:

```python
with open('out.json', 'w', encoding='utf-8') as f:
    json.dump(obj, f, indent=2)
```

The file will now contain the formatted JSON text. Read it back in with
`json.load` as shown earlier.

---

## 3. Common use cases with pandas

When you fetch data from a REST API, the response is almost always JSON.  A
straightforward way to begin analysis is to convert that JSON directly into
a `pandas.DataFrame`.

If the top-level element of the JSON is a **list of records** (i.e. a list
of dictionaries all sharing the same keys), then you can pass the list
directly to the `DataFrame` constructor:

```python
import pandas as pd
import json

# imagine api_response_text is the raw JSON string from the HTTP call
api_response_text = '[{"userId":1,"id":1,"title":"...","body":"..."}, ...]'

data = json.loads(api_response_text)
df = pd.DataFrame(data)
```

The resulting DataFrame will have one column per dictionary key (userId, id,
title, body), and one row per element of the list.

If the JSON is **nested** (objects inside objects), you may want to
download a flat table using `json_normalize`:

```python
from pandas import json_normalize

nested = {
    'users': [
        {'id': 1, 'name': 'Alice', 'prefs': {'theme': 'dark'}},
        {'id': 2, 'name': 'Bob', 'prefs': {'theme': 'light'}}
    ]
}

# flatten the 'users' list
flat = json_normalize(nested, 'users')
# you can expand nested fields by using 'record_path' and 'meta' parameters
```

Conversely, once you've manipulated a DataFrame you might want to write it
back out to JSON.  Use `DataFrame.to_json()`; common options are
`orient='records'` (produce list-of-dicts) and `lines=True` (one object
per line, useful for streaming):

```python
df.to_json('data.json', orient='records', lines=True)
```

This output can be sent to another API or simply stored for later reuse.

---

## 4. Handling non-standard types

The JSON specification only knows about a small set of primitive types:
strings, numbers, booleans (`true`/`false`), `null`, arrays and objects.  If
you try to serialize a Python object that does not map to one of these
(e.g. a `datetime`, a `Decimal`, or a custom class) the encoder will raise
a `TypeError`.

You can supply a `default` function to `dump`/`dumps` which will be called
for objects the encoder doesn't understand.  That function should return a
serializable object or raise `TypeError` itself:

```python
import json
import datetime

def default_serializer(o):
    if isinstance(o, datetime.datetime):
        # convert datetime to ISO 8601 string
        return o.isoformat()
    # let the encoder raise the error for other types
    raise TypeError(f"Type {type(o)} not serializable")

now = datetime.datetime.now()
text = json.dumps({'time': now}, default=default_serializer)
print(text)
```

When reading the JSON back you can parse those strings back into
datetime objects manually using `datetime.fromisoformat` or similar.

Many libraries (such as `pandas`) provide their own hooks or
`json_normalize` helpers to manage complex types automatically.

---

## 5. Error handling

When consuming JSON from external sources, never assume the input is
well-formed.  The `json` module will raise a subclass of
`ValueError` called `json.JSONDecodeError` when parsing fails.  Always
catch this exception around untrusted data to avoid crashing your program:

```python
from json import loads, JSONDecodeError

bad_text = "{not valid json}"
try:
    data = loads(bad_text)
except JSONDecodeError as e:
    print('invalid JSON received:', e)
    data = {}  # or handle the error appropriately
```

The exception object contains useful attributes such as `lineno` and
`colno` to pinpoint the location of the error in the input text.

Keeping error handling in place makes code robust when working with
highly variable web responses or when the JSON is generated by user
input.

---

## 6. Working with files generated earlier in this project

The `session` module in this repository stores `DataFrame` snapshots as
JSON under the hood.  You can open one of the session files manually and
use the techniques above to inspect or modify its contents.

---

This tutorial gives a quick overview of JSON operations; you can refer to
the official Python documentation for more details on the `json` module
and to `pandas` documentation for advanced normalization options.