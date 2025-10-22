from fastapi.testclient import TestClient

# TODO: "Add response check"
def test_read_libraries(client: TestClient) -> None:
    response = client.get("/libraries")
    assert response.status_code == 200
