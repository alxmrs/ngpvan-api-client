from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.savedlistssavedlistid_response_200 import SavedlistssavedlistidResponse200
from ...models.savedlistssavedlistid_response_400 import SavedlistssavedlistidResponse400
from ...models.savedlistssavedlistid_response_404 import SavedlistssavedlistidResponse404
from ...types import Response


def _get_kwargs(
    saved_list_id: int = 123,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/savedLists/{savedListId}".format(client.base_url, savedListId=saved_list_id)

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
) -> Optional[
    Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]
]:
    if response.status_code == 200:
        response_200 = SavedlistssavedlistidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = SavedlistssavedlistidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = SavedlistssavedlistidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    saved_list_id: int = 123,
    *,
    client: Client,
) -> Response[
    Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]
]:
    """/savedLists/{savedListId}

     Use this endpoint to get metadata about a saved list.

    Returns a standard [Saved List](ref:saved-lists#common-models-29) object, if found.

    If the specified Saved List does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        saved_list_id (int):  Default: 123.

    Returns:
        Response[Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]]
    """

    kwargs = _get_kwargs(
        saved_list_id=saved_list_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    saved_list_id: int = 123,
    *,
    client: Client,
) -> Optional[
    Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]
]:
    """/savedLists/{savedListId}

     Use this endpoint to get metadata about a saved list.

    Returns a standard [Saved List](ref:saved-lists#common-models-29) object, if found.

    If the specified Saved List does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        saved_list_id (int):  Default: 123.

    Returns:
        Response[Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]]
    """

    return sync_detailed(
        saved_list_id=saved_list_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    saved_list_id: int = 123,
    *,
    client: Client,
) -> Response[
    Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]
]:
    """/savedLists/{savedListId}

     Use this endpoint to get metadata about a saved list.

    Returns a standard [Saved List](ref:saved-lists#common-models-29) object, if found.

    If the specified Saved List does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        saved_list_id (int):  Default: 123.

    Returns:
        Response[Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]]
    """

    kwargs = _get_kwargs(
        saved_list_id=saved_list_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    saved_list_id: int = 123,
    *,
    client: Client,
) -> Optional[
    Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]
]:
    """/savedLists/{savedListId}

     Use this endpoint to get metadata about a saved list.

    Returns a standard [Saved List](ref:saved-lists#common-models-29) object, if found.

    If the specified Saved List does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        saved_list_id (int):  Default: 123.

    Returns:
        Response[Union[SavedlistssavedlistidResponse200, SavedlistssavedlistidResponse400, SavedlistssavedlistidResponse404]]
    """

    return (
        await asyncio_detailed(
            saved_list_id=saved_list_id,
            client=client,
        )
    ).parsed
