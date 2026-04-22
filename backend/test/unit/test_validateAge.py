import pytest
import unittest.mock as mock

from src.util.helpers import ValidationHelper


@pytest.mark.parametrize('age, expected', [
    (-1, "invalid"), (0, "underaged"), (1, "underaged"),
    (17, "underaged"), (18, "valid"), (19, "valid"),
    (119, "valid"), (120, "valid"), (121, "invalid")
])

@pytest.mark.unit
def test_ageValidation(age, expected):

    mockedUserController = mock.MagicMock()
    mockedUserController.get.return_value = {"age": age}

    obj = ValidationHelper(mockedUserController)
    result = obj.validateAge(None)

    assert result == expected
