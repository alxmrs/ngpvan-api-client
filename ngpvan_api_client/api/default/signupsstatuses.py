from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.signupsstatuses_response_200_item import SignupsstatusesResponse200Item
from ...models.signupsstatuses_response_400 import SignupsstatusesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    event_id: Union[Unset, None, int] = UNSET,
    event_type_id: Union[Unset, None, int] = 143856,
) -> Dict[str, Any]:
    url = "{}/signups/statuses".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["eventId"] = event_id

    params["eventTypeId"] = event_type_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SignupsstatusesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = SignupsstatusesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    event_id: Union[Unset, None, int] = UNSET,
    event_type_id: Union[Unset, None, int] = 143856,
) -> Response[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]:
    """/signups/statuses

     Use this endpoint to retrieve all valid Signup Statuses for a given Event or for any
    [Event](ref:events) of a given [Event Type](ref:event-types).

    The information returned by this endpoint changes only as frequently as an Event Type changes (which
    is typically not very often in production). Consider caching the results of this endpoint.

    Args:
        event_id (Union[Unset, None, int]):
        event_type_id (Union[Unset, None, int]):  Default: 143856.

    Returns:
        Response[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        event_id=event_id,
        event_type_id=event_type_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    event_id: Union[Unset, None, int] = UNSET,
    event_type_id: Union[Unset, None, int] = 143856,
) -> Optional[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]:
    """/signups/statuses

     Use this endpoint to retrieve all valid Signup Statuses for a given Event or for any
    [Event](ref:events) of a given [Event Type](ref:event-types).

    The information returned by this endpoint changes only as frequently as an Event Type changes (which
    is typically not very often in production). Consider caching the results of this endpoint.

    Args:
        event_id (Union[Unset, None, int]):
        event_type_id (Union[Unset, None, int]):  Default: 143856.

    Returns:
        Response[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]
    """

    return sync_detailed(
        client=client,
        event_id=event_id,
        event_type_id=event_type_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    event_id: Union[Unset, None, int] = UNSET,
    event_type_id: Union[Unset, None, int] = 143856,
) -> Response[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]:
    """/signups/statuses

     Use this endpoint to retrieve all valid Signup Statuses for a given Event or for any
    [Event](ref:events) of a given [Event Type](ref:event-types).

    The information returned by this endpoint changes only as frequently as an Event Type changes (which
    is typically not very often in production). Consider caching the results of this endpoint.

    Args:
        event_id (Union[Unset, None, int]):
        event_type_id (Union[Unset, None, int]):  Default: 143856.

    Returns:
        Response[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        event_id=event_id,
        event_type_id=event_type_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    event_id: Union[Unset, None, int] = UNSET,
    event_type_id: Union[Unset, None, int] = 143856,
) -> Optional[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]:
    """/signups/statuses

     Use this endpoint to retrieve all valid Signup Statuses for a given Event or for any
    [Event](ref:events) of a given [Event Type](ref:event-types).

    The information returned by this endpoint changes only as frequently as an Event Type changes (which
    is typically not very often in production). Consider caching the results of this endpoint.

    Args:
        event_id (Union[Unset, None, int]):
        event_type_id (Union[Unset, None, int]):  Default: 143856.

    Returns:
        Response[Union[List[SignupsstatusesResponse200Item], SignupsstatusesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            event_id=event_id,
            event_type_id=event_type_id,
        )
    ).parsed
