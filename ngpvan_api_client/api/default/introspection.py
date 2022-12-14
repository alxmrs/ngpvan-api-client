from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.introspection_response_200 import IntrospectionResponse200
from ...models.introspection_response_400 import IntrospectionResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/apiKeyProfiles".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[IntrospectionResponse200, IntrospectionResponse400]]:
    if response.status_code == 200:
        response_200 = IntrospectionResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = IntrospectionResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[IntrospectionResponse200, IntrospectionResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[IntrospectionResponse200, IntrospectionResponse400]]:
    """Introspection

     An introspection endpoint is available, if you need information about the API key you are using. The
    route returns a Paginated List of API keys available, with only one element in the list.

    Returns:
        Response[Union[IntrospectionResponse200, IntrospectionResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[IntrospectionResponse200, IntrospectionResponse400]]:
    """Introspection

     An introspection endpoint is available, if you need information about the API key you are using. The
    route returns a Paginated List of API keys available, with only one element in the list.

    Returns:
        Response[Union[IntrospectionResponse200, IntrospectionResponse400]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[IntrospectionResponse200, IntrospectionResponse400]]:
    """Introspection

     An introspection endpoint is available, if you need information about the API key you are using. The
    route returns a Paginated List of API keys available, with only one element in the list.

    Returns:
        Response[Union[IntrospectionResponse200, IntrospectionResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[IntrospectionResponse200, IntrospectionResponse400]]:
    """Introspection

     An introspection endpoint is available, if you need information about the API key you are using. The
    route returns a Paginated List of API keys available, with only one element in the list.

    Returns:
        Response[Union[IntrospectionResponse200, IntrospectionResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
