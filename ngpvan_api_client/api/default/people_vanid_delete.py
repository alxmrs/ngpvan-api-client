from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.people_vanid_delete_response_400 import PeopleVanidDeleteResponse400
from ...types import Response


def _get_kwargs(
    van_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}".format(client.base_url, vanId=van_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PeopleVanidDeleteResponse400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = PeopleVanidDeleteResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PeopleVanidDeleteResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    van_id: int,
    *,
    client: Client,
) -> Response[Union[Any, PeopleVanidDeleteResponse400]]:
    """/people/{vanId}

     Suppresses a contact record

    Args:
        van_id (int):

    Returns:
        Response[Union[Any, PeopleVanidDeleteResponse400]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    van_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, PeopleVanidDeleteResponse400]]:
    """/people/{vanId}

     Suppresses a contact record

    Args:
        van_id (int):

    Returns:
        Response[Union[Any, PeopleVanidDeleteResponse400]]
    """

    return sync_detailed(
        van_id=van_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    van_id: int,
    *,
    client: Client,
) -> Response[Union[Any, PeopleVanidDeleteResponse400]]:
    """/people/{vanId}

     Suppresses a contact record

    Args:
        van_id (int):

    Returns:
        Response[Union[Any, PeopleVanidDeleteResponse400]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    van_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, PeopleVanidDeleteResponse400]]:
    """/people/{vanId}

     Suppresses a contact record

    Args:
        van_id (int):

    Returns:
        Response[Union[Any, PeopleVanidDeleteResponse400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
        )
    ).parsed
