import pytest

from demostration_solution.tests.test_dao.test_director import director_dao
from demostration_solution.service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, d_dao=director_dao):
        self.director_service = DirectorService(dao= d_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_data = {
            "name": "John"
        }
        director = self.director_service.create(director_data)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_data = {
            "id": 1,
            "name": "John"
        }
        self.director_service.update(director_data)