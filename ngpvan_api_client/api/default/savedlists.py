from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.savedlists_response_400 import SavedlistsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    folder_id: Union[Unset, None, int] = 1234,
    max_door_count: Union[Unset, None, int] = 1000,
    max_people_count: Union[Unset, None, int] = 2000,
) -> Dict[str, Any]:
    url = "{}/savedLists".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["folderId"] = folder_id

    params["maxDoorCount"] = max_door_count

    params["maxPeopleCount"] = max_people_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, SavedlistsResponse400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = SavedlistsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, SavedlistsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    folder_id: Union[Unset, None, int] = 1234,
    max_door_count: Union[Unset, None, int] = 1000,
    max_people_count: Union[Unset, None, int] = 2000,
) -> Response[Union[Any, SavedlistsResponse400]]:
    """/savedLists

     Use this endpoint to retrieve metadata about available Saved Lists. The list of people in a Saved
    List is not available via this endpoint.

    Args:
        folder_id (Union[Unset, None, int]):  Default: 1234.
        max_door_count (Union[Unset, None, int]):  Default: 1000.
        max_people_count (Union[Unset, None, int]):  Default: 2000.

    Returns:
        Response[Union[Any, SavedlistsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        folder_id=folder_id,
        max_door_count=max_door_count,
        max_people_count=max_people_count,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    folder_id: Union[Unset, None, int] = 1234,
    max_door_count: Union[Unset, None, int] = 1000,
    max_people_count: Union[Unset, None, int] = 2000,
) -> Optional[Union[Any, SavedlistsResponse400]]:
    """/savedLists

     Use this endpoint to retrieve metadata about available Saved Lists. The list of people in a Saved
    List is not available via this endpoint.

    Args:
        folder_id (Union[Unset, None, int]):  Default: 1234.
        max_door_count (Union[Unset, None, int]):  Default: 1000.
        max_people_count (Union[Unset, None, int]):  Default: 2000.

    Returns:
        Response[Union[Any, SavedlistsResponse400]]
    """

    return sync_detailed(
        client=client,
        folder_id=folder_id,
        max_door_count=max_door_count,
        max_people_count=max_people_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    folder_id: Union[Unset, None, int] = 1234,
    max_door_count: Union[Unset, None, int] = 1000,
    max_people_count: Union[Unset, None, int] = 2000,
) -> Response[Union[Any, SavedlistsResponse400]]:
    """/savedLists

     Use this endpoint to retrieve metadata about available Saved Lists. The list of people in a Saved
    List is not available via this endpoint.

    Args:
        folder_id (Union[Unset, None, int]):  Default: 1234.
        max_door_count (Union[Unset, None, int]):  Default: 1000.
        max_people_count (Union[Unset, None, int]):  Default: 2000.

    Returns:
        Response[Union[Any, SavedlistsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        folder_id=folder_id,
        max_door_count=max_door_count,
        max_people_count=max_people_count,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    folder_id: Union[Unset, None, int] = 1234,
    max_door_count: Union[Unset, None, int] = 1000,
    max_people_count: Union[Unset, None, int] = 2000,
) -> Optional[Union[Any, SavedlistsResponse400]]:
    """/savedLists

     Use this endpoint to retrieve metadata about available Saved Lists. The list of people in a Saved
    List is not available via this endpoint.

    Args:
        folder_id (Union[Unset, None, int]):  Default: 1234.
        max_door_count (Union[Unset, None, int]):  Default: 1000.
        max_people_count (Union[Unset, None, int]):  Default: 2000.

    Returns:
        Response[Union[Any, SavedlistsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            folder_id=folder_id,
            max_door_count=max_door_count,
            max_people_count=max_people_count,
        )
    ).parsed
