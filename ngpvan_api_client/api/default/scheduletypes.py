from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.scheduletypes_response_200 import ScheduletypesResponse200
from ...models.scheduletypes_response_400 import ScheduletypesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    top: Union[Unset, None, int] = 40,
) -> Dict[str, Any]:
    url = "{}/scheduleTypes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ScheduletypesResponse200, ScheduletypesResponse400]]:
    if response.status_code == 200:
        response_200 = ScheduletypesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ScheduletypesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ScheduletypesResponse200, ScheduletypesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    top: Union[Unset, None, int] = 40,
) -> Response[Union[ScheduletypesResponse200, ScheduletypesResponse400]]:
    """/scheduleTypes

     Use this endpoint to retrieve all Schedule Types available in the current context.

    Args:
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[ScheduletypesResponse200, ScheduletypesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
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
    top: Union[Unset, None, int] = 40,
) -> Optional[Union[ScheduletypesResponse200, ScheduletypesResponse400]]:
    """/scheduleTypes

     Use this endpoint to retrieve all Schedule Types available in the current context.

    Args:
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[ScheduletypesResponse200, ScheduletypesResponse400]]
    """

    return sync_detailed(
        client=client,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    top: Union[Unset, None, int] = 40,
) -> Response[Union[ScheduletypesResponse200, ScheduletypesResponse400]]:
    """/scheduleTypes

     Use this endpoint to retrieve all Schedule Types available in the current context.

    Args:
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[ScheduletypesResponse200, ScheduletypesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    top: Union[Unset, None, int] = 40,
) -> Optional[Union[ScheduletypesResponse200, ScheduletypesResponse400]]:
    """/scheduleTypes

     Use this endpoint to retrieve all Schedule Types available in the current context.

    Args:
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[ScheduletypesResponse200, ScheduletypesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            top=top,
        )
    ).parsed
