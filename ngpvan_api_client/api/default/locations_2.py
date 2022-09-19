from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.locations_2_json_body import Locations2JsonBody
from ...models.locations_2_response_400 import Locations2Response400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Locations2JsonBody,
) -> Dict[str, Any]:
    url = "{}/locations".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Locations2Response400]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 400:
        response_400 = Locations2Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Locations2Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Locations2JsonBody,
) -> Response[Union[Any, Locations2Response400]]:
    """/locations

     Use this endpoint to create a new Location.

    Typically it’s more appropriate to [find or create](ref:locations#locationsfindorcreate) a Location
    because you may not know whether a very similar Location already exists (e.g., was created in the
    VAN UI).

    If successful, the endpoint responds with HTTP Status Code `201 Created`. It also sets the
    **Location** header to the [location](ref:location#locationslocationid) of the Location.

    Args:
        json_body (Locations2JsonBody):

    Returns:
        Response[Union[Any, Locations2Response400]]
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
    json_body: Locations2JsonBody,
) -> Optional[Union[Any, Locations2Response400]]:
    """/locations

     Use this endpoint to create a new Location.

    Typically it’s more appropriate to [find or create](ref:locations#locationsfindorcreate) a Location
    because you may not know whether a very similar Location already exists (e.g., was created in the
    VAN UI).

    If successful, the endpoint responds with HTTP Status Code `201 Created`. It also sets the
    **Location** header to the [location](ref:location#locationslocationid) of the Location.

    Args:
        json_body (Locations2JsonBody):

    Returns:
        Response[Union[Any, Locations2Response400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Locations2JsonBody,
) -> Response[Union[Any, Locations2Response400]]:
    """/locations

     Use this endpoint to create a new Location.

    Typically it’s more appropriate to [find or create](ref:locations#locationsfindorcreate) a Location
    because you may not know whether a very similar Location already exists (e.g., was created in the
    VAN UI).

    If successful, the endpoint responds with HTTP Status Code `201 Created`. It also sets the
    **Location** header to the [location](ref:location#locationslocationid) of the Location.

    Args:
        json_body (Locations2JsonBody):

    Returns:
        Response[Union[Any, Locations2Response400]]
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
    json_body: Locations2JsonBody,
) -> Optional[Union[Any, Locations2Response400]]:
    """/locations

     Use this endpoint to create a new Location.

    Typically it’s more appropriate to [find or create](ref:locations#locationsfindorcreate) a Location
    because you may not know whether a very similar Location already exists (e.g., was created in the
    VAN UI).

    If successful, the endpoint responds with HTTP Status Code `201 Created`. It also sets the
    **Location** header to the [location](ref:location#locationslocationid) of the Location.

    Args:
        json_body (Locations2JsonBody):

    Returns:
        Response[Union[Any, Locations2Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
