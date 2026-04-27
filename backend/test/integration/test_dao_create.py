import pytest

from unittest.mock import patch
from pymongo.errors import WriteError
from src.util.dao import DAO


@pytest.fixture
def dao_test():
    with patch("src.util.dao.getValidator") as mock_validator_function:
        mock_validator_function.return_value = {
                    "$jsonSchema": {
                        "bsonType": "object",
                        "required": ["name", "email"],
                        "properties": {
                            "name": {
                                "bsonType": "string"
                            },
                            "email": {
                                "bsonType": "string",
                                "uniqueItems": True
                            },
                            "seen": {
                                "bsonType": "bool"
                            }

                        }
                    }
                }

        dao = DAO("edu_test")

        dao.collection.delete_many({})

        yield dao

        dao.collection.delete_many({})
        dao.collection.drop()

@pytest.mark.integration
def test_dao_create_success(dao_test):

    result = dao_test.create({"name": "calle", "email": "calle@hotmail.com", "seen": True, })

    assert "_id" in result


@pytest.mark.integration
def test_dao_create_without_required_field(dao_test):

    with pytest.raises(WriteError):

        dao_test.create({"name": "calle", "seen": True})


@pytest.mark.integration
def test_dao_create_int_on_string(dao_test):

    with pytest.raises(WriteError):

        dao_test.create({"name": 123, "email": "calle@hotmail.com", "seen": True })

@pytest.mark.integration
def test_dao_create_object_on_string(dao_test):

    with pytest.raises(WriteError):

        dao_test.create({"name": {"video": "Pokemon"}, "email": "calle@hotmail.com", "seen": True })

@pytest.mark.integration
def test_dao_create_string_on_boolean(dao_test):

    with pytest.raises(WriteError):

        dao_test.create({"name": {"video": "Pokemon"}, "email": "calle@hotmail.com", "seen": "True"})


@pytest.mark.integration
def test_dao_create_int_on_boolean(dao_test):

    with pytest.raises(WriteError):

        dao_test.create({"name": {"video": "Pokemon"}, "email": "calle@hotmail.com", "seen": 1})


@pytest.mark.integration
def test_dao_create_wrong_declaration(dao_test):

    with pytest.raises(WriteError):

        dao_test.create({"name": "kalle", "email": "calle@hotmail.com", "seen": [True, False, True] })


@pytest.mark.integration
def test_dao_create_duplicate_email(dao_test):
    
    with pytest.raises(WriteError):

        dao_test.create({"name": "calle", "email": "calle@hotmail.com", "seen": True, })
        dao_test.create({"name": "palle", "email": "calle@hotmail.com", "seen": True, })