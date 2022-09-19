from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_campaign_by_id_response_200 import GetCampaignByIdResponse200
from ...models.get_campaign_by_id_response_400 import GetCampaignByIdResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    campaign_id: int,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/campaigns/{campaignId}".format(client.base_url, campaignId=campaign_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]:
    if response.status_code == 200:
        response_200 = GetCampaignByIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetCampaignByIdResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    campaign_id: int,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Response[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]:
    """/campaigns/{campaignId}

     Get an existing Campaign by ID

    Args:
        campaign_id (int):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        client=client,
        expand=expand,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    campaign_id: int,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Optional[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]:
    """/campaigns/{campaignId}

     Get an existing Campaign by ID

    Args:
        campaign_id (int):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]
    """

    return sync_detailed(
        campaign_id=campaign_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    campaign_id: int,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Response[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]:
    """/campaigns/{campaignId}

     Get an existing Campaign by ID

    Args:
        campaign_id (int):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        client=client,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    campaign_id: int,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Optional[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]:
    """/campaigns/{campaignId}

     Get an existing Campaign by ID

    Args:
        campaign_id (int):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[GetCampaignByIdResponse200, GetCampaignByIdResponse400]]
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            client=client,
            expand=expand,
        )
    ).parsed
