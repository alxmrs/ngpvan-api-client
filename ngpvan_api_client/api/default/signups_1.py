from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.signups_1_response_400 import Signups1Response400
from ...models.signups_1_response_404 import Signups1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    event_id: Union[Unset, None, int] = UNSET,
    van_id: Union[Unset, None, str] = "100476252",
) -> Dict[str, Any]:
    url = "{}/signups".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["eventId"] = event_id

    params["vanId"] = van_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Signups1Response400, Signups1Response404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = Signups1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = Signups1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Signups1Response400, Signups1Response404]]:
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
    van_id: Union[Unset, None, str] = "100476252",
) -> Response[Union[Any, Signups1Response400, Signups1Response404]]:
    """/signups

     Use this endpoint to find all of a Person’s Signups (across all Events) or to find all of the
    Signups for a specific Event.

    Either the `eventId` parameter, or the `vanId` parameter, *must* be specified.

    If `vanId` is specified but the Person is not accessible, this endpoint will return an error with
    HTTP Status Code `403 Forbidden`.

    If `vanId` is specified but the Person does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    If `eventId` is specified but the Event does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        event_id (Union[Unset, None, int]):
        van_id (Union[Unset, None, str]):  Default: '100476252'.

    Returns:
        Response[Union[Any, Signups1Response400, Signups1Response404]]
    """

    kwargs = _get_kwargs(
        client=client,
        event_id=event_id,
        van_id=van_id,
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
    van_id: Union[Unset, None, str] = "100476252",
) -> Optional[Union[Any, Signups1Response400, Signups1Response404]]:
    """/signups

     Use this endpoint to find all of a Person’s Signups (across all Events) or to find all of the
    Signups for a specific Event.

    Either the `eventId` parameter, or the `vanId` parameter, *must* be specified.

    If `vanId` is specified but the Person is not accessible, this endpoint will return an error with
    HTTP Status Code `403 Forbidden`.

    If `vanId` is specified but the Person does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    If `eventId` is specified but the Event does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        event_id (Union[Unset, None, int]):
        van_id (Union[Unset, None, str]):  Default: '100476252'.

    Returns:
        Response[Union[Any, Signups1Response400, Signups1Response404]]
    """

    return sync_detailed(
        client=client,
        event_id=event_id,
        van_id=van_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    event_id: Union[Unset, None, int] = UNSET,
    van_id: Union[Unset, None, str] = "100476252",
) -> Response[Union[Any, Signups1Response400, Signups1Response404]]:
    """/signups

     Use this endpoint to find all of a Person’s Signups (across all Events) or to find all of the
    Signups for a specific Event.

    Either the `eventId` parameter, or the `vanId` parameter, *must* be specified.

    If `vanId` is specified but the Person is not accessible, this endpoint will return an error with
    HTTP Status Code `403 Forbidden`.

    If `vanId` is specified but the Person does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    If `eventId` is specified but the Event does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        event_id (Union[Unset, None, int]):
        van_id (Union[Unset, None, str]):  Default: '100476252'.

    Returns:
        Response[Union[Any, Signups1Response400, Signups1Response404]]
    """

    kwargs = _get_kwargs(
        client=client,
        event_id=event_id,
        van_id=van_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    event_id: Union[Unset, None, int] = UNSET,
    van_id: Union[Unset, None, str] = "100476252",
) -> Optional[Union[Any, Signups1Response400, Signups1Response404]]:
    """/signups

     Use this endpoint to find all of a Person’s Signups (across all Events) or to find all of the
    Signups for a specific Event.

    Either the `eventId` parameter, or the `vanId` parameter, *must* be specified.

    If `vanId` is specified but the Person is not accessible, this endpoint will return an error with
    HTTP Status Code `403 Forbidden`.

    If `vanId` is specified but the Person does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    If `eventId` is specified but the Event does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        event_id (Union[Unset, None, int]):
        van_id (Union[Unset, None, str]):  Default: '100476252'.

    Returns:
        Response[Union[Any, Signups1Response400, Signups1Response404]]
    """

    return (
        await asyncio_detailed(
            client=client,
            event_id=event_id,
            van_id=van_id,
        )
    ).parsed
