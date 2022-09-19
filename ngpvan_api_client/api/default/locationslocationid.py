from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.locationslocationid_response_400 import LocationslocationidResponse400
from ...models.locationslocationid_response_404 import LocationslocationidResponse404
from ...types import Response


def _get_kwargs(
    location_id: int = 301,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/locations/{locationId}".format(client.base_url, locationId=location_id)

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
) -> Optional[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = LocationslocationidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = LocationslocationidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    location_id: int = 301,
    *,
    client: Client,
) -> Response[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]:
    """/locations/{locationId}

     Retrieve a specific Location

    *Description*

    Use this endpoint to retrieve the details of a specific Location.

    Args:
        location_id (int):  Default: 301.

    Returns:
        Response[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    location_id: int = 301,
    *,
    client: Client,
) -> Optional[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]:
    """/locations/{locationId}

     Retrieve a specific Location

    *Description*

    Use this endpoint to retrieve the details of a specific Location.

    Args:
        location_id (int):  Default: 301.

    Returns:
        Response[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]
    """

    return sync_detailed(
        location_id=location_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    location_id: int = 301,
    *,
    client: Client,
) -> Response[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]:
    """/locations/{locationId}

     Retrieve a specific Location

    *Description*

    Use this endpoint to retrieve the details of a specific Location.

    Args:
        location_id (int):  Default: 301.

    Returns:
        Response[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    location_id: int = 301,
    *,
    client: Client,
) -> Optional[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]:
    """/locations/{locationId}

     Retrieve a specific Location

    *Description*

    Use this endpoint to retrieve the details of a specific Location.

    Args:
        location_id (int):  Default: 301.

    Returns:
        Response[Union[Any, LocationslocationidResponse400, LocationslocationidResponse404]]
    """

    return (
        await asyncio_detailed(
            location_id=location_id,
            client=client,
        )
    ).parsed
