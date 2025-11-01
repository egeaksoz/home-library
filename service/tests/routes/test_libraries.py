from fastapi.testclient import TestClient


# TODO: "Add response check"
def test_read_libraries(client: TestClient) -> None:
    response = client.get("/libraries")
    assert response.status_code == 200


# TODO: "Add response check"
def test_read_library(client: TestClient) -> None:
    response = client.get("/libraries/1")
    assert response.status_code == 200


def test_create_library_no_body(client: TestClient) -> None:
    response = client.post("/libraries")
    assert response.status_code == 422


def test_create_library(client: TestClient) -> None:
    library = {"name": "test_library"}
    response = client.post(
        "/libraries", headers={"Content-Type": "application/json"}, json=library
    )
    assert response.status_code == 201


def test_update_library(client: TestClient) -> None:
    new_library = {"name": "new_test_library"}
    response = client.put(
        "/libraries/1", headers={"Content-Type": "application/json"}, json=new_library
    )
    assert response.status_code == 200
    new_library_name: str = response.json()["name"]
    assert new_library_name == "new_test_library"


def test_delete_library(client: TestClient) -> None:
    all_libraries = client.get("/libraries")
    final_id: int = all_libraries.json()[-1]["id"]
    response = client.delete(f"/libraries/{final_id}")
    assert response.status_code == 204
