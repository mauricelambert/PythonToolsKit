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
     - Operator (some basic functions callable from operator)
 - List:
     - Operator (some basic functions callable from operator)
 - Tuple:
     - Operator (some basic functions callable from operator)
 - Function:
     - Operator (some basic functions callable from operator)
 - Arguments:
     - Password and password prompt
     - Input file and stdin
     - Output file and stdout
     - Verbose mode
     - Debug mode
 - Thread:
     - Join all
     - Class SimpleThread
     - Thread decorator
 - Import:
     - import from path/filename
 - GetFile:
     - Research an existant file from current directory and lib directory
     - Open an existant file from current directory or lib directory
 - ScapyTools:
     - Command line arguments for scapy (ArgumentParser with an optional argument "interface" by default and iface research)
 - GetType
     - Type string value (None, bool, int, float, IP)
     - Numbers (int, float) and IP/network generator from string
 - Random: Get random strings (random length, generator, check for strong password, secure, urlsafe, ...)
 - Json:
     - Load invalid JSON
     - Correct invalid JSON

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

## Unittests

For `GetType` and `Json` modules i use `doctest` (unittests in documentation) and `coverage`:

```bash
python3 GetType.py             # run doctest with verbose mode
python3 -m doctest GetType.py  # run doctest without verbose mode
coverage run GetType.py        # Calcul coverage
coverage report                # Report in console
coverage html                  # Report in HTML page
```

| Module       | Coverage  | Statements | missing    |
|--------------|-----------|------------|------------|
| GetType.py   | 100%      | 130        | 000        |
| Json.py      | 100%      | 46         | 000        |

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
 - [Documentation Tuple](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Tuple.html)
 - [Documentation List](https://mauricelambert.github.io/info/python/code/PythonToolsKit/List.html)
 - [Documentation Function](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Function.html)
 - [Documentation Thread](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Thread.html)
 - [Documentation Import](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Import.html)
 - [Documentation ScapyTools](https://mauricelambert.github.io/info/python/code/PythonToolsKit/ScapyTools.html)
 - [Documentation GetFile](https://mauricelambert.github.io/info/python/code/PythonToolsKit/GetFile.html)
 - [Documentation GetType](https://mauricelambert.github.io/info/python/code/PythonToolsKit/GetType.html)
 - [Documentation Random](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Random.html)
 - [Documentation Json](https://mauricelambert.github.io/info/python/code/PythonToolsKit/Json.html)
 - [Pypi package](https://pypi.org/project/PythonToolsKit/)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
