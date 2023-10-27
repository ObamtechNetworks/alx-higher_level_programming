# 0x07. Python - Test-driven development
This section is the start of my learning journey on Test-Driven Development with Python at ALX

# Explanation of Testing in Software Development:
Testing is an essential aspect of software development that involves the process of evaluating a system or application to identify errors or discrepancies between expected and actual outcomes. 

The primary goal of testing is to ensure that software behaves as intended and to catch bugs before they reach users. 

Proper testing helps in delivering reliable, high-quality software.

Importance of Testing and Test-Driven Development (TDD):
Reliability: Testing ensures that the software functions correctly under various conditions, making it more reliable for users.
Bug Detection: Testing helps in identifying and fixing bugs early in the development process, reducing the cost of bug fixes.
Code Quality: Writing tests encourages writing modular and maintainable code, improving overall code quality.
Documentation: Tests serve as living documentation, providing examples of how code should be used.
Refactoring Confidence: Tests provide a safety net that allows developers to refactor code with confidence, knowing that existing functionality won't break.

# Test-Driven Development (TDD):
Test-Driven Development (TDD) is a software development approach where tests are written before the actual code.

The TDD process typically involves the following steps:

- Write a Test: Create a test that defines a function or improvements of a function, which should be very succinct.
- Run the Test: Ensure the test fails. This validates that the test does not pass for the current codebase.
- Write Code: Write the minimum amount of code necessary to pass the test. This step focuses on writing only the code required to make the test pass.
- Run Tests: Run all the tests to ensure the new one passes and existing functionality is not broken.
- Refactor Code: Refactor the code for readability, maintainability, or performance while ensuring all tests still pass.

# What Are Doctests in Python?
Doctests are tests that are embedded within the docstrings of Python functions or modules. They serve as documentation and test cases at the same time. Doctests are defined within triple quotes (either single or double) in the docstrings of a function or module.

### Writing Simple Doctests:
Let's consider a simple function:

```
def add(a, b):
    """
    This function adds two numbers.

    >>> add(1, 2)
    3
    >>> add(-1, 5)
    4
    """
    return a + b
```
In this example, the add function has two doctests within its docstring. Each doctest consists of an example usage of the function and the expected output.

### How to Run Doctests:
Python provides a built-in doctest module that can be used to run doctests. You can run doctests by executing the following command in the terminal:

`python -m doctest -v your_script.py`

### Using Doctests from a Text File:
Doctests can also be stored in a separate text file. For example, consider a file tests.txt:

```
# tests.txt
>>> add(1, 2)
3
>>> add(-1, 5)
4
```
To run doctests from a file, use the following command:
`python -m doctest -v -o TXT your_tests.txt`
This runs doctests from `your_tests.txt` and specifies the output format as TXT.

# Resources
### Read or watch:

- [doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)](https://docs.python.org/3/library/doctest.html)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
- [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
- [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases


# Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)*
- All your files must be executable
- The length of your files will be tested using wc
- Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

Let's journey together! :)
