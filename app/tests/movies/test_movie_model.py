import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Big Lebowski", genre="comedy", year="1996")
    movie.save()
    assert movie.title == "Big Lebowski"
    assert movie.genre == "comedy"
    assert movie.year == "1996"
    assert movie.created_at
    assert movie.updated_at
    assert str(movie) == movie.title