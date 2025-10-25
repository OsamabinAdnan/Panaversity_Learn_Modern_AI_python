import pytest
from CalculatorClass import Calculator
#from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6

def test_divide(calc):
    assert calc.divide(6, 3) == 2

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(6, 0)


#calc1 = calc()

#test_add()
# test_subtract(calc)
# test_multiply(calc)
# test_divide(calc)
# test_divide_by_zero(calc)


# Instead of directly calling test_add(), run tests using pytest
# This will ensure that the fixture is used to provide the 'calc' argument
if __name__ == '__main__':
    pytest.main(['-v']) # Remove arguments to let pytest discover tests automatically