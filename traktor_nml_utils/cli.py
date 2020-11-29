from os.path import isfile
from pathlib import Path
import logging
import os
import sys

import click
from traktor_nml_utils import TraktorCollection

logger = logging.getLogger(__name__)


def get_nml_files(directory):
    return [
        Path(file) for file in os.scandir(directory) if
        isfile(file) and file.name.endswith('.nml')
    ]


@click.group()
@click.option('-v', '--verbose', count=True, help="Verbose logging")
@click.option('-d', '--debug', help="Debug logging")
def cli(verbose, debug):
    loglevel = logging.WARNING
    if verbose:
        loglevel = logging.INFO
    elif debug:
        loglevel = logging.DEBUG
    logging.basicConfig(level=loglevel)


@cli.command()
@click.argument('nml_file')
def traktor_import_file(nml_file):
    """NML file to import."""
    if not os.path.exists(nml_file):
        sys.exit(f"NML file {nml_file} does not exist")
    TraktorCollection(Path(nml_file))


@cli.command()
@click.argument('nml_dir')
def traktor_import_dir(nml_dir):
    """NML directory to import."""
    for nml_file in get_nml_files(nml_dir):
        collection = TraktorCollection(Path(nml_file))
        for entry in collection.entries:
            print(f"{nml_file} {entry.artist} - {entry.title}")


if __name__ == '__main__':
    cli()
