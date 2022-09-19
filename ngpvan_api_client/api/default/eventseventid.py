from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.eventseventid_response_400 import EventseventidResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: int = 1631,
    *,
    client: Client,
    expand: Union[Unset, None, str] = "locations,codes",
) -> Dict[str, Any]:
    url = "{}/events/{eventId}".format(client.base_url, eventId=event_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$expand"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, EventseventidResponse400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = EventseventidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, EventseventidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_id: int = 1631,
    *,
    client: Client,
    expand: Union[Unset, None, str] = "locations,codes",
) -> Response[Union[Any, EventseventidResponse400]]:
    """/events/{eventId}

     Use this endpoint to retrieve the details of a specific Event.

    Use the [Signups](ref:signups#signups-1) endpoint to retrieve a list of the Event’s participants.

    Args:
        event_id (int):  Default: 1631.
        expand (Union[Unset, None, str]):  Default: 'locations,codes'.

    Returns:
        Response[Union[Any, EventseventidResponse400]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
        expand=expand,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    event_id: int = 1631,
    *,
    client: Client,
    expand: Union[Unset, None, str] = "locations,codes",
) -> Optional[Union[Any, EventseventidResponse400]]:
    """/events/{eventId}

     Use this endpoint to retrieve the details of a specific Event.

    Use the [Signups](ref:signups#signups-1) endpoint to retrieve a list of the Event’s participants.

    Args:
        event_id (int):  Default: 1631.
        expand (Union[Unset, None, str]):  Default: 'locations,codes'.

    Returns:
        Response[Union[Any, EventseventidResponse400]]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    event_id: int = 1631,
    *,
    client: Client,
    expand: Union[Unset, None, str] = "locations,codes",
) -> Response[Union[Any, EventseventidResponse400]]:
    """/events/{eventId}

     Use this endpoint to retrieve the details of a specific Event.

    Use the [Signups](ref:signups#signups-1) endpoint to retrieve a list of the Event’s participants.

    Args:
        event_id (int):  Default: 1631.
        expand (Union[Unset, None, str]):  Default: 'locations,codes'.

    Returns:
        Response[Union[Any, EventseventidResponse400]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_id: int = 1631,
    *,
    client: Client,
    expand: Union[Unset, None, str] = "locations,codes",
) -> Optional[Union[Any, EventseventidResponse400]]:
    """/events/{eventId}

     Use this endpoint to retrieve the details of a specific Event.

    Use the [Signups](ref:signups#signups-1) endpoint to retrieve a list of the Event’s participants.

    Args:
        event_id (int):  Default: 1631.
        expand (Union[Unset, None, str]):  Default: 'locations,codes'.

    Returns:
        Response[Union[Any, EventseventidResponse400]]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            expand=expand,
        )
    ).parsed
