from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.districtfields_response_400 import DistrictfieldsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    custom: Union[Unset, None, bool] = False,
    organize_at: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/districtFields".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["custom"] = custom

    params["organizeAt"] = organize_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DistrictfieldsResponse400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = DistrictfieldsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DistrictfieldsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    custom: Union[Unset, None, bool] = False,
    organize_at: Union[Unset, None, bool] = False,
) -> Response[Union[Any, DistrictfieldsResponse400]]:
    """/districtFields

     Get all available district fields

    *Description*

    Use this endpoint to retrieve all District Fields

    *Response*

    This endpoint returns an object whose `districts` property provides an array of [District
    Field](ref:district-field) objects, without district field values.

    Args:
        custom (Union[Unset, None, bool]):
        organize_at (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, DistrictfieldsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        custom=custom,
        organize_at=organize_at,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    custom: Union[Unset, None, bool] = False,
    organize_at: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, DistrictfieldsResponse400]]:
    """/districtFields

     Get all available district fields

    *Description*

    Use this endpoint to retrieve all District Fields

    *Response*

    This endpoint returns an object whose `districts` property provides an array of [District
    Field](ref:district-field) objects, without district field values.

    Args:
        custom (Union[Unset, None, bool]):
        organize_at (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, DistrictfieldsResponse400]]
    """

    return sync_detailed(
        client=client,
        custom=custom,
        organize_at=organize_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    custom: Union[Unset, None, bool] = False,
    organize_at: Union[Unset, None, bool] = False,
) -> Response[Union[Any, DistrictfieldsResponse400]]:
    """/districtFields

     Get all available district fields

    *Description*

    Use this endpoint to retrieve all District Fields

    *Response*

    This endpoint returns an object whose `districts` property provides an array of [District
    Field](ref:district-field) objects, without district field values.

    Args:
        custom (Union[Unset, None, bool]):
        organize_at (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, DistrictfieldsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        custom=custom,
        organize_at=organize_at,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    custom: Union[Unset, None, bool] = False,
    organize_at: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, DistrictfieldsResponse400]]:
    """/districtFields

     Get all available district fields

    *Description*

    Use this endpoint to retrieve all District Fields

    *Response*

    This endpoint returns an object whose `districts` property provides an array of [District
    Field](ref:district-field) objects, without district field values.

    Args:
        custom (Union[Unset, None, bool]):
        organize_at (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, DistrictfieldsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            custom=custom,
            organize_at=organize_at,
        )
    ).parsed
