# json2sql

A lightweight Python3 library for describing SQL statements using JSON

![codecov](https://codecov.io/gh/fridex/json2sql/branch/master/graph/badge.svg)
![PyPI Current Version](https://img.shields.io/pypi/v/json2sql.svg)
![PyPI Implementation](https://img.shields.io/pypi/implementation/json2sql.svg)
![PyPI Wheel](https://img.shields.io/pypi/wheel/json2sql.svg)
![Travis CI](https://travis-ci.org/fridex/json2sql.svg?branch=master)
![GitHub stars](https://img.shields.io/github/stars/fridex/json2sql.svg)
![GitHub license](https://img.shields.io/badge/license-ASL-blue.svg)
![Twitter](https://img.shields.io/twitter/url/http/github.com/fridex/json2sql.svg?style=social)

Is this project helpful? [Send me a simple warm message](https://saythanks.io/to/fridex)!

## Crossroad

 * [PyPI](https://pypi.python.org/pypi/json2sql)
 * [Travis CI](https://travis-ci.org/fridex/json2sql)
 * [Issue tracker](https://github.com/fridex/json2sql/issues)
 
 
## Documentation


### API design

* input - text file, string, dict
* kwargs


### json2sql.json2sql()

TBD

### json2sql.delete2sql()

TBD

### json2sql.insert2sql()

TBD

### json2sql.replace2sql()

TBD

### json2sql.select2sql()

TBD

### json2sql.update2sql()

TBD

## Installation

There is required Python3 in version 3.4 or later:

```bash
$ pip3 install json2sql
```

## Why was this library created?

The code was originally placed in [fabric8-analytics project](htpps://github.com/fabric8-analytics) for instrumentation of jobs based on API requests or periodic jobs written in YAML/JSON config files. Code was extracted to provide basic JSON/YAML/dict to SQL conversion.

## Under the hood

This project uses mosql under the hood for creating SQL statements. However it was not possible to use mosql to create more sophisticated queries (such as joins described by jobs or nested select queries). Check out [mosql](http://mosql.mosky.tw) page for more details.