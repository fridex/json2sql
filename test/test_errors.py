#!/usr/bin/env python3
# ######################################################################
# Copyright (C) 2017  Fridolin Pokorny, fridolin.pokorny@gmail.com
# This file is part of json2sql package.
# ######################################################################
"""Tests for error handling."""

from json2sql import select2sql
from json2sql import ParsingInputError
import pytest

from .base import TestBase


class TestErrors(TestBase):
    """Tests for error handling."""

    def test_unknown_subquery_key(self):
        wrong_nested_query = {'$filter': {'table': 'BarTable'}, 'wrong_key': 'baz'}
        with pytest.raises(ParsingInputError):
            select2sql(table='FooTable', where={'something in': wrong_nested_query})
