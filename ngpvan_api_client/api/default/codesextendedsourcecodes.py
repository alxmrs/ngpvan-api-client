from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.codesextendedsourcecodes_response_400 import CodesextendedsourcecodesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    van_id: Union[Unset, None, int] = 100476252,
    extended_source_code_name: Union[Unset, None, str] = "AXY1",
) -> Dict[str, Any]:
    url = "{}/codes/extendedSourceCodes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["vanId"] = van_id

    params["extendedSourceCodeName"] = extended_source_code_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CodesextendedsourcecodesResponse400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = CodesextendedsourcecodesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CodesextendedsourcecodesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    van_id: Union[Unset, None, int] = 100476252,
    extended_source_code_name: Union[Unset, None, str] = "AXY1",
) -> Response[Union[Any, CodesextendedsourcecodesResponse400]]:
    """/codes/extendedSourceCodes

     Use this endpoint to find Extended Source Codes available in the current context.

    Args:
        van_id (Union[Unset, None, int]):  Default: 100476252.
        extended_source_code_name (Union[Unset, None, str]):  Default: 'AXY1'.

    Returns:
        Response[Union[Any, CodesextendedsourcecodesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        van_id=van_id,
        extended_source_code_name=extended_source_code_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    van_id: Union[Unset, None, int] = 100476252,
    extended_source_code_name: Union[Unset, None, str] = "AXY1",
) -> Optional[Union[Any, CodesextendedsourcecodesResponse400]]:
    """/codes/extendedSourceCodes

     Use this endpoint to find Extended Source Codes available in the current context.

    Args:
        van_id (Union[Unset, None, int]):  Default: 100476252.
        extended_source_code_name (Union[Unset, None, str]):  Default: 'AXY1'.

    Returns:
        Response[Union[Any, CodesextendedsourcecodesResponse400]]
    """

    return sync_detailed(
        client=client,
        van_id=van_id,
        extended_source_code_name=extended_source_code_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    van_id: Union[Unset, None, int] = 100476252,
    extended_source_code_name: Union[Unset, None, str] = "AXY1",
) -> Response[Union[Any, CodesextendedsourcecodesResponse400]]:
    """/codes/extendedSourceCodes

     Use this endpoint to find Extended Source Codes available in the current context.

    Args:
        van_id (Union[Unset, None, int]):  Default: 100476252.
        extended_source_code_name (Union[Unset, None, str]):  Default: 'AXY1'.

    Returns:
        Response[Union[Any, CodesextendedsourcecodesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        van_id=van_id,
        extended_source_code_name=extended_source_code_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    van_id: Union[Unset, None, int] = 100476252,
    extended_source_code_name: Union[Unset, None, str] = "AXY1",
) -> Optional[Union[Any, CodesextendedsourcecodesResponse400]]:
    """/codes/extendedSourceCodes

     Use this endpoint to find Extended Source Codes available in the current context.

    Args:
        van_id (Union[Unset, None, int]):  Default: 100476252.
        extended_source_code_name (Union[Unset, None, str]):  Default: 'AXY1'.

    Returns:
        Response[Union[Any, CodesextendedsourcecodesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            van_id=van_id,
            extended_source_code_name=extended_source_code_name,
        )
    ).parsed
