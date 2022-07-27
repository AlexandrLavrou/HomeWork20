from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    stuord = Director(id=1, name='stuord')
    bron = Director(id=2, name='bron')
    albert = Director(id=1, name='albert')

    director_dao.get_one = MagicMock(return_value=stuord)
    director_dao.get_all = MagicMock(return_value=[stuord, bron, albert])
    director_dao.create = MagicMock(return_value=Director(id=2))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        user = self.director_service.get_one(1)

        assert user is not None
        assert user.id is not None

    def test_get_all(self):
        users = self.director_service.get_all()

        assert len(users) > 0

    def test_create(self):
        user_data = {"name": "carlos"}
        user = self.director_service.create(user_data)

        assert user.id is not None

    def test_update(self):
        user_data = {"name": "carlos"}
        user = self.director_service.update(user_data)

        assert user.id is not None

    # def test_partially_update(self):
    #     user_data = {"name": "carlos"}
    #     user = self.director_service.partially_update(user_data)

        assert user.id is not None

    def test_delete(self):
        self.director_service.delete(1)
