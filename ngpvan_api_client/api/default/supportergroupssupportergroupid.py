from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.supportergroupssupportergroupid_response_400 import SupportergroupssupportergroupidResponse400
from ...types import Response


def _get_kwargs(
    supporter_group_id: int = 1234,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/supporterGroups/{supporterGroupId}".format(client.base_url, supporterGroupId=supporter_group_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, SupportergroupssupportergroupidResponse400]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = SupportergroupssupportergroupidResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, SupportergroupssupportergroupidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    supporter_group_id: int = 1234,
    *,
    client: Client,
) -> Response[Union[Any, SupportergroupssupportergroupidResponse400]]:
    """/supporterGroups/{supporterGroupId}

     Use this endpoint to delete a supporter group. Deleting a supporter group will also remove every
    member from it.

    If successful, the endpoint responds with HTTP Status Code `204 No Content`.

    Args:
        supporter_group_id (int):  Default: 1234.

    Returns:
        Response[Union[Any, SupportergroupssupportergroupidResponse400]]
    """

    kwargs = _get_kwargs(
        supporter_group_id=supporter_group_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    supporter_group_id: int = 1234,
    *,
    client: Client,
) -> Optional[Union[Any, SupportergroupssupportergroupidResponse400]]:
    """/supporterGroups/{supporterGroupId}

     Use this endpoint to delete a supporter group. Deleting a supporter group will also remove every
    member from it.

    If successful, the endpoint responds with HTTP Status Code `204 No Content`.

    Args:
        supporter_group_id (int):  Default: 1234.

    Returns:
        Response[Union[Any, SupportergroupssupportergroupidResponse400]]
    """

    return sync_detailed(
        supporter_group_id=supporter_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    supporter_group_id: int = 1234,
    *,
    client: Client,
) -> Response[Union[Any, SupportergroupssupportergroupidResponse400]]:
    """/supporterGroups/{supporterGroupId}

     Use this endpoint to delete a supporter group. Deleting a supporter group will also remove every
    member from it.

    If successful, the endpoint responds with HTTP Status Code `204 No Content`.

    Args:
        supporter_group_id (int):  Default: 1234.

    Returns:
        Response[Union[Any, SupportergroupssupportergroupidResponse400]]
    """

    kwargs = _get_kwargs(
        supporter_group_id=supporter_group_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    supporter_group_id: int = 1234,
    *,
    client: Client,
) -> Optional[Union[Any, SupportergroupssupportergroupidResponse400]]:
    """/supporterGroups/{supporterGroupId}

     Use this endpoint to delete a supporter group. Deleting a supporter group will also remove every
    member from it.

    If successful, the endpoint responds with HTTP Status Code `204 No Content`.

    Args:
        supporter_group_id (int):  Default: 1234.

    Returns:
        Response[Union[Any, SupportergroupssupportergroupidResponse400]]
    """

    return (
        await asyncio_detailed(
            supporter_group_id=supporter_group_id,
            client=client,
        )
    ).parsed
