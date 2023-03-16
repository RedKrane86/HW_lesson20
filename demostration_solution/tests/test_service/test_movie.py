import pytest

from demostration_solution.tests.test_dao.test_movie import movie_dao
from demostration_solution.service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, m_dao=movie_dao):
        self.movie_service = MovieService(dao= m_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_data = {
            "title": 'movie1',
            "description": 'movie1 description',
            "trailer": 'movie1 trailer',
            "year": 2023,
            "rating": 13,
            "genre_id": 1,
            "director_id": 1
        }
        movie = self.movie_service.create(movie_data)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_data = {
            "id": 1,
            "title": 'movie1',
            "description": 'movie1 description',
            "trailer": 'movie1 trailer',
            "year": 2023,
            "rating": 13,
            "genre_id": 1,
            "director_id": 1
        }
        self.movie_service.update(movie_data)
