import pytest
from calculator import add, divide, is_prime_number

@pytest.mark.parametrize("a,b,expected", [(0,0,0),(-4,7,3),(0.1,0.2,0.3)])
def test_add(a,b,expected):
    assert add(a,b) == pytest.approx(expected)

@pytest.mark.parametrize("a,b,expected", [(0,3,0),(-9,3,-3),(7,2,3.5)])
def test_divide(a,b,expected):
    assert divide(a,b) == pytest.approx(expected)

@pytest.mark.parametrize("divisor", [0,0.0])
def test_zero_divisor(divisor):
    with pytest.raises(ZeroDivisionError, match="Делитель"):
        divide(1,divisor)

@pytest.mark.parametrize("n,expected", [(-3,False),(0,False),(1,False),(2,True),
    (11,True),(49,False),(91,False),(97,True)])
def test_prime(n,expected):
    assert is_prime_number(n) is expected

@pytest.mark.parametrize("n", [True,3.5])
def test_prime_type(n):
    with pytest.raises(TypeError):
        is_prime_number(n)
