from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.supportergroupssupportergroupid_1_response_200 import Supportergroupssupportergroupid1Response200
from ...models.supportergroupssupportergroupid_1_response_400 import Supportergroupssupportergroupid1Response400
from ...models.supportergroupssupportergroupid_1_response_404 import Supportergroupssupportergroupid1Response404
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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[
        Supportergroupssupportergroupid1Response200,
        Supportergroupssupportergroupid1Response400,
        Supportergroupssupportergroupid1Response404,
    ]
]:
    if response.status_code == 200:
        response_200 = Supportergroupssupportergroupid1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Supportergroupssupportergroupid1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Supportergroupssupportergroupid1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        Supportergroupssupportergroupid1Response200,
        Supportergroupssupportergroupid1Response400,
        Supportergroupssupportergroupid1Response404,
    ]
]:
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
) -> Response[
    Union[
        Supportergroupssupportergroupid1Response200,
        Supportergroupssupportergroupid1Response400,
        Supportergroupssupportergroupid1Response404,
    ]
]:
    """/supporterGroups/{supporterGroupId}

     Use this endpoint to retrieve a supporter group.

    Args:
        supporter_group_id (int):  Default: 1234.

    Returns:
        Response[Union[Supportergroupssupportergroupid1Response200, Supportergroupssupportergroupid1Response400, Supportergroupssupportergroupid1Response404]]
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
) -> Optional[
    Union[
        Supportergroupssupportergroupid1Response200,
        Supportergroupssupportergroupid1Response400,
        Supportergroupssupportergroupid1Response404,
    ]
]:
    """/supporterGroups/{supporterGroupId}

     Use this endpoint to retrieve a supporter group.

    Args:
        supporter_group_id (int):  Default: 1234.

    Returns:
        Response[Union[Supportergroupssupportergroupid1Response200, Supportergroupssupportergroupid1Response400, Supportergroupssupportergroupid1Response404]]
    """

    return sync_detailed(
        supporter_group_id=supporter_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    supporter_group_id: int = 1234,
    *,
    client: Client,
) -> Response[
    Union[
        Supportergroupssupportergroupid1Response200,
        Supportergroupssupportergroupid1Response400,
        Supportergroupssupportergroupid1Response404,
    ]
]:
    """/supporterGroups/{supporterGroupId}

     Use this endpoint to retrieve a supporter group.

    Args:
        supporter_group_id (int):  Default: 1234.

    Returns:
        Response[Union[Supportergroupssupportergroupid1Response200, Supportergroupssupportergroupid1Response400, Supportergroupssupportergroupid1Response404]]
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
) -> Optional[
    Union[
        Supportergroupssupportergroupid1Response200,
        Supportergroupssupportergroupid1Response400,
        Supportergroupssupportergroupid1Response404,
    ]
]:
    """/supporterGroups/{supporterGroupId}

     Use this endpoint to retrieve a supporter group.

    Args:
        supporter_group_id (int):  Default: 1234.

    Returns:
        Response[Union[Supportergroupssupportergroupid1Response200, Supportergroupssupportergroupid1Response400, Supportergroupssupportergroupid1Response404]]
    """

    return (
        await asyncio_detailed(
            supporter_group_id=supporter_group_id,
            client=client,
        )
    ).parsed
