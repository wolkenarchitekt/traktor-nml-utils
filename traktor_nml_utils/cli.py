import logging

import click
from traktor_nml_utils import TraktorCollection

logger = logging.getLogger(__name__)


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
def traktor_import(nml_file):
    collection = TraktorCollection(nml_file)
    for history_entry in collection.history:
        from pdb import set_trace; set_trace()
        print(history_entry)


if __name__ == '__main__':
    cli()
