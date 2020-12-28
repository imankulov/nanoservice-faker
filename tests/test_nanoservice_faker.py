import pytest
from fastapi.testclient import TestClient

from nanoservice_faker.app import app
from nanoservice_faker.custom_types import all_methods

client = TestClient(app)


@pytest.mark.parametrize("method", all_methods())
def test_method(method):
    response = client.get(f"/gen/{method}")
    assert response.status_code == 200
    assert len(response.json()) == 10
