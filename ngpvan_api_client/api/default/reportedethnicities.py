from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.reportedethnicities_response_200 import ReportedethnicitiesResponse200
from ...models.reportedethnicities_response_400 import ReportedethnicitiesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    top: Union[Unset, None, int] = 3,
    skip: Union[Unset, None, int] = 1,
) -> Dict[str, Any]:
    url = "{}/reportedEthnicities".format(client.base_url)

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
) -> Optional[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]:
    if response.status_code == 200:
        response_200 = ReportedethnicitiesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ReportedethnicitiesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]:
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
) -> Response[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]:
    """/reportedEthnicities

     Retrieve available Reported Ethnicities

    Args:
        top (Union[Unset, None, int]):  Default: 3.
        skip (Union[Unset, None, int]):  Default: 1.

    Returns:
        Response[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]
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
) -> Optional[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]:
    """/reportedEthnicities

     Retrieve available Reported Ethnicities

    Args:
        top (Union[Unset, None, int]):  Default: 3.
        skip (Union[Unset, None, int]):  Default: 1.

    Returns:
        Response[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]
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
) -> Response[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]:
    """/reportedEthnicities

     Retrieve available Reported Ethnicities

    Args:
        top (Union[Unset, None, int]):  Default: 3.
        skip (Union[Unset, None, int]):  Default: 1.

    Returns:
        Response[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]
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
) -> Optional[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]:
    """/reportedEthnicities

     Retrieve available Reported Ethnicities

    Args:
        top (Union[Unset, None, int]):  Default: 3.
        skip (Union[Unset, None, int]):  Default: 1.

    Returns:
        Response[Union[ReportedethnicitiesResponse200, ReportedethnicitiesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            top=top,
            skip=skip,
        )
    ).parsed
