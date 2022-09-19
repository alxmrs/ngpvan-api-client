from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.targets_1_response_400 import Targets1Response400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    status: Union[Unset, None, str] = "Setup",
    type: Union[Unset, None, str] = "Static",
    top: Union[Unset, None, int] = 35,
    expand: Union[Unset, None, str] = "subgroups",
) -> Dict[str, Any]:
    url = "{}/targets".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["status"] = status

    params["type"] = type

    params["$top"] = top

    params["$expand"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Targets1Response400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = Targets1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Targets1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    status: Union[Unset, None, str] = "Setup",
    type: Union[Unset, None, str] = "Static",
    top: Union[Unset, None, int] = 35,
    expand: Union[Unset, None, str] = "subgroups",
) -> Response[Union[Any, Targets1Response400]]:
    """/targets

     Use this endpoint to retrieve all Targets that are available in the current context.

    Args:
        status (Union[Unset, None, str]):  Default: 'Setup'.
        type (Union[Unset, None, str]):  Default: 'Static'.
        top (Union[Unset, None, int]):  Default: 35.
        expand (Union[Unset, None, str]):  Default: 'subgroups'.

    Returns:
        Response[Union[Any, Targets1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        status=status,
        type=type,
        top=top,
        expand=expand,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    status: Union[Unset, None, str] = "Setup",
    type: Union[Unset, None, str] = "Static",
    top: Union[Unset, None, int] = 35,
    expand: Union[Unset, None, str] = "subgroups",
) -> Optional[Union[Any, Targets1Response400]]:
    """/targets

     Use this endpoint to retrieve all Targets that are available in the current context.

    Args:
        status (Union[Unset, None, str]):  Default: 'Setup'.
        type (Union[Unset, None, str]):  Default: 'Static'.
        top (Union[Unset, None, int]):  Default: 35.
        expand (Union[Unset, None, str]):  Default: 'subgroups'.

    Returns:
        Response[Union[Any, Targets1Response400]]
    """

    return sync_detailed(
        client=client,
        status=status,
        type=type,
        top=top,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    status: Union[Unset, None, str] = "Setup",
    type: Union[Unset, None, str] = "Static",
    top: Union[Unset, None, int] = 35,
    expand: Union[Unset, None, str] = "subgroups",
) -> Response[Union[Any, Targets1Response400]]:
    """/targets

     Use this endpoint to retrieve all Targets that are available in the current context.

    Args:
        status (Union[Unset, None, str]):  Default: 'Setup'.
        type (Union[Unset, None, str]):  Default: 'Static'.
        top (Union[Unset, None, int]):  Default: 35.
        expand (Union[Unset, None, str]):  Default: 'subgroups'.

    Returns:
        Response[Union[Any, Targets1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        status=status,
        type=type,
        top=top,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    status: Union[Unset, None, str] = "Setup",
    type: Union[Unset, None, str] = "Static",
    top: Union[Unset, None, int] = 35,
    expand: Union[Unset, None, str] = "subgroups",
) -> Optional[Union[Any, Targets1Response400]]:
    """/targets

     Use this endpoint to retrieve all Targets that are available in the current context.

    Args:
        status (Union[Unset, None, str]):  Default: 'Setup'.
        type (Union[Unset, None, str]):  Default: 'Static'.
        top (Union[Unset, None, int]):  Default: 35.
        expand (Union[Unset, None, str]):  Default: 'subgroups'.

    Returns:
        Response[Union[Any, Targets1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            type=type,
            top=top,
            expand=expand,
        )
    ).parsed
