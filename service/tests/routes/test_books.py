from fastapi.testclient import TestClient


# TODO: "Add response check"
def test_get_books(client: TestClient) -> None:
    response = client.get("/libraries/2/books")
    assert response.status_code == 200


def test_get_book(client: TestClient) -> None:
    response = client.get("/libraries/2/books/7")
    assert response.status_code == 200


def test_post_book(client: TestClient) -> None:
    response = client.post(
        "/libraries/2/books",
        headers={"Content-Type": "application/json"},
        json={
            "title": "Test Book",
            "author": "Test Author",
            "language": "Test Language",
        },
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"
    assert response.json()["author"] == "Test Author"
    assert response.json()["language"] == "Test Language"


def test_put_book(client: TestClient) -> None:
    response = client.put(
        "/libraries/2/books/7",
        headers={"Content-Type": "application/json"},
        json={
            "title": "Updated Test Book",
            "author": "Updated Test Author",
            "language": "Updated Test Language",
        },
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Book"
    assert response.json()["author"] == "Updated Test Author"
    assert response.json()["language"] == "Updated Test Language"


def test_delete_book(client: TestClient) -> None:
    books = client.get("/libraries/2/books")
    final_id: int = books.json()[-1]["id"]
    response = client.delete(f"/libraries/2/books/{final_id}")
    assert response.status_code == 204


def test_delete_book_not_found(client: TestClient) -> None:
    response = client.delete("/libraries/2/books/999")
    assert response.status_code == 404
