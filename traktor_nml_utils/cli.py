import logging
from pathlib import Path

import click
from traktor_nml_utils import TraktorCollection, TraktorHistory, is_history_file

logger = logging.getLogger(__name__)


@click.group()
@click.option("-v", "--verbose", count=True, help="Verbose logging")
@click.option("-d", "--debug", help="Debug logging")
def cli(verbose, debug):
    loglevel = logging.WARNING
    if verbose:
        loglevel = logging.INFO
    elif debug:
        loglevel = logging.DEBUG
    logging.basicConfig(level=loglevel)


@cli.command()
@click.argument("nml")
def traktor_import(nml):
    """NML import from file or directory."""
    p = Path(nml)
    if p.is_dir():
        nml_files = p.glob("**/*.nml")
    else:
        nml_files = [p]

    for nml_file in nml_files:
        print(f"Importing NML: {nml_file}")
        if is_history_file(nml_file):
            TraktorHistory(nml_file)
        else:
            TraktorCollection(nml_file)


if __name__ == "__main__":
    cli()
