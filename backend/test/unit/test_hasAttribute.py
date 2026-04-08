import pytest
from src.util.helpers import hasAttribute

@pytest.fixture
def obj():
    return {"name": "jane"}

@pytest.mark.unit
def test_hasAttribute(obj):
    result = hasAttribute(obj, "name")

    assert result == True

@pytest.mark.unit
def test_hasAttribute_false(obj):
    result = hasAttribute(obj, "age")

    assert result == False
