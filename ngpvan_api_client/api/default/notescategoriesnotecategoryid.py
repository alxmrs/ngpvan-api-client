from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.notescategoriesnotecategoryid_response_400 import NotescategoriesnotecategoryidResponse400
from ...models.notescategoriesnotecategoryid_response_404 import NotescategoriesnotecategoryidResponse404
from ...types import Response


def _get_kwargs(
    note_category_id: int = 10,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/notes/categories/{noteCategoryId}".format(client.base_url, noteCategoryId=note_category_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = NotescategoriesnotecategoryidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = NotescategoriesnotecategoryidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    note_category_id: int = 10,
    *,
    client: Client,
) -> Response[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]:
    """/notes/categories/{noteCategoryId}

     Use this endpoint to retrieve a specific Note Category.

    Returns a standard [Note Category](ref:notes#common-models-26) object, if found.

    If the specified Note Category does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        note_category_id (int):  Default: 10.

    Returns:
        Response[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]
    """

    kwargs = _get_kwargs(
        note_category_id=note_category_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    note_category_id: int = 10,
    *,
    client: Client,
) -> Optional[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]:
    """/notes/categories/{noteCategoryId}

     Use this endpoint to retrieve a specific Note Category.

    Returns a standard [Note Category](ref:notes#common-models-26) object, if found.

    If the specified Note Category does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        note_category_id (int):  Default: 10.

    Returns:
        Response[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]
    """

    return sync_detailed(
        note_category_id=note_category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    note_category_id: int = 10,
    *,
    client: Client,
) -> Response[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]:
    """/notes/categories/{noteCategoryId}

     Use this endpoint to retrieve a specific Note Category.

    Returns a standard [Note Category](ref:notes#common-models-26) object, if found.

    If the specified Note Category does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        note_category_id (int):  Default: 10.

    Returns:
        Response[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]
    """

    kwargs = _get_kwargs(
        note_category_id=note_category_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    note_category_id: int = 10,
    *,
    client: Client,
) -> Optional[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]:
    """/notes/categories/{noteCategoryId}

     Use this endpoint to retrieve a specific Note Category.

    Returns a standard [Note Category](ref:notes#common-models-26) object, if found.

    If the specified Note Category does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        note_category_id (int):  Default: 10.

    Returns:
        Response[Union[Any, NotescategoriesnotecategoryidResponse400, NotescategoriesnotecategoryidResponse404]]
    """

    return (
        await asyncio_detailed(
            note_category_id=note_category_id,
            client=client,
        )
    ).parsed
