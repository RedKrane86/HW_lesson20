import pytest
from unittest.mock import MagicMock

from demostration_solution.implemented import movie_dao
from demostration_solution.dao.model.movie import Movie


@pytest.fixture
def movie_dao():
    m1 = Movie(
        id=1,
        title='movie1',
        description='movie1 description',
        trailer='movie1 trailer',
        year=2021,
        rating=11,
        genre_id=1,
        director_id=1
        )
    m2 = Movie(
        id=2,
        title='movie2',
        description='movie2 description',
        trailer='movie2 trailer',
        year=2022,
        rating=12,
        genre_id=2,
        director_id=2
    )
    m3 = Movie(
        id=3,
        title='movie3',
        description='movie3 description',
        trailer='movie3 trailer',
        year=2023,
        rating=13,
        genre_id=3,
        director_id=3
    )

    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.get_one = MagicMock(return_value=Movie(id=1))
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao