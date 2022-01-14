![PythonToolsKit logo](https://mauricelambert.github.io/info/python/code/PythonToolsKit/logo_small.png "PythonToolsKit logo")

# PythonToolsKit

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
  - Dict:
     - Clean dict (for example, after loading the API response, you want to keep only certain informations)
  - Arguments:
     - Password and password prompt
     - Input file and stdin
     - Output file and stdout

## Requirements

This package require:

 - python3
 - python3 Standard Library

## Installation

```bash
pip install PythonToolsKit
```

## Usages

Examples with responses (mode console) are available in HTML documentation.

Note for import: add `PythonToolsKit.<module>`

```python
from PythonToolsKit.Timeout import *
import PythonToolsKit.Timeout
```

## Links

 - [Github Page](https://github.com/mauricelambert/PythonToolsKit/)
 - [Documentation Timeout](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Timeout.html)
 - [Documentation Terminal](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Terminal.html)
 - [Documentation StringF](https://mauricelambert.github.io/info/python/code/PythonToolsKit/StringF.html)
 - [Documentation PrintF](https://mauricelambert.github.io/info/python/code/PythonToolsKit/PrintF.html)
 - [Documentation Process](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Process.html)
 - [Documentation Logs](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Logs.html)
 - [Documentation GetPass](https://mauricelambert.github.io/info/python/code/PythonToolsKit/GetPass.html)
 - [Documentation Encodings](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Encodings.html)
 - [Documentation DictObject](https://mauricelambert.github.io/info/python/code/PythonToolsKit/DictObject.html)
 - [Documentation Report](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Report.html)
 - [Documentation urlopen](https://mauricelambert.github.io/info/python/code/PythonToolsKit/urlopen.html)
 - [Documentation Dict](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Dict.html)
 - [Documentation Arguments](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Arguments.html)
 - [Pypi package](https://pypi.org/project/PythonToolsKit/)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
