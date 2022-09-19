from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.districtfieldsdistrictfieldid_response_400 import DistrictfieldsdistrictfieldidResponse400
from ...types import Response


def _get_kwargs(
    district_field_id: int = 1,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/districtFields/{districtFieldId}".format(client.base_url, districtFieldId=district_field_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DistrictfieldsdistrictfieldidResponse400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = DistrictfieldsdistrictfieldidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DistrictfieldsdistrictfieldidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    district_field_id: int = 1,
    *,
    client: Client,
) -> Response[Union[Any, DistrictfieldsdistrictfieldidResponse400]]:
    """/districtFields/{districtFieldId}

     Use this endpoint to get full details for a district field

    Args:
        district_field_id (int):  Default: 1.

    Returns:
        Response[Union[Any, DistrictfieldsdistrictfieldidResponse400]]
    """

    kwargs = _get_kwargs(
        district_field_id=district_field_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    district_field_id: int = 1,
    *,
    client: Client,
) -> Optional[Union[Any, DistrictfieldsdistrictfieldidResponse400]]:
    """/districtFields/{districtFieldId}

     Use this endpoint to get full details for a district field

    Args:
        district_field_id (int):  Default: 1.

    Returns:
        Response[Union[Any, DistrictfieldsdistrictfieldidResponse400]]
    """

    return sync_detailed(
        district_field_id=district_field_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    district_field_id: int = 1,
    *,
    client: Client,
) -> Response[Union[Any, DistrictfieldsdistrictfieldidResponse400]]:
    """/districtFields/{districtFieldId}

     Use this endpoint to get full details for a district field

    Args:
        district_field_id (int):  Default: 1.

    Returns:
        Response[Union[Any, DistrictfieldsdistrictfieldidResponse400]]
    """

    kwargs = _get_kwargs(
        district_field_id=district_field_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    district_field_id: int = 1,
    *,
    client: Client,
) -> Optional[Union[Any, DistrictfieldsdistrictfieldidResponse400]]:
    """/districtFields/{districtFieldId}

     Use this endpoint to get full details for a district field

    Args:
        district_field_id (int):  Default: 1.

    Returns:
        Response[Union[Any, DistrictfieldsdistrictfieldidResponse400]]
    """

    return (
        await asyncio_detailed(
            district_field_id=district_field_id,
            client=client,
        )
    ).parsed
