import pytest
from calculator import add, multiply

def test_add():
    assert add(5, 3) == 5
    assert add(9, 2) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0