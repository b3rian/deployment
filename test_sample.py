import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_is_positive(number):
    assert number > 0


    
