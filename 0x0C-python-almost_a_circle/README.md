# 0x0C. Python - Almost a circle

In this project, I encapsulated skills in Python object-oriented programming by coding three connected classes to represent rectangles and squares. I wrote my own test suite using the unittest module to test all functionality for each class.

The three classes involved utilizing the following Python tools:

Import
Exceptions
Private attributes
Getter/setter
Class/static methods
Inheritance
File I/O
args / kwargs
JSON and CSV serialization/deserialization
Unittesting
Tests ✔️
tests/test_models: Folder containing the following independently-developed test files:
test_base.py
test_rectangle.py
test_square

## Class and Module Fixtures¶

Class and module level fixtures are implemented in TestSuite. When the test suite encounters a test from a new class then tearDownClass() from the previous class (if there is one) is called, followed by setUpClass() from the new class.

Similarly if a test is from a different module from the previous test then tearDownModule from the previous module is run, followed by setUpModule from the new module.