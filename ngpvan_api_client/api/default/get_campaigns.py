from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_campaigns_response_200 import GetCampaignsResponse200
from ...models.get_campaigns_response_400 import GetCampaignsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/campaigns".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$top"] = top

    params["$skip"] = skip

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[GetCampaignsResponse200, GetCampaignsResponse400]]:
    if response.status_code == 200:
        response_200 = GetCampaignsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetCampaignsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GetCampaignsResponse200, GetCampaignsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
) -> Response[Union[GetCampaignsResponse200, GetCampaignsResponse400]]:
    """/campaigns

     Returns a [paginated](ref:pagination) list of [campaigns](ref:campaigns-common-models#campaign).

    Args:
        top (Union[Unset, None, int]):
        skip (Union[Unset, None, int]):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[GetCampaignsResponse200, GetCampaignsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        top=top,
        skip=skip,
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
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
) -> Optional[Union[GetCampaignsResponse200, GetCampaignsResponse400]]:
    """/campaigns

     Returns a [paginated](ref:pagination) list of [campaigns](ref:campaigns-common-models#campaign).

    Args:
        top (Union[Unset, None, int]):
        skip (Union[Unset, None, int]):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[GetCampaignsResponse200, GetCampaignsResponse400]]
    """

    return sync_detailed(
        client=client,
        top=top,
        skip=skip,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
) -> Response[Union[GetCampaignsResponse200, GetCampaignsResponse400]]:
    """/campaigns

     Returns a [paginated](ref:pagination) list of [campaigns](ref:campaigns-common-models#campaign).

    Args:
        top (Union[Unset, None, int]):
        skip (Union[Unset, None, int]):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[GetCampaignsResponse200, GetCampaignsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        top=top,
        skip=skip,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
) -> Optional[Union[GetCampaignsResponse200, GetCampaignsResponse400]]:
    """/campaigns

     Returns a [paginated](ref:pagination) list of [campaigns](ref:campaigns-common-models#campaign).

    Args:
        top (Union[Unset, None, int]):
        skip (Union[Unset, None, int]):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[GetCampaignsResponse200, GetCampaignsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            top=top,
            skip=skip,
            expand=expand,
        )
    ).parsed
