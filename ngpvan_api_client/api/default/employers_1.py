from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.employers_1_response_400 import Employers1Response400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "parent",
) -> Dict[str, Any]:
    url = "{}/employers".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["isMyOrganization"] = is_my_organization

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Employers1Response400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = Employers1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Employers1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "parent",
) -> Response[Union[Any, Employers1Response400]]:
    """/employers

     Use this endpoint to retrieve all Employers available in the current context.

    By default, this endpoint returns 250 records per request. A maximum of 500 records per request is
    allowed via the `$top` parameter.

    Args:
        is_my_organization (Union[Unset, None, bool]):
        expand (Union[Unset, None, str]):  Default: 'parent'.

    Returns:
        Response[Union[Any, Employers1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        is_my_organization=is_my_organization,
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
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "parent",
) -> Optional[Union[Any, Employers1Response400]]:
    """/employers

     Use this endpoint to retrieve all Employers available in the current context.

    By default, this endpoint returns 250 records per request. A maximum of 500 records per request is
    allowed via the `$top` parameter.

    Args:
        is_my_organization (Union[Unset, None, bool]):
        expand (Union[Unset, None, str]):  Default: 'parent'.

    Returns:
        Response[Union[Any, Employers1Response400]]
    """

    return sync_detailed(
        client=client,
        is_my_organization=is_my_organization,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "parent",
) -> Response[Union[Any, Employers1Response400]]:
    """/employers

     Use this endpoint to retrieve all Employers available in the current context.

    By default, this endpoint returns 250 records per request. A maximum of 500 records per request is
    allowed via the `$top` parameter.

    Args:
        is_my_organization (Union[Unset, None, bool]):
        expand (Union[Unset, None, str]):  Default: 'parent'.

    Returns:
        Response[Union[Any, Employers1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        is_my_organization=is_my_organization,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "parent",
) -> Optional[Union[Any, Employers1Response400]]:
    """/employers

     Use this endpoint to retrieve all Employers available in the current context.

    By default, this endpoint returns 250 records per request. A maximum of 500 records per request is
    allowed via the `$top` parameter.

    Args:
        is_my_organization (Union[Unset, None, bool]):
        expand (Union[Unset, None, str]):  Default: 'parent'.

    Returns:
        Response[Union[Any, Employers1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            is_my_organization=is_my_organization,
            expand=expand,
        )
    ).parsed
