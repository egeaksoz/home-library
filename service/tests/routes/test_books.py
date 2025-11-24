import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_books(async_client: AsyncClient) -> None:
    response = await async_client.get("/libraries/5/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3


@pytest.mark.asyncio
async def test_get_book(async_client: AsyncClient) -> None:
    response = await async_client.get("/libraries/5/books/5")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_book(async_client: AsyncClient) -> None:
    response = await async_client.post(
        "/libraries/5/books/",
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


@pytest.mark.asyncio
async def test_put_book(async_client: AsyncClient) -> None:
    response = await async_client.put(
        "/libraries/5/books/6",
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


@pytest.mark.asyncio
async def test_delete_book(async_client: AsyncClient) -> None:
    response = await async_client.delete("/libraries/2/books/7")
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_book_not_found(async_client: AsyncClient) -> None:
    response = await async_client.delete("/libraries/5/books/999")
    assert response.status_code == 404
