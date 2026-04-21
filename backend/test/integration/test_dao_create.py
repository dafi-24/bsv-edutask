import pytest

from unittest.mock import patch
from src.util.dao import DAO


@pytest.fixture
def dao_test():
    with patch("src.util.dao.getValidator") as mock_validator_function:
        mock_validator_function.return_value = {
                    "$jsonSchema": {
                        "bsonType": "object",
                        "required": ["name", "seen"],
                        "properties": {
                            "name": {
                                "bsonType": "string"
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


def test_dao_create_success(dao_test):

    result = dao_test.create({"name": "calle", "seen": True})

    assert result["_id"]