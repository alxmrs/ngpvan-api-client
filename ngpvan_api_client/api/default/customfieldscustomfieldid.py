from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.customfieldscustomfieldid_response_200 import CustomfieldscustomfieldidResponse200
from ...models.customfieldscustomfieldid_response_400 import CustomfieldscustomfieldidResponse400
from ...types import Response


def _get_kwargs(
    custom_field_id: int = 157,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/customFields/{customFieldId}".format(client.base_url, customFieldId=custom_field_id)

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
) -> Optional[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]:
    if response.status_code == 200:
        response_200 = CustomfieldscustomfieldidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CustomfieldscustomfieldidResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    custom_field_id: int = 157,
    *,
    client: Client,
) -> Response[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]:
    """/customFields/{customFieldId}

     Use this endpoint to retrieve information about a specific Custom Field available in the current
    context.

    Args:
        custom_field_id (int):  Default: 157.

    Returns:
        Response[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]
    """

    kwargs = _get_kwargs(
        custom_field_id=custom_field_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    custom_field_id: int = 157,
    *,
    client: Client,
) -> Optional[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]:
    """/customFields/{customFieldId}

     Use this endpoint to retrieve information about a specific Custom Field available in the current
    context.

    Args:
        custom_field_id (int):  Default: 157.

    Returns:
        Response[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]
    """

    return sync_detailed(
        custom_field_id=custom_field_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    custom_field_id: int = 157,
    *,
    client: Client,
) -> Response[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]:
    """/customFields/{customFieldId}

     Use this endpoint to retrieve information about a specific Custom Field available in the current
    context.

    Args:
        custom_field_id (int):  Default: 157.

    Returns:
        Response[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]
    """

    kwargs = _get_kwargs(
        custom_field_id=custom_field_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    custom_field_id: int = 157,
    *,
    client: Client,
) -> Optional[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]:
    """/customFields/{customFieldId}

     Use this endpoint to retrieve information about a specific Custom Field available in the current
    context.

    Args:
        custom_field_id (int):  Default: 157.

    Returns:
        Response[Union[CustomfieldscustomfieldidResponse200, CustomfieldscustomfieldidResponse400]]
    """

    return (
        await asyncio_detailed(
            custom_field_id=custom_field_id,
            client=client,
        )
    ).parsed
