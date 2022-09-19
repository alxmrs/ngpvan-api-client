from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.events_2_json_body import Events2JsonBody
from ...models.events_2_response_201 import Events2Response201
from ...models.events_2_response_400 import Events2Response400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Events2JsonBody,
) -> Dict[str, Any]:
    url = "{}/events".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Events2Response201, Events2Response400]]:
    if response.status_code == 201:
        response_201 = Events2Response201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Events2Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Events2Response201, Events2Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Events2JsonBody,
) -> Response[Union[Events2Response201, Events2Response400]]:
    """/events

     Use this endpoint to create a new Event.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Event in the response body. It also sets the **Location** header to the
    (location)[ref:eventseventid] of the newly created Event.

    Args:
        json_body (Events2JsonBody):

    Returns:
        Response[Union[Events2Response201, Events2Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: Events2JsonBody,
) -> Optional[Union[Events2Response201, Events2Response400]]:
    """/events

     Use this endpoint to create a new Event.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Event in the response body. It also sets the **Location** header to the
    (location)[ref:eventseventid] of the newly created Event.

    Args:
        json_body (Events2JsonBody):

    Returns:
        Response[Union[Events2Response201, Events2Response400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Events2JsonBody,
) -> Response[Union[Events2Response201, Events2Response400]]:
    """/events

     Use this endpoint to create a new Event.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Event in the response body. It also sets the **Location** header to the
    (location)[ref:eventseventid] of the newly created Event.

    Args:
        json_body (Events2JsonBody):

    Returns:
        Response[Union[Events2Response201, Events2Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Events2JsonBody,
) -> Optional[Union[Events2Response201, Events2Response400]]:
    """/events

     Use this endpoint to create a new Event.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Event in the response body. It also sets the **Location** header to the
    (location)[ref:eventseventid] of the newly created Event.

    Args:
        json_body (Events2JsonBody):

    Returns:
        Response[Union[Events2Response201, Events2Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
