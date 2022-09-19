from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.codetypes_response_400 import CodetypesResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/codeTypes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CodetypesResponse400, List[str]]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CodetypesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CodetypesResponse400, List[str]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[CodetypesResponse400, List[str]]]:
    """/codeTypes

     Use this endpoint to determine which code types are available for your API key. At most two types
    will be available: `Tag` and/or `SourceCode`. See [Codes Overview](ref:codes#overview-7) for more
    information.

    Returns:
        Response[Union[CodetypesResponse400, List[str]]]
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
) -> Optional[Union[CodetypesResponse400, List[str]]]:
    """/codeTypes

     Use this endpoint to determine which code types are available for your API key. At most two types
    will be available: `Tag` and/or `SourceCode`. See [Codes Overview](ref:codes#overview-7) for more
    information.

    Returns:
        Response[Union[CodetypesResponse400, List[str]]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[CodetypesResponse400, List[str]]]:
    """/codeTypes

     Use this endpoint to determine which code types are available for your API key. At most two types
    will be available: `Tag` and/or `SourceCode`. See [Codes Overview](ref:codes#overview-7) for more
    information.

    Returns:
        Response[Union[CodetypesResponse400, List[str]]]
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
) -> Optional[Union[CodetypesResponse400, List[str]]]:
    """/codeTypes

     Use this endpoint to determine which code types are available for your API key. At most two types
    will be available: `Tag` and/or `SourceCode`. See [Codes Overview](ref:codes#overview-7) for more
    information.

    Returns:
        Response[Union[CodetypesResponse400, List[str]]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
