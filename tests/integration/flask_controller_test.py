import pytest

from main import app


@pytest.fixture
def get_flask_client():
    app.config.update({"TESTING": True})

    with app.test_client() as get_flask_client:
        yield get_flask_client


def test_flask_controller_home_route(get_flask_client):
    response = get_flask_client.get("/")
    assert response.status_code == 200
