from fastapi.testclient import TestClient


# TODO: "Add response check"
def test_get_books(client: TestClient) -> None:
    response = client.get("/libraries/1/books")
    assert response.status_code == 200
