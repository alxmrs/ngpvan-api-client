from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.minivanexportsminivanexportid_response_400 import MinivanexportsminivanexportidResponse400
from ...models.minivanexportsminivanexportid_response_404 import MinivanexportsminivanexportidResponse404
from ...types import Response


def _get_kwargs(
    minivan_export_id: int = 13149,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/minivanExports/{minivanExportId}".format(client.base_url, minivanExportId=minivan_export_id)

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
) -> Optional[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = MinivanexportsminivanexportidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = MinivanexportsminivanexportidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    minivan_export_id: int = 13149,
    *,
    client: Client,
) -> Response[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]:
    """/minivanExports/{minivanExportId}

     Use this endpoint to get full details for a MiniVAN Export

    Args:
        minivan_export_id (int):  Default: 13149.

    Returns:
        Response[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]
    """

    kwargs = _get_kwargs(
        minivan_export_id=minivan_export_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    minivan_export_id: int = 13149,
    *,
    client: Client,
) -> Optional[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]:
    """/minivanExports/{minivanExportId}

     Use this endpoint to get full details for a MiniVAN Export

    Args:
        minivan_export_id (int):  Default: 13149.

    Returns:
        Response[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]
    """

    return sync_detailed(
        minivan_export_id=minivan_export_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    minivan_export_id: int = 13149,
    *,
    client: Client,
) -> Response[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]:
    """/minivanExports/{minivanExportId}

     Use this endpoint to get full details for a MiniVAN Export

    Args:
        minivan_export_id (int):  Default: 13149.

    Returns:
        Response[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]
    """

    kwargs = _get_kwargs(
        minivan_export_id=minivan_export_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    minivan_export_id: int = 13149,
    *,
    client: Client,
) -> Optional[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]:
    """/minivanExports/{minivanExportId}

     Use this endpoint to get full details for a MiniVAN Export

    Args:
        minivan_export_id (int):  Default: 13149.

    Returns:
        Response[Union[Any, MinivanexportsminivanexportidResponse400, MinivanexportsminivanexportidResponse404]]
    """

    return (
        await asyncio_detailed(
            minivan_export_id=minivan_export_id,
            client=client,
        )
    ).parsed
