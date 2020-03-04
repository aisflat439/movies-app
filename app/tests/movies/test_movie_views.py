from rest_framework import status
import pytest

from movies.models import Movie

MOVIES_URL = "/api/movies/"


@pytest.mark.django_db
def test_add_movie(client):
    """proper payload"""
    payload = {
        "title": "High Fidelity",
        "genre": "comedy",
        "year": "1999",
    }
    response = client.post(MOVIES_URL, payload)
    num_movies = Movie.objects.all()

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == payload["title"]
    assert num_movies.count() == 1


@pytest.mark.django_db
def test_add_movie_no_payload(client):
    """No payload object passed"""
    response = client.post(MOVIES_URL)
    num_movies = Movie.objects.all()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert num_movies.count() == 0


@pytest.mark.django_db
def test_add_movie_invalid_payload(client):
    """payload is missing a field"""
    payload = {
        "title": "High Fidelity",
        "genre": "comedy",
    }
    response = client.post(MOVIES_URL, payload)
    num_movies = Movie.objects.all()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert num_movies.count() == 0


@pytest.mark.django_db
def test_get_a_single_movie(client, add_movie):
    """get a single movie by title"""
    mock_movie = add_movie(title="High Fidelity", genre="comedy", year="1999",)

    response = client.get(f"{MOVIES_URL}{mock_movie.id}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "High Fidelity"
    assert response.data["genre"] == "comedy"
    assert response.data["year"] == "1999"


def test_get_a_single_movie_bad_id(client):
    """What happens if you try to get a movie with a whack id"""
    response = client.get(f"{MOVIES_URL}yolo/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    mock_movie_one = add_movie(title="High Fidelity", genre="comedy", year="1999",)
    mock_movie_two = add_movie(title="Big Lebowski", genre="comedy", year="1998",)

    response = client.get(MOVIES_URL)
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]["title"] == mock_movie_one.title
    assert response.data[1]["title"] == mock_movie_two.title
