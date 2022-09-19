from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.eventseventid_2_response_400 import Eventseventid2Response400
from ...models.eventseventid_2_response_404 import Eventseventid2Response404
from ...types import Response


def _get_kwargs(
    event_id: int = 1374,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/events/{eventId}".format(client.base_url, eventId=event_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = Eventseventid2Response400.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = Eventseventid2Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_id: int = 1374,
    *,
    client: Client,
) -> Response[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]:
    """/events/{eventId}

     Use this endpoint to delete an existing Event and its related [Signups](ref:signups). If the Event
    is part of a recurring series of Events, the other Events in the series will remain untouched.

    If the Event is linked to any Voter Registration Batches, the links will be removed.

    If the specified Event does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Event does exist but is not editable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        event_id (int):  Default: 1374.

    Returns:
        Response[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    event_id: int = 1374,
    *,
    client: Client,
) -> Optional[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]:
    """/events/{eventId}

     Use this endpoint to delete an existing Event and its related [Signups](ref:signups). If the Event
    is part of a recurring series of Events, the other Events in the series will remain untouched.

    If the Event is linked to any Voter Registration Batches, the links will be removed.

    If the specified Event does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Event does exist but is not editable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        event_id (int):  Default: 1374.

    Returns:
        Response[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_id: int = 1374,
    *,
    client: Client,
) -> Response[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]:
    """/events/{eventId}

     Use this endpoint to delete an existing Event and its related [Signups](ref:signups). If the Event
    is part of a recurring series of Events, the other Events in the series will remain untouched.

    If the Event is linked to any Voter Registration Batches, the links will be removed.

    If the specified Event does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Event does exist but is not editable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        event_id (int):  Default: 1374.

    Returns:
        Response[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_id: int = 1374,
    *,
    client: Client,
) -> Optional[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]:
    """/events/{eventId}

     Use this endpoint to delete an existing Event and its related [Signups](ref:signups). If the Event
    is part of a recurring series of Events, the other Events in the series will remain untouched.

    If the Event is linked to any Voter Registration Batches, the links will be removed.

    If the specified Event does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Event does exist but is not editable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        event_id (int):  Default: 1374.

    Returns:
        Response[Union[Any, Eventseventid2Response400, Eventseventid2Response404]]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
        )
    ).parsed
