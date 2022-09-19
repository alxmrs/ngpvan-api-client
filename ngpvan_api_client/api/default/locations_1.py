from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.locations_1_response_400 import Locations1Response400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    name: Union[Unset, None, str] = "HQ",
) -> Dict[str, Any]:
    url = "{}/locations".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Locations1Response400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = Locations1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Locations1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    name: Union[Unset, None, str] = "HQ",
) -> Response[Union[Any, Locations1Response400]]:
    """/locations

     Use this endpoint to find Locations available in the current context using a number of filter
    options.

    Args:
        name (Union[Unset, None, str]):  Default: 'HQ'.

    Returns:
        Response[Union[Any, Locations1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    name: Union[Unset, None, str] = "HQ",
) -> Optional[Union[Any, Locations1Response400]]:
    """/locations

     Use this endpoint to find Locations available in the current context using a number of filter
    options.

    Args:
        name (Union[Unset, None, str]):  Default: 'HQ'.

    Returns:
        Response[Union[Any, Locations1Response400]]
    """

    return sync_detailed(
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    name: Union[Unset, None, str] = "HQ",
) -> Response[Union[Any, Locations1Response400]]:
    """/locations

     Use this endpoint to find Locations available in the current context using a number of filter
    options.

    Args:
        name (Union[Unset, None, str]):  Default: 'HQ'.

    Returns:
        Response[Union[Any, Locations1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    name: Union[Unset, None, str] = "HQ",
) -> Optional[Union[Any, Locations1Response400]]:
    """/locations

     Use this endpoint to find Locations available in the current context using a number of filter
    options.

    Args:
        name (Union[Unset, None, str]):  Default: 'HQ'.

    Returns:
        Response[Union[Any, Locations1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
