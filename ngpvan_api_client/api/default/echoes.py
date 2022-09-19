from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.echoes_json_body import EchoesJsonBody
from ...models.echoes_response_200 import EchoesResponse200
from ...models.echoes_response_400 import EchoesResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: EchoesJsonBody,
) -> Dict[str, Any]:
    url = "{}/echoes".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[EchoesResponse200, EchoesResponse400]]:
    if response.status_code == 200:
        response_200 = EchoesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = EchoesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[EchoesResponse200, EchoesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: EchoesJsonBody,
) -> Response[Union[EchoesResponse200, EchoesResponse400]]:
    """/echoes

    Args:
        json_body (EchoesJsonBody):

    Returns:
        Response[Union[EchoesResponse200, EchoesResponse400]]
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
    json_body: EchoesJsonBody,
) -> Optional[Union[EchoesResponse200, EchoesResponse400]]:
    """/echoes

    Args:
        json_body (EchoesJsonBody):

    Returns:
        Response[Union[EchoesResponse200, EchoesResponse400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: EchoesJsonBody,
) -> Response[Union[EchoesResponse200, EchoesResponse400]]:
    """/echoes

    Args:
        json_body (EchoesJsonBody):

    Returns:
        Response[Union[EchoesResponse200, EchoesResponse400]]
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
    json_body: EchoesJsonBody,
) -> Optional[Union[EchoesResponse200, EchoesResponse400]]:
    """/echoes

    Args:
        json_body (EchoesJsonBody):

    Returns:
        Response[Union[EchoesResponse200, EchoesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
