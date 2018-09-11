import pytest
from calc import soma

def tesscalc():
	assert soma(1, 1) == 2
	assert soma(-1, 1) == 0
	assert soma('1', 1) == 2
	assert soma('-1', 1) == 0
	assert soma(1.5, 1) == 2.5
	assert soma('-1,5', 1) == -0.5
