import pytest
from unittest.mock import MagicMock

from demostration_solution.implemented import director_dao
from demostration_solution.dao.model.director import Director

@pytest.fixture
def director_dao():
    john = Director(id=1, name='john')
    kate = Director(id=2, name='kate')
    jack = Director(id=3, name='jack')

    director_dao.get_all = MagicMock(return_value=[john, kate, jack])
    director_dao.get_one = MagicMock(return_value=Director(id=1))
    director_dao.create = MagicMock(return_value=Director(id=2))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao
