# Command Line Application

## Environment
Assuming following environment is in the target system.

- Python 3.4+ (comes with pip)
- virtualenv


## Start Setup
'python' referring to python3
- python -m virtualenv ENV
- source ENV/bin/activate
- pip install -r requirements.txt

## Start the application

>python start.py

Above command shows the following interface
>Select any product to find average cubic weight
>1. Air Conditioners

>Enter product number [strictly numeric value]

User has to enter the product number from the list else application will fail
>1

Output would be
>Average Cubic Weight: 41.6133846875 Kg

>Rounded Average Cubic Weight: 41.61 Kg

## Execute tests

>python -m unittest

## Support for different categories

The Application is designed in such a way that it can be extended to support 
different categories with minimal code, provided that average cubic weight 
calculation remains the same.
