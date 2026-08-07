# Traktor NML utils

[![Tests](https://github.com/wolkenarchitekt/traktor-nml-utils/actions/workflows/test.yml/badge.svg)](https://github.com/wolkenarchitekt/traktor-nml-utils/actions/workflows/test.yml)
[![PyPI](https://img.shields.io/pypi/v/traktor-nml-utils)](https://pypi.org/project/traktor-nml-utils/)
![Python versions](https://img.shields.io/pypi/pyversions/traktor-nml-utils)

This module contains utilities to parse and modify [Native Instruments Traktor](https://www.native-instruments.com/de/products/traktor/dj-software/traktor-pro-3/) NML files.\
Traktor 2.x, 3.x and 4.x NML files are supported.

It can parse collection NML files (`$TRAKTOR_DIR/collection.nml`) and history NML files (`$TRAKTOR_DIR/History/history_$DATE.nml`).

All NML attributes are readable and writable using auto-generated dataclasses 
(see `traktor_nml_utils/models`).\
This allows a typesafe way to work with NML files, fully supporting IDE autocompletion

While reading should work in 99% cases, writing NML files hasn't been tested thoroughly enough yet, so always 
keep a copy of your NML files.

## Requirements

traktor-nml-utils requires Python 3.10 or newer.

traktor-nml-utils is tested with Traktor 4.x (NML `VERSION="20"`) and Traktor 3.3.0,
though it should be able to parse Traktor 2.x NML files as well. Feel free to provide
files that cause problems on parsing.  

## Installation

```shell
pip install traktor-nml-utils
```

## Usage

### Get artist, title and rating of all collection entries

```python
from traktor_nml_utils import TraktorCollection
from pathlib import Path

collection = TraktorCollection(path=Path("collection.nml"))

for entry in collection.nml.collection.entry:
    print(entry.artist, entry.title, entry.info.ranking)
```

### Get cuepoint start

```python
entry = collection.nml.collection.entry[0]

for cue_v2 in entry.cue_v2:
    print(cue_v2.start)
```

### Find entry

```python
artist = "Yotto"
title = "Another Riff For The Good Times (Extended Mix)"

entry = [
    entry
    for entry in collection.nml.collection.entry
    if entry.artist == artist and entry.title == title
][0]
```

### Add cuepoint

```python
from traktor_nml_utils.models.collection import CueV2Type
from traktor_nml_utils.utils import duration_str_to_milliseconds

my_cue = CueV2Type(
    value=None,
    name="n.n.",
    displ_order=0,
    type=0,
    start=duration_str_to_milliseconds("00:01:00"),
    len=0.0,
    repeats=-1,
    hotcue=1,
)
entry.cue_v2.append(my_cue)

# Write XML file
collection.save()
```

## Run tests

Run tests within Docker container:

```shell
argc docker-build
argc docker-test
```

Create virtualenv and run tests:

```shell
argc virtualenv-create
argc virtualenv-test
```


To test if parsing your own collection/history files with traktor-nml-utils works, 
pass your Traktor directory to the CLI:

```shell
traktor-nml-utils traktor-import ~/traktor3/
```

## How does it work?

### NML files to Python dataclasses

Since there is no official schema for Traktor NML files, the dataclasses in
`traktor_nml_utils/models/` were generated from sample NML files with
[xsdata](https://pypi.org/project/xsdata/), which infers the schema directly from
XML documents. They have since been hand-tuned to match Traktor's exact output
format, so they are maintained in the repository rather than regenerated blindly.

To generate fresh models from your own files, overwrite `collection.nml` and
`history.nml` in `./xml_to_xsd/` and run:

```shell
argc generate-models
```

This writes new models to `build/generated/`. Compare them against the hand-tuned
modules in `traktor_nml_utils/models/` and merge any differences manually (class
names differ: xsdata names classes after elements, e.g. `Entry` instead of the
committed `Entrytype`).
