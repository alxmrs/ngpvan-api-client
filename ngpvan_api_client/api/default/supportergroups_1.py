from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.supportergroups_1_json_body import Supportergroups1JsonBody
from ...models.supportergroups_1_response_201 import Supportergroups1Response201
from ...models.supportergroups_1_response_400 import Supportergroups1Response400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Supportergroups1JsonBody,
) -> Dict[str, Any]:
    url = "{}/supporterGroups".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Supportergroups1Response201, Supportergroups1Response400]]:
    if response.status_code == 201:
        response_201 = Supportergroups1Response201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Supportergroups1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Supportergroups1Response201, Supportergroups1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Supportergroups1JsonBody,
) -> Response[Union[Supportergroups1Response201, Supportergroups1Response400]]:
    """/supporterGroups

     Use this endpoint to create a new supporter group

    Args:
        json_body (Supportergroups1JsonBody):

    Returns:
        Response[Union[Supportergroups1Response201, Supportergroups1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: Supportergroups1JsonBody,
) -> Optional[Union[Supportergroups1Response201, Supportergroups1Response400]]:
    """/supporterGroups

     Use this endpoint to create a new supporter group

    Args:
        json_body (Supportergroups1JsonBody):

    Returns:
        Response[Union[Supportergroups1Response201, Supportergroups1Response400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Supportergroups1JsonBody,
) -> Response[Union[Supportergroups1Response201, Supportergroups1Response400]]:
    """/supporterGroups

     Use this endpoint to create a new supporter group

    Args:
        json_body (Supportergroups1JsonBody):

    Returns:
        Response[Union[Supportergroups1Response201, Supportergroups1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Supportergroups1JsonBody,
) -> Optional[Union[Supportergroups1Response201, Supportergroups1Response400]]:
    """/supporterGroups

     Use this endpoint to create a new supporter group

    Args:
        json_body (Supportergroups1JsonBody):

    Returns:
        Response[Union[Supportergroups1Response201, Supportergroups1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
