import pytest
from unittest.mock import MagicMock

from demostration_solution.implemented import genre_dao
from demostration_solution.dao.model.genre import Genre


@pytest.fixture
def genre_dao():
    g1 = Genre(id=1, name='ha-ha')
    g2 = Genre(id=2, name='hi-hi')
    g3 = Genre(id=3, name='ho-ho')

    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])
    genre_dao.get_one = MagicMock(return_value=Genre(id=1))
    genre_dao.create = MagicMock(return_value=Genre(id=2))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao
