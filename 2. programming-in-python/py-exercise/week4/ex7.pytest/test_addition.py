import addition
import pytest

"""
The rule of thumb is that the assert statement looks for a Boolean result. 
You can use in, not in, is, <, >, other than == to check Boolean values. 
"""

# test_keyword must be inserted first
def test_add():
    assert True # if "False"  it fails, elif "True" it passes
    assert addition.add(4, 5) == 9
    
def test_sub():
    assert addition.sub(4, 5) == -1

"""------> to run this file
1. python -m pytest test_addition.py
2. pytest test_addition.py
3. pytest test_addition.py::test_add --------> for test specific function
4. pytest ex7.pytest/test_addition.py::test_add -------> test specific function outside the directory
5. pytest ex7.pytest/ ----------> outside the directory ex7.pytest

test function returns boolean value, if its true it prints "." if fail prints "F".
on the terminal -> "ex7.pytest/test_addition.py .. " this two dots represents 2 files are successfully
run, if one of them fails only one dot is printed and the other one represented by "F" which is failed
""" 