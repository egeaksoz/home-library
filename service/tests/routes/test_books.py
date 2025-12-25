import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_books(async_client: AsyncClient, request) -> None:
    response = await async_client.get(
        f"/libraries/{request.config.library_1_uuid}/books/"
    )
    assert response.status_code == 200
    assert len(response.json()) == 3


@pytest.mark.asyncio
async def test_get_book(async_client: AsyncClient, request) -> None:
    response = await async_client.get(
        f"/libraries/{request.config.library_1_uuid}/books/{request.config.book_1_uuid}"
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_post_book(async_client: AsyncClient, request) -> None:
    response = await async_client.post(
        f"/libraries/{request.config.library_1_uuid}/books/",
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
async def test_put_book(async_client: AsyncClient, request) -> None:
    response = await async_client.put(
        f"/libraries/{request.config.library_1_uuid}/books/{request.config.book_1_uuid}",
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
async def test_delete_book(async_client: AsyncClient, request) -> None:
    response = await async_client.delete(
        f"/libraries/{request.config.library_1_uuid}/books/{request.config.book_3_uuid}"
    )
    assert response.status_code == 204


@pytest.mark.asyncio
async def test_delete_book_not_found(async_client: AsyncClient, request) -> None:
    response = await async_client.delete(
        f"/libraries/{request.config.library_2_uuid}/books/a713c349-1ab5-4bc1-be78-f5fa147b116f"
    )
    assert response.status_code == 404
