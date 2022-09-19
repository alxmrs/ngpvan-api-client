from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.locationslocationid_1_response_400 import Locationslocationid1Response400
from ...models.locationslocationid_1_response_404 import Locationslocationid1Response404
from ...types import Response


def _get_kwargs(
    location_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/locations/{locationId}".format(client.base_url, locationId=location_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = Locationslocationid1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Locationslocationid1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    location_id: int,
    *,
    client: Client,
) -> Response[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]:
    """/locations/{locationId}

     Use this endpoint to delete an existing Location. Use with caution as this this action is
    irreversible. [Events](ref:events) associated with the given Location will continue to function
    though the [Signups](ref:signups) associated with the now deleted Location will display “Invalid
    Location” in the VAN UI.

    Args:
        location_id (int):

    Returns:
        Response[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    location_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]:
    """/locations/{locationId}

     Use this endpoint to delete an existing Location. Use with caution as this this action is
    irreversible. [Events](ref:events) associated with the given Location will continue to function
    though the [Signups](ref:signups) associated with the now deleted Location will display “Invalid
    Location” in the VAN UI.

    Args:
        location_id (int):

    Returns:
        Response[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]
    """

    return sync_detailed(
        location_id=location_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    location_id: int,
    *,
    client: Client,
) -> Response[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]:
    """/locations/{locationId}

     Use this endpoint to delete an existing Location. Use with caution as this this action is
    irreversible. [Events](ref:events) associated with the given Location will continue to function
    though the [Signups](ref:signups) associated with the now deleted Location will display “Invalid
    Location” in the VAN UI.

    Args:
        location_id (int):

    Returns:
        Response[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]
    """

    kwargs = _get_kwargs(
        location_id=location_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    location_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]:
    """/locations/{locationId}

     Use this endpoint to delete an existing Location. Use with caution as this this action is
    irreversible. [Events](ref:events) associated with the given Location will continue to function
    though the [Signups](ref:signups) associated with the now deleted Location will display “Invalid
    Location” in the VAN UI.

    Args:
        location_id (int):

    Returns:
        Response[Union[Any, Locationslocationid1Response400, Locationslocationid1Response404]]
    """

    return (
        await asyncio_detailed(
            location_id=location_id,
            client=client,
        )
    ).parsed
