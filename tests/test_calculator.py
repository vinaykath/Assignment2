'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiply():
    '''Testing if Multiplication works'''
    assert multiply(2,2) ==4

def test_divide():
    '''Testing if division works'''
    assert divide(2,2) ==1