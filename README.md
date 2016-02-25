# Apy
apy is a minimal python framework for creating rest APIs. Available under the
MIT License.
## Usage
this will create a service like [Github zen](https://api.github.com/zen)

### folder setup
```
zen.py
api/
    zen.json
    add.json
```
in api/zen.json:
```json
{
    "phrase":getPhrase(),
    "requests":req()
}
```
in api/add.json:
```json
{
    "number":nums()
}
```
in zen.py:
```python
from apy import apiMethod
import apy

phrases = [ #some phrases from https://api.github.com/zen
"Design for failure.",
"Anything added dilutes everything else.",
"Speak like a human.",
"Half measures are as bad as nothing at all.",
"Practicality beats purity.",
]

count = 0

@apiMethod
def getPhrase():
    global count
    count += 1
    return phrases[count%len(phrases)]


@apiMethod
def req():
    return count


@apiMethod
def phrase(p):
    phrases.append(p)


@apiMethod
def nums():
    return len(phrases)


apy.run("api")
```
### GET
a GET request to `/zen` returns something like:
```json
{
    "phrase":"Design for failure.",
    "request":"1"
}
```
### POST
a POST request to `/add`:

sent data:
```json
{
    "phrase":"Favor focus over features."
}
```
received data:
```json
{
    "number":6
}
```
after this, the phrase is now one of the phrases
