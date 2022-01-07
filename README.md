![PyCommons logo](https://mauricelambert.github.io/info/python/code/PyCommons_small.png "PyCommons logo")

# PyCommons

## Description

This package implements useful tools and functions for producing python packages or tools implemented in python.

Features implemented:

 - Timeout: 
     - Timeout decorator using MultiThreading
     - Timeout decorator using MultiProcessing
     - Timeout decorator using signal (UNIX only)
 - Terminal: ANSI features for terminal (color, position of the cursor, style...)
 - StringF:
     - Format the strings length
     - Make a table from Sequence of strings
     - Make a table of Attribute/Value from python object
 - PrintF:
     - Print states of tasks/programs
     - Print info, check OK/NOK, error... with prefix and color management
 - Process: generator to read process output lines in real time
 - Logs
     - Default logger builder
     - Decorator trace function (log the beginning and end of function execution)
     - Colored logger (StreamHandler only)
     - CSV formatter (logs in CSV format)
     - Handler for compressed log file rotation and store indefinitely
 - GetPass: a getpass function showing "\*"
 - Encodings:
     - Generator to obtain probable encodings
     - Function to try to decode the data with probable encodings
 - DictObject:
     - Dynamic object (build from dict)
     - JsonDeserializer
     - CsvDeserializer
 - Report:
     - Report as text/markdown
     - Report as CSV
     - Report as JSON
     - Report as HTML
     - Statistics
     - Sort and filter elements in the reports
     - The frequency and percentage of filtered elements
  - urlopen:
     - New urlopen based on urllib.request with a easiest way to manage HTTP error code (using decorator)
  - cleandict
     - Clean dict (for example, after loading the API response, you want to keep only certain information)

## Requirements

This package require:

 - python3
 - python3 Standard Library

## Installation

```bash
pip install PyCommons
```

## Usages

Examples with responses (mode console) are available in HTML documentation.

Note for import: add `PyCommons.<module>`
```python
from PyCommons.Timeout import *
import PyCommons.Timeout
```

## Links

 - [Github Page](https://github.com/mauricelambert/PyCommons/)
 - [Documentation Timeout](https://mauricelambert.github.io/info/python/code/PyCommons/Timeout.html)
 - [Documentation Terminal](https://mauricelambert.github.io/info/python/code/PyCommons/Terminal.html)
 - [Documentation StringF](https://mauricelambert.github.io/info/python/code/StringF.html)
 - [Documentation PrintF](https://mauricelambert.github.io/info/python/code/PrintF.html)
 - [Documentation Process](https://mauricelambert.github.io/info/python/code/Process.html)
 - [Documentation Logs](https://mauricelambert.github.io/info/python/code/Logs.html)
 - [Documentation GetPass](https://mauricelambert.github.io/info/python/code/GetPass.html)
 - [Documentation Encodings](https://mauricelambert.github.io/info/python/code/Encodings.html)
 - [Documentation DictObject](https://mauricelambert.github.io/info/python/code/DictObject.html)
 - [Documentation Report](https://mauricelambert.github.io/info/python/code/Report.html)
 - [Documentation urlopen](https://mauricelambert.github.io/info/python/code/urlopen.html)
 - [Documentation cleandict](https://mauricelambert.github.io/info/python/code/cleandict.html)
 - [Pypi package](https://pypi.org/project/PyCommons/)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
