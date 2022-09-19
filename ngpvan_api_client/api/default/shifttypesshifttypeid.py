from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.shifttypesshifttypeid_response_200 import ShifttypesshifttypeidResponse200
from ...models.shifttypesshifttypeid_response_400 import ShifttypesshifttypeidResponse400
from ...models.shifttypesshifttypeid_response_404 import ShifttypesshifttypeidResponse404
from ...types import Response


def _get_kwargs(
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/shiftTypes/{shiftTypeId}".format(client.base_url, shiftTypeId=shift_type_id)

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
    Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]
]:
    if response.status_code == 200:
        response_200 = ShifttypesshifttypeidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ShifttypesshifttypeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ShifttypesshifttypeidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Response[
    Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]
]:
    """/shiftTypes/{shiftTypeId}

     Use this endpoint to retrieve the details of a specific Shift Type.

    Args:
        shift_type_id (int):  Default: 12.

    Returns:
        Response[Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]]
    """

    kwargs = _get_kwargs(
        shift_type_id=shift_type_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Optional[
    Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]
]:
    """/shiftTypes/{shiftTypeId}

     Use this endpoint to retrieve the details of a specific Shift Type.

    Args:
        shift_type_id (int):  Default: 12.

    Returns:
        Response[Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]]
    """

    return sync_detailed(
        shift_type_id=shift_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Response[
    Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]
]:
    """/shiftTypes/{shiftTypeId}

     Use this endpoint to retrieve the details of a specific Shift Type.

    Args:
        shift_type_id (int):  Default: 12.

    Returns:
        Response[Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]]
    """

    kwargs = _get_kwargs(
        shift_type_id=shift_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Optional[
    Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]
]:
    """/shiftTypes/{shiftTypeId}

     Use this endpoint to retrieve the details of a specific Shift Type.

    Args:
        shift_type_id (int):  Default: 12.

    Returns:
        Response[Union[ShifttypesshifttypeidResponse200, ShifttypesshifttypeidResponse400, ShifttypesshifttypeidResponse404]]
    """

    return (
        await asyncio_detailed(
            shift_type_id=shift_type_id,
            client=client,
        )
    ).parsed
