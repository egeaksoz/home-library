import pytest
from httpx import AsyncClient


# TODO: "Add response check"
@pytest.mark.asyncio
async def test_read_libraries(async_client: AsyncClient) -> None:
    response = await async_client.get("/libraries/")
    assert response.status_code == 200


# TODO: "Add response check"
@pytest.mark.asyncio
async def test_read_library(async_client: AsyncClient, request) -> None:
    response = await async_client.get(f"/libraries/{request.config.library_1_uuid}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_library_no_body(async_client: AsyncClient) -> None:
    response = await async_client.post("/libraries/")
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_library(async_client: AsyncClient) -> None:
    library = {"name": "test_library"}
    response = await async_client.post(
        "/libraries/", headers={"Content-Type": "application/json"}, json=library
    )
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_update_library(async_client: AsyncClient, request) -> None:
    new_library = {"name": "new_test_library"}
    response = await async_client.put(
        f"/libraries/{request.config.library_1_uuid}",
        headers={"Content-Type": "application/json"},
        json=new_library,
    )
    assert response.status_code == 200
    new_library_name: str = response.json()["name"]
    assert new_library_name == "new_test_library"


@pytest.mark.asyncio
async def test_delete_library(async_client: AsyncClient, request) -> None:
    response = await async_client.delete(f"/libraries/{request.config.library_2_uuid}")
    assert response.status_code == 204
