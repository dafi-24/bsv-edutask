import pytest

import unittest.mock as mock

from src.controllers.usercontroller import UserController

@pytest.fixture
def obj():
    return [{"user":"calle"}, {"user":"anna"}]

@pytest.mark.unit
def test_checkmail_true(obj):

    mockedController = mock.MagicMock()
    mockedController.find.return_value = [obj[0]]

    controller = UserController(mockedController)

    assert controller.get_user_by_email("calle@hotmail.com") == obj[0]

@pytest.mark.unit
def test_checkmail_None():

    mockedController = mock.MagicMock()
    mockedController.find.return_value = [None]

    controller = UserController(mockedController)

    assert controller.get_user_by_email("calle@hotmail.com") == None

@pytest.mark.unit
def test_check_multiple_mail_true(obj):

    mockedController = mock.MagicMock()
    mockedController.find.return_value = [obj[0], obj[1]]

    controller = UserController(mockedController)

    assert controller.get_user_by_email("calle@hotmail.com") == obj[0]

@pytest.mark.unit
def test_check_multiple_mail_false(obj):

    mockedController = mock.MagicMock()
    mockedController.find.return_value = [obj[0], obj[1]]

    controller = UserController(mockedController)

    assert controller.get_user_by_email("calle@hotmail.com") != obj[1]

@pytest.mark.unit
def test_invalid_mail_at(obj):

    mockedController = mock.MagicMock()
    mockedController.find.return_value = [obj[0], obj[1]]

    controller = UserController(mockedController)

    with pytest.raises(ValueError):
        controller.get_user_by_email("callehotmail.com")

@pytest.mark.unit
def test_invalid_mail_dot(obj):

    mockedController = mock.MagicMock()
    mockedController.find.return_value = [obj[0], obj[1]]

    controller = UserController(mockedController)

    with pytest.raises(ValueError):
        controller.get_user_by_email("calle@hotmailcom")

@pytest.mark.unit
def test_no_mail(obj):

    mockedController = mock.MagicMock()
    mockedController.find.return_value = [obj[0], obj[1]]

    controller = UserController(mockedController)

    with pytest.raises(ValueError):
        controller.get_user_by_email("")

@pytest.mark.unit
def test_exception():

    mockedController = mock.MagicMock()
    mockedController.find.return_value = 1

    controller = UserController(mockedController)

    with pytest.raises(Exception):
        controller.get_user_by_email("calle@hotmail.com")
