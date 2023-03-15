import pytest

from demostration_solution.tests.test_dao.test_genre import genre_dao
from demostration_solution.service.genre import GenreService
class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, g_dao=genre_dao):
        self.genre_service = GenreService(dao= g_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_data = {
            "name": "ha-ha"
        }
        genre = self.genre_service.create(genre_data)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_data = {
            "id": 1,
            "name": "ha-ha"
        }
        self.genre_service.update(genre_data)