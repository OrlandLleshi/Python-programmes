import pytest
import programs.count as pc

def test_count_zeros():
    assert pc.count([0,0,0], 0) == 3

def test_count_string():
    assert pc.count(["a","a","a"], "a") == 3

def test_count_minus():
	assert count.count([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert count.count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2
