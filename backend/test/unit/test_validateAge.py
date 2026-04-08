import pytest
import unittest.mock as mock

from src.util.helpers import ValidationHelper


@pytest.mark.unit
def test_ageValidation():
    

    #create a mock object
    mockedusercontroller = mock.MagicMock()
    mockedusercontroller.get.return_value = {'age': 18}

    obj = ValidationHelper(mockedusercontroller)
    result = obj.validateAge(userid=1)

    assert result == "underaged"
    
    #test validate age mocked object

# @pytest.mark.unit
# def