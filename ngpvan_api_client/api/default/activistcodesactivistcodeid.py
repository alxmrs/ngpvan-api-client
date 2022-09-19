from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.activistcodesactivistcodeid_response_200 import ActivistcodesactivistcodeidResponse200
from ...models.activistcodesactivistcodeid_response_400 import ActivistcodesactivistcodeidResponse400
from ...types import Response


def _get_kwargs(
    activist_code_id: int = 3214,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/activistCodes/{activistCodeId}".format(client.base_url, activistCodeId=activist_code_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]:
    if response.status_code == 200:
        response_200 = ActivistcodesactivistcodeidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ActivistcodesactivistcodeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    activist_code_id: int = 3214,
    *,
    client: Client,
) -> Response[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]:
    """/activistCodes/{activistCodeId}

     Use this endpoint to retrieve information about a specific Activist Code available in the current
    context.

    Args:
        activist_code_id (int):  Default: 3214.

    Returns:
        Response[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]
    """

    kwargs = _get_kwargs(
        activist_code_id=activist_code_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    activist_code_id: int = 3214,
    *,
    client: Client,
) -> Optional[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]:
    """/activistCodes/{activistCodeId}

     Use this endpoint to retrieve information about a specific Activist Code available in the current
    context.

    Args:
        activist_code_id (int):  Default: 3214.

    Returns:
        Response[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]
    """

    return sync_detailed(
        activist_code_id=activist_code_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    activist_code_id: int = 3214,
    *,
    client: Client,
) -> Response[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]:
    """/activistCodes/{activistCodeId}

     Use this endpoint to retrieve information about a specific Activist Code available in the current
    context.

    Args:
        activist_code_id (int):  Default: 3214.

    Returns:
        Response[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]
    """

    kwargs = _get_kwargs(
        activist_code_id=activist_code_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    activist_code_id: int = 3214,
    *,
    client: Client,
) -> Optional[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]:
    """/activistCodes/{activistCodeId}

     Use this endpoint to retrieve information about a specific Activist Code available in the current
    context.

    Args:
        activist_code_id (int):  Default: 3214.

    Returns:
        Response[Union[ActivistcodesactivistcodeidResponse200, ActivistcodesactivistcodeidResponse400, Any]]
    """

    return (
        await asyncio_detailed(
            activist_code_id=activist_code_id,
            client=client,
        )
    ).parsed
