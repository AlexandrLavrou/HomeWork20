from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.movie import MovieDAO
from demostration_solution.dao.model.movie import Movie
from demostration_solution.service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(id=1,
                   title='Криминальное чтиво',
                   description='шикарный фильм',
                   trailer='где-то есть',
                   year=1990,
                   rating=10,
                   genre_id=6,
                   director_id=1)
    movie2 = Movie(id=2,
                   title='Рик и Морти',
                   description='шикарный мульт',
                   trailer='где-то есть',
                   year=2020,
                   rating=10,
                   genre_id=6,
                   director_id=9)

    movie3 = Movie(id=3,
                   title='Полярный',
                   description='шикарный фильмец',
                   trailer='на Нетфликс есть',
                   year=2020,
                   rating=10,
                   genre_id=5,
                   director_id=5)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_data = {
            "title": "Disentchantment",
            "description": "мульт",
            "trailer": "тоже на Нетфликс",
            "year": 2019,
            "rating": 9.9,
            "genre_id": 5,
            "director_id": 5
        }
        movie = self.movie_service.create(movie_data)

        assert movie is not None
        assert movie.id is not None

    def test_update(self):
        movie_data = {
            "title": "1408",
            "description": "шикарный хоррор все времен",
            "trailer": "где-то точно есть!",
            "year": 2010,
            "rating": 10.0,
            "genre_id": 1,
            "director_id": 3
        }
        movie = self.movie_service.update(movie_data)

        assert movie is not None
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)
