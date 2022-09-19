from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.activistcodes_response_200 import ActivistcodesResponse200
from ...models.activistcodes_response_400 import ActivistcodesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active",
    name: Union[Unset, None, str] = "Precinct",
    type: Union[Unset, None, str] = "Volunteer",
    top: Union[Unset, None, int] = 200,
) -> Dict[str, Any]:
    url = "{}/activistCodes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["statuses"] = statuses

    params["name"] = name

    params["type"] = type

    params["$top"] = top

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ActivistcodesResponse200, ActivistcodesResponse400]]:
    if response.status_code == 200:
        response_200 = ActivistcodesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ActivistcodesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ActivistcodesResponse200, ActivistcodesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active",
    name: Union[Unset, None, str] = "Precinct",
    type: Union[Unset, None, str] = "Volunteer",
    top: Union[Unset, None, int] = 200,
) -> Response[Union[ActivistcodesResponse200, ActivistcodesResponse400]]:
    """/activistCodes

     Use this endpoint to retrieve all Activist Codes that are available in the current context.

    This endpoint accepts [standard pagination parameters](ref:pagination) and returns a standard
    paginated response.

    By default, this endpoint returns 50 records per request. A maximum of 200 records per request is
    allowed via the `$top` parameter.

    Args:
        statuses (Union[Unset, None, str]):  Default: 'Active'.
        name (Union[Unset, None, str]):  Default: 'Precinct'.
        type (Union[Unset, None, str]):  Default: 'Volunteer'.
        top (Union[Unset, None, int]):  Default: 200.

    Returns:
        Response[Union[ActivistcodesResponse200, ActivistcodesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        statuses=statuses,
        name=name,
        type=type,
        top=top,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active",
    name: Union[Unset, None, str] = "Precinct",
    type: Union[Unset, None, str] = "Volunteer",
    top: Union[Unset, None, int] = 200,
) -> Optional[Union[ActivistcodesResponse200, ActivistcodesResponse400]]:
    """/activistCodes

     Use this endpoint to retrieve all Activist Codes that are available in the current context.

    This endpoint accepts [standard pagination parameters](ref:pagination) and returns a standard
    paginated response.

    By default, this endpoint returns 50 records per request. A maximum of 200 records per request is
    allowed via the `$top` parameter.

    Args:
        statuses (Union[Unset, None, str]):  Default: 'Active'.
        name (Union[Unset, None, str]):  Default: 'Precinct'.
        type (Union[Unset, None, str]):  Default: 'Volunteer'.
        top (Union[Unset, None, int]):  Default: 200.

    Returns:
        Response[Union[ActivistcodesResponse200, ActivistcodesResponse400]]
    """

    return sync_detailed(
        client=client,
        statuses=statuses,
        name=name,
        type=type,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active",
    name: Union[Unset, None, str] = "Precinct",
    type: Union[Unset, None, str] = "Volunteer",
    top: Union[Unset, None, int] = 200,
) -> Response[Union[ActivistcodesResponse200, ActivistcodesResponse400]]:
    """/activistCodes

     Use this endpoint to retrieve all Activist Codes that are available in the current context.

    This endpoint accepts [standard pagination parameters](ref:pagination) and returns a standard
    paginated response.

    By default, this endpoint returns 50 records per request. A maximum of 200 records per request is
    allowed via the `$top` parameter.

    Args:
        statuses (Union[Unset, None, str]):  Default: 'Active'.
        name (Union[Unset, None, str]):  Default: 'Precinct'.
        type (Union[Unset, None, str]):  Default: 'Volunteer'.
        top (Union[Unset, None, int]):  Default: 200.

    Returns:
        Response[Union[ActivistcodesResponse200, ActivistcodesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        statuses=statuses,
        name=name,
        type=type,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active",
    name: Union[Unset, None, str] = "Precinct",
    type: Union[Unset, None, str] = "Volunteer",
    top: Union[Unset, None, int] = 200,
) -> Optional[Union[ActivistcodesResponse200, ActivistcodesResponse400]]:
    """/activistCodes

     Use this endpoint to retrieve all Activist Codes that are available in the current context.

    This endpoint accepts [standard pagination parameters](ref:pagination) and returns a standard
    paginated response.

    By default, this endpoint returns 50 records per request. A maximum of 200 records per request is
    allowed via the `$top` parameter.

    Args:
        statuses (Union[Unset, None, str]):  Default: 'Active'.
        name (Union[Unset, None, str]):  Default: 'Precinct'.
        type (Union[Unset, None, str]):  Default: 'Volunteer'.
        top (Union[Unset, None, int]):  Default: 200.

    Returns:
        Response[Union[ActivistcodesResponse200, ActivistcodesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            statuses=statuses,
            name=name,
            type=type,
            top=top,
        )
    ).parsed
