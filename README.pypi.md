# Traktor NML utils

[![Build Status](https://travis-ci.com/wolkenarchitekt/traktor-nml-utils.svg?branch=master)](https://travis-ci.com/wolkenarchitekt/traktor-nml-utils)

This module contains utilities to parse and modify Native Instruments Traktor NML files.

It can parse collection files (`$TRAKTOR_DIR/collection.nml`) and history 
files (`$TRAKTOR_DIR/History/history_$DATE.nml`).

## Requirements

Because traktor-nml-utils uses `dataclasses`, you need at least Python 3.7.x. 

## Installation

```shell
pip install traktor-nml-utils
```

## Usage

### Get artist, title and rating of all collection entries

```python
from traktor_nml_utils import TraktorCollection
from pathlib import Path

collection = TraktorCollection(path=Path('collection.nml'))

for entry in collection.model.entry:
    print(entry.artist, entry.title, entry.info.ranking)

```
