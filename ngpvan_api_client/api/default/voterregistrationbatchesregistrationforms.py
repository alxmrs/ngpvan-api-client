from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.voterregistrationbatchesregistrationforms_response_200 import (
    VoterregistrationbatchesregistrationformsResponse200,
)
from ...models.voterregistrationbatchesregistrationforms_response_400 import (
    VoterregistrationbatchesregistrationformsResponse400,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/voterRegistrationBatches/registrationForms".format(client.base_url)

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
) -> Optional[
    Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]
]:
    if response.status_code == 200:
        response_200 = VoterregistrationbatchesregistrationformsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = VoterregistrationbatchesregistrationformsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[
    Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]
]:
    """/voterRegistrationBatches/registrationForms

     Returns a list of registration forms available for use when creating a new voter registration batch
    via [POST /voterRegistrationBatches](ref:voter-registration-batches#voterregistrationbatches-1).

    Returns:
        Response[Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]]
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
) -> Optional[
    Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]
]:
    """/voterRegistrationBatches/registrationForms

     Returns a list of registration forms available for use when creating a new voter registration batch
    via [POST /voterRegistrationBatches](ref:voter-registration-batches#voterregistrationbatches-1).

    Returns:
        Response[Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[
    Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]
]:
    """/voterRegistrationBatches/registrationForms

     Returns a list of registration forms available for use when creating a new voter registration batch
    via [POST /voterRegistrationBatches](ref:voter-registration-batches#voterregistrationbatches-1).

    Returns:
        Response[Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]]
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
) -> Optional[
    Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]
]:
    """/voterRegistrationBatches/registrationForms

     Returns a list of registration forms available for use when creating a new voter registration batch
    via [POST /voterRegistrationBatches](ref:voter-registration-batches#voterregistrationbatches-1).

    Returns:
        Response[Union[VoterregistrationbatchesregistrationformsResponse200, VoterregistrationbatchesregistrationformsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
