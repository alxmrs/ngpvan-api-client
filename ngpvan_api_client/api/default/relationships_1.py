from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.relationships_1_response_200 import Relationships1Response200
from ...models.relationships_1_response_400 import Relationships1Response400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    top: Union[Unset, None, int] = 3,
    skip: Union[Unset, None, int] = 1,
) -> Dict[str, Any]:
    url = "{}/relationships".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$top"] = top

    params["$skip"] = skip

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
) -> Optional[Union[Relationships1Response200, Relationships1Response400]]:
    if response.status_code == 200:
        response_200 = Relationships1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Relationships1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Relationships1Response200, Relationships1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    top: Union[Unset, None, int] = 3,
    skip: Union[Unset, None, int] = 1,
) -> Response[Union[Relationships1Response200, Relationships1Response400]]:
    """/relationships

     Retrieve available Relationships

    Args:
        top (Union[Unset, None, int]):  Default: 3.
        skip (Union[Unset, None, int]):  Default: 1.

    Returns:
        Response[Union[Relationships1Response200, Relationships1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        top=top,
        skip=skip,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    top: Union[Unset, None, int] = 3,
    skip: Union[Unset, None, int] = 1,
) -> Optional[Union[Relationships1Response200, Relationships1Response400]]:
    """/relationships

     Retrieve available Relationships

    Args:
        top (Union[Unset, None, int]):  Default: 3.
        skip (Union[Unset, None, int]):  Default: 1.

    Returns:
        Response[Union[Relationships1Response200, Relationships1Response400]]
    """

    return sync_detailed(
        client=client,
        top=top,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    top: Union[Unset, None, int] = 3,
    skip: Union[Unset, None, int] = 1,
) -> Response[Union[Relationships1Response200, Relationships1Response400]]:
    """/relationships

     Retrieve available Relationships

    Args:
        top (Union[Unset, None, int]):  Default: 3.
        skip (Union[Unset, None, int]):  Default: 1.

    Returns:
        Response[Union[Relationships1Response200, Relationships1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        top=top,
        skip=skip,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    top: Union[Unset, None, int] = 3,
    skip: Union[Unset, None, int] = 1,
) -> Optional[Union[Relationships1Response200, Relationships1Response400]]:
    """/relationships

     Retrieve available Relationships

    Args:
        top (Union[Unset, None, int]):  Default: 3.
        skip (Union[Unset, None, int]):  Default: 1.

    Returns:
        Response[Union[Relationships1Response200, Relationships1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            top=top,
            skip=skip,
        )
    ).parsed
