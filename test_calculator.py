from calculator import add, divide, subtract

def test_add():
    assert add(2, 3) == 5
    
def test_subtract():
    assert subtract(5, 2) == 3

def test_divide_by_non_zero():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Expected an exception for division by zero"
    except ValueError:
        pass  # Expected