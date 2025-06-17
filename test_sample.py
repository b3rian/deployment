import pytest

@pytest.mark.parametrize("input_val,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input_val, expected):
    assert input_val ** 2 == expected

    
