# Traktor NML utils

This module contains utilities to parse and modify Traktor NML files.

It can parse collection files (`$TRAKTOR_DIR/collection.nml`) and history 
files (`$TRAKTOR_DIR/History/history_$DATE.nml`).

You can deal with all XML data in the most Pythonic way.

## Requirements

Because traktor-nml-utils uses `dataclasses`, you need at least Python 3.7.x. 

## Installation

```
pip install --user git+ssh://git@github.com/ifischer/traktor-nml-utils.git@1.0.0
```

## Usage

```
from traktor_nml_utils import TraktorCollection

collection = TraktorCollection('collection.nml')

for entry in collection.entries:
    print(entry)

for history_item in collection.history:
    print(history_item)
    
for playlist in collection.playlists:
    print(playlist)
```


