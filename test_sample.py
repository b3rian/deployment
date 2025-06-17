import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_is_even(number):
    assert number % 2 == 0  # Will fail for 1 and 3

    
