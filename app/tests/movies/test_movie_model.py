import json

import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Sample Movie", genre="comedy", year="1995")
    movie.save()

    assert movie.title == "Sample Movie"
    assert movie.genre == "comedy"
    assert movie.year == "1995"
    assert movie.created_at
    assert movie.updated_at
    assert str(movie) == movie.title
