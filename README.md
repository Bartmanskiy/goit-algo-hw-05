## Description

This repository contains a set of Python exercises focused on recursion, memoization, generators, regular expressions, higher-order functions, and command-line application development.

The project demonstrates practical approaches to optimizing recursive calculations, extracting data from text, processing numerical values, and building an interactive contact management assistant.

## Technologies

* Python
* Recursion
* Memoization and caching
* Generators
* Regular expressions (`re`)
* Higher-order functions
* Dictionaries and data structures
* Exception handling
* Command-line interface (CLI)

## Functionality

### Fibonacci Sequence with Memoization

The `homework_1.py` script implements a Fibonacci number calculator using recursion combined with memoization.
The implementation:
* calculates Fibonacci numbers recursively;
* stores previously calculated values in a cache;
* reuses cached results to avoid unnecessary calculations;
* provides an optimized approach compared with a basic recursive implementation.

### Number Extraction and Income Calculation

The `homework_2.py` script processes text containing numerical values and calculates their total.
The implementation:
* uses a regular expression to find numbers in text;
* implements a generator for efficient value extraction;
* converts extracted values to floating-point numbers;
* uses a higher-order function to calculate the total income.

### Contact Management Assistant

The `homework_4.py` script implements an interactive command-line assistant for managing contacts.
The assistant supports:
* adding new contacts;
* changing existing phone numbers;
* searching for a contact's phone number;
* displaying all saved contacts;
* processing commands such as `hello`, `add`, `change`, `phone`, `all`, `close`, and `exit`;
* handling invalid input through a custom error-handling decorator;
* providing informative messages when required arguments are missing or a contact cannot be found.

## Links

GitHub: https://github.com/Bartmanskiy/goit-algo-hw-05
