from calc import *

def test_add():
    result = addNumbers(1,2)
    assert result == 3, "Add is not working"

def test_subtract():
    result = subtractNumbers(5,4)
    assert result == 1, "Subtract is not working"