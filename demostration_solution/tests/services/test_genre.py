from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    horror = Genre(id=1, name='horror')
    mistic = Genre(id=2, name='mictic')
    comedy = Genre(id=3, name='comedy')

    genre_dao.get_one = MagicMock(return_value=horror)
    genre_dao.get_all = MagicMock(return_value=[horror, mistic, comedy])
    genre_dao.create = MagicMock(return_value=Genre(id=2))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        genre_data = {"name": "drama"}
        genre = self.genre_service.create(genre_data)

        assert genre.id is not None

    def test_update(self):
        genre_data = {"name": "carlos"}
        genre = self.genre_service.update(genre_data)

        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)
