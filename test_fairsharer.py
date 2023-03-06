import pytest
from fairsharer import fair_sharer

def test_fair_sharer():
    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 1)
    expected = [100, 800, 900, 0]
    assert result == expected, f"Unexpected result! Expected {expected}, but got {result}"

    values = [0, 1000, 800, 0]
    result = fair_sharer(values, 0)
    expected = 1000
    assert result[1] == expected, f"Unexpected result! Expected {expected}, but got {result}"
    
    values = [1000, 300, 800]
    result = fair_sharer(values, 3)
    expected = [712, 579, 809]
    assert result == expected, f"Unexpected result! Expected {expected}, but got {result}"
    
test_fair_sharer()
