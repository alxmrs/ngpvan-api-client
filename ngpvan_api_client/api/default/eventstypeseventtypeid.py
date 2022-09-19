from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.eventstypeseventtypeid_response_400 import EventstypeseventtypeidResponse400
from ...models.eventstypeseventtypeid_response_404 import EventstypeseventtypeidResponse404
from ...types import Response


def _get_kwargs(
    event_type_id: int = 20036,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/events/types/{eventTypeId}".format(client.base_url, eventTypeId=event_type_id)

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
) -> Optional[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = EventstypeseventtypeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = EventstypeseventtypeidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_type_id: int = 20036,
    *,
    client: Client,
) -> Response[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]:
    """/events/types/{eventTypeId}

     Use this endpoint to retrieve information about a specific Event Type available in the current
    context.

    Args:
        event_type_id (int):  Default: 20036.

    Returns:
        Response[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]
    """

    kwargs = _get_kwargs(
        event_type_id=event_type_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    event_type_id: int = 20036,
    *,
    client: Client,
) -> Optional[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]:
    """/events/types/{eventTypeId}

     Use this endpoint to retrieve information about a specific Event Type available in the current
    context.

    Args:
        event_type_id (int):  Default: 20036.

    Returns:
        Response[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]
    """

    return sync_detailed(
        event_type_id=event_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_type_id: int = 20036,
    *,
    client: Client,
) -> Response[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]:
    """/events/types/{eventTypeId}

     Use this endpoint to retrieve information about a specific Event Type available in the current
    context.

    Args:
        event_type_id (int):  Default: 20036.

    Returns:
        Response[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]
    """

    kwargs = _get_kwargs(
        event_type_id=event_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_type_id: int = 20036,
    *,
    client: Client,
) -> Optional[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]:
    """/events/types/{eventTypeId}

     Use this endpoint to retrieve information about a specific Event Type available in the current
    context.

    Args:
        event_type_id (int):  Default: 20036.

    Returns:
        Response[Union[Any, EventstypeseventtypeidResponse400, EventstypeseventtypeidResponse404]]
    """

    return (
        await asyncio_detailed(
            event_type_id=event_type_id,
            client=client,
        )
    ).parsed
