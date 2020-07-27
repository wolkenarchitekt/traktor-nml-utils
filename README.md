# Traktor NML utils

[![Build Status](https://travis-ci.com/ifischer/traktor-nml-utils.svg?branch=master)](https://travis-ci.com/ifischer/traktor-nml-utils)

This module contains utilities to parse and modify Native Instruments Traktor NML files.

It can parse collection files (`$TRAKTOR_DIR/collection.nml`) and history 
files (`$TRAKTOR_DIR/History/history_$DATE.nml`).

You can deal with all XML data in a pythonic way.

## REWRITE IN PROGRESS ##

I'm currently rewriting this library to support reading and updating almost all available fields within NML files, using a 
very different approach (XML schema + python-xsdata generated data classes).

## Requirements

Because traktor-nml-utils uses `dataclasses`, you need at least Python 3.7.x. 

## Installation

```shell
pip install traktor-nml-utils
```

## Usage

```python
from traktor_nml_utils import TraktorCollection

collection = TraktorCollection('collection.nml')

for entry in collection.entries:
    print(entry)

for history_item in collection.history:
    print(history_item)
    
for playlist in collection.playlists:
    print(playlist)
```

## Run tests

Run tests within Docker container:

```shell
make build test
```

## Tutorials

### Get artist, title and rating of all collection entries

```python
from traktor_nml_utils import TraktorCollection

collection = TraktorCollection('collection.nml')

for entry in collection.entries:
    print(f'{entry.artist} - {entry.title} ({entry.ranking}')
```
