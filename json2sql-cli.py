#!/usr/bin/env python3
# ######################################################################
# Copyright (C) 2017  Fridolin Pokorny, fridolin.pokorny@gmail.com
# This file is part of json2sql package.
# ######################################################################
"""Convert JSON/YAML/dict to a SQL statement."""

import logging
import sys

import click

import daiquiri
from json2sql import delete2sql
from json2sql import insert2sql
from json2sql import json2sql
from json2sql import replace2sql
from json2sql import select2sql
from json2sql import update2sql

_logger = daiquiri.getLogger(__name__)


class CliInputError(Exception):
    """Exception raised when wrong CLI arguments are passed."""


@click.command()
@click.option('--delete', '-D', is_flag=True, help='Treat input as DELETE SQL statement.')
@click.option('--insert', '-I', is_flag=True, help='Treat input as INSERT SQL statement.')
@click.option('--replace', '-R', is_flag=True, help='Treat input as REPLACE SQL statement.')
@click.option('--select', '-S', is_flag=True, help='Treat input as SELECT SQL statement.')
@click.option('--update', '-U', is_flag=True, help='Treat input as UPDATE SQL statement.')
@click.option('--output-file', '-o', default=None, help='Specify output file.')
@click.option('--amend-output', '-a', is_flag=True, help='Amend to output file instead of overwriting it.')
@click.option('--input-file', '-i', default=None, help='Specify input file.')
@click.option('--verbose', '-v', count=True, help='Increase logging verbosity, can be used multiple times.')
def main(delete=False, insert=False, replace=False, select=False, update=False,
         output_file=None, amend_output=False, input_file=None, verbose=0):
    """Convert JSON/YAML/dict to a SQL statement."""
    if verbose:
        # hack based on num values of logging.DEBUG, logging.INFO, ...
        level = max(logging.ERROR - verbose * 10, logging.DEBUG)
        daiquiri.setup(outputs=(daiquiri.output.STDERR,), level=level)

    if amend_output and not output_file:
        raise CliInputError("Flag --amend-output specified but no --output-file specified.")

    count = int(delete) + int(insert) + int(replace) + int(select) + int(update)
    if count > 1:
        raise CliInputError("Only one of --delete, --insert, --replace, --select, --update "
                            "can be supplied at once.")

    if delete:
        _logger.debug("Translating DELETE description to SQL statement")
        result = delete2sql(input_file or sys.stdin)
    elif insert:
        _logger.debug("Translating INSERT description to SQL statement")
        result = insert2sql(input_file or sys.stdin)
    elif replace:
        _logger.debug("Translating REPLACE description to SQL statement")
        result = replace2sql(input_file or sys.stdin)
    elif select:
        _logger.debug("Translating SELECT description to SQL statement")
        result = select2sql(input_file or sys.stdin)
    elif update:
        _logger.debug("Translating UPDATE description to SQL statement")
        result = update2sql(input_file or sys.stdin)
    else:
        _logger.debug("Translating JSON/YAML description to SQL statement")
        result = json2sql(input_file or sys.stdin)

    _logger.debug("Result is: %s", result)

    if output_file is not None:
        _logger.debug("Writing output to file '%s' - content will be %s",
                      output_file, 'amended' if amend_output else 'overwritten')
        with open(output_file, 'a' if amend_output else 'w') as f:
            f.write(result)
            f.write('\n')
    else:
        _logger.debug("Writing output to stdout")
        print(result)


if __name__ == '__main__':
    main()
