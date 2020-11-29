from os.path import isfile
from pathlib import Path
import logging
import os

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
@click.option('--nml-file', help="NML file to import")
def traktor_import_file(nml_file):
    TraktorCollection(nml_file)


@cli.command()
@click.option('--nml-dir', help="NML dir to import recursively")
def traktor_import_dir(nml_dir):
    for nml_file in get_nml_files(nml_dir):
        collection = TraktorCollection(str(nml_file))
        for entry in collection.entries:
            print(f"{nml_file} {entry.artist} - {entry.title}")


if __name__ == '__main__':
    cli()
