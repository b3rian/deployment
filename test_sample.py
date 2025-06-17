import pytest

@pytest.fixture(params=[1, 2])
def x(request):
    return request.param

@pytest.fixture(params=[10, 20])
def y(request):
    return request.param

def test_multiplication(x, y):
    assert x * y >= 10


    
