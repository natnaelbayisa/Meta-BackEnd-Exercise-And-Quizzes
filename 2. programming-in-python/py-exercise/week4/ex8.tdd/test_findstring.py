from curses.ascii import isdigit
import pytest 
import findstring

def test_ispresent():
    assert findstring.ispresent("dell")
    
def test_nodigit():
    assert findstring.nodigit("N8")