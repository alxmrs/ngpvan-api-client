from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bargainingunitsbargainingunitid_response_200 import BargainingunitsbargainingunitidResponse200
from ...models.bargainingunitsbargainingunitid_response_400 import BargainingunitsbargainingunitidResponse400
from ...models.bargainingunitsbargainingunitid_response_404 import BargainingunitsbargainingunitidResponse404
from ...types import Response


def _get_kwargs(
    bargaining_unit_id: int = 99,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bargainingUnits/{bargainingUnitId}".format(client.base_url, bargainingUnitId=bargaining_unit_id)

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
) -> Optional[
    Union[
        BargainingunitsbargainingunitidResponse200,
        BargainingunitsbargainingunitidResponse400,
        BargainingunitsbargainingunitidResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = BargainingunitsbargainingunitidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BargainingunitsbargainingunitidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = BargainingunitsbargainingunitidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        BargainingunitsbargainingunitidResponse200,
        BargainingunitsbargainingunitidResponse400,
        BargainingunitsbargainingunitidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    bargaining_unit_id: int = 99,
    *,
    client: Client,
) -> Response[
    Union[
        BargainingunitsbargainingunitidResponse200,
        BargainingunitsbargainingunitidResponse400,
        BargainingunitsbargainingunitidResponse404,
    ]
]:
    """/bargainingUnits/{bargainingUnitId}

     Use this endpoint to retrieve the details of a specific Bargaining Unit.

    Args:
        bargaining_unit_id (int):  Default: 99.

    Returns:
        Response[Union[BargainingunitsbargainingunitidResponse200, BargainingunitsbargainingunitidResponse400, BargainingunitsbargainingunitidResponse404]]
    """

    kwargs = _get_kwargs(
        bargaining_unit_id=bargaining_unit_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    bargaining_unit_id: int = 99,
    *,
    client: Client,
) -> Optional[
    Union[
        BargainingunitsbargainingunitidResponse200,
        BargainingunitsbargainingunitidResponse400,
        BargainingunitsbargainingunitidResponse404,
    ]
]:
    """/bargainingUnits/{bargainingUnitId}

     Use this endpoint to retrieve the details of a specific Bargaining Unit.

    Args:
        bargaining_unit_id (int):  Default: 99.

    Returns:
        Response[Union[BargainingunitsbargainingunitidResponse200, BargainingunitsbargainingunitidResponse400, BargainingunitsbargainingunitidResponse404]]
    """

    return sync_detailed(
        bargaining_unit_id=bargaining_unit_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bargaining_unit_id: int = 99,
    *,
    client: Client,
) -> Response[
    Union[
        BargainingunitsbargainingunitidResponse200,
        BargainingunitsbargainingunitidResponse400,
        BargainingunitsbargainingunitidResponse404,
    ]
]:
    """/bargainingUnits/{bargainingUnitId}

     Use this endpoint to retrieve the details of a specific Bargaining Unit.

    Args:
        bargaining_unit_id (int):  Default: 99.

    Returns:
        Response[Union[BargainingunitsbargainingunitidResponse200, BargainingunitsbargainingunitidResponse400, BargainingunitsbargainingunitidResponse404]]
    """

    kwargs = _get_kwargs(
        bargaining_unit_id=bargaining_unit_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    bargaining_unit_id: int = 99,
    *,
    client: Client,
) -> Optional[
    Union[
        BargainingunitsbargainingunitidResponse200,
        BargainingunitsbargainingunitidResponse400,
        BargainingunitsbargainingunitidResponse404,
    ]
]:
    """/bargainingUnits/{bargainingUnitId}

     Use this endpoint to retrieve the details of a specific Bargaining Unit.

    Args:
        bargaining_unit_id (int):  Default: 99.

    Returns:
        Response[Union[BargainingunitsbargainingunitidResponse200, BargainingunitsbargainingunitidResponse400, BargainingunitsbargainingunitidResponse404]]
    """

    return (
        await asyncio_detailed(
            bargaining_unit_id=bargaining_unit_id,
            client=client,
        )
    ).parsed
