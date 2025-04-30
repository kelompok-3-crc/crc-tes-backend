import pytest
from app import add, multiply

def test_add():
    assert add(5, 3) == 8
    assert add(9, 2) == 11

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0