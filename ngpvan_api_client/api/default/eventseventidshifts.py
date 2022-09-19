from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.eventseventidshifts_json_body import EventseventidshiftsJsonBody
from ...models.eventseventidshifts_response_201 import EventseventidshiftsResponse201
from ...models.eventseventidshifts_response_400 import EventseventidshiftsResponse400
from ...models.eventseventidshifts_response_404 import EventseventidshiftsResponse404
from ...types import Response


def _get_kwargs(
    event_id: int = 1631,
    *,
    client: Client,
    json_body: EventseventidshiftsJsonBody,
) -> Dict[str, Any]:
    url = "{}/events/{eventId}/shifts".format(client.base_url, eventId=event_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]
]:
    if response.status_code == 201:
        response_201 = EventseventidshiftsResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = EventseventidshiftsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = EventseventidshiftsResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]
]:
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
    json_body: EventseventidshiftsJsonBody,
) -> Response[
    Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]
]:
    """/events/{eventId}/shifts

     Use this endpoint to add new Shifts to an existing Event. The advantages of this endpoint over the
    [Update](ref:eventseventid-3) endpoint are that you needn’t know the other properties of an event
    and it will return the unique identifier of the new Shift.

    If the specified Event does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Event does exist but is not editable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Shift in the response body.

    Args:
        event_id (int):  Default: 1631.
        json_body (EventseventidshiftsJsonBody):

    Returns:
        Response[Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
        json_body=json_body,
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
    json_body: EventseventidshiftsJsonBody,
) -> Optional[
    Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]
]:
    """/events/{eventId}/shifts

     Use this endpoint to add new Shifts to an existing Event. The advantages of this endpoint over the
    [Update](ref:eventseventid-3) endpoint are that you needn’t know the other properties of an event
    and it will return the unique identifier of the new Shift.

    If the specified Event does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Event does exist but is not editable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Shift in the response body.

    Args:
        event_id (int):  Default: 1631.
        json_body (EventseventidshiftsJsonBody):

    Returns:
        Response[Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    event_id: int = 1631,
    *,
    client: Client,
    json_body: EventseventidshiftsJsonBody,
) -> Response[
    Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]
]:
    """/events/{eventId}/shifts

     Use this endpoint to add new Shifts to an existing Event. The advantages of this endpoint over the
    [Update](ref:eventseventid-3) endpoint are that you needn’t know the other properties of an event
    and it will return the unique identifier of the new Shift.

    If the specified Event does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Event does exist but is not editable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Shift in the response body.

    Args:
        event_id (int):  Default: 1631.
        json_body (EventseventidshiftsJsonBody):

    Returns:
        Response[Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_id: int = 1631,
    *,
    client: Client,
    json_body: EventseventidshiftsJsonBody,
) -> Optional[
    Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]
]:
    """/events/{eventId}/shifts

     Use this endpoint to add new Shifts to an existing Event. The advantages of this endpoint over the
    [Update](ref:eventseventid-3) endpoint are that you needn’t know the other properties of an event
    and it will return the unique identifier of the new Shift.

    If the specified Event does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Event does exist but is not editable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Shift in the response body.

    Args:
        event_id (int):  Default: 1631.
        json_body (EventseventidshiftsJsonBody):

    Returns:
        Response[Union[Any, EventseventidshiftsResponse201, EventseventidshiftsResponse400, EventseventidshiftsResponse404]]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
