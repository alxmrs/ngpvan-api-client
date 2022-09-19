from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.voterregistrationbatchesstatesstatesupportedfields_response_200 import (
    VoterregistrationbatchesstatesstatesupportedfieldsResponse200,
)
from ...models.voterregistrationbatchesstatesstatesupportedfields_response_400 import (
    VoterregistrationbatchesstatesstatesupportedfieldsResponse400,
)
from ...types import Response


def _get_kwargs(
    state: str = "MA",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/voterRegistrationBatches/states/{state}/supportedFields".format(client.base_url, state=state)

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
    Union[
        VoterregistrationbatchesstatesstatesupportedfieldsResponse200,
        VoterregistrationbatchesstatesstatesupportedfieldsResponse400,
    ]
]:
    if response.status_code == 200:
        response_200 = VoterregistrationbatchesstatesstatesupportedfieldsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = VoterregistrationbatchesstatesstatesupportedfieldsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        VoterregistrationbatchesstatesstatesupportedfieldsResponse200,
        VoterregistrationbatchesstatesstatesupportedfieldsResponse400,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    state: str = "MA",
    *,
    client: Client,
) -> Response[
    Union[
        VoterregistrationbatchesstatesstatesupportedfieldsResponse200,
        VoterregistrationbatchesstatesstatesupportedfieldsResponse400,
    ]
]:
    """/voterRegistrationBatches/states/{state}/supportedFields

     Retrieve list of fields available for use when sending registrants via [POST
    /voterRegistrationBatches/{batchId}/people](ref:voter-registration-
    batches#voterregistrationbatchesbatchidpeople). Though the fields themselves are not currently
    state-specific, the possible values for dropdown fields are state-specific.

    State must be a valid US state abbreviation.

    Args:
        state (str):  Default: 'MA'.

    Returns:
        Response[Union[VoterregistrationbatchesstatesstatesupportedfieldsResponse200, VoterregistrationbatchesstatesstatesupportedfieldsResponse400]]
    """

    kwargs = _get_kwargs(
        state=state,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    state: str = "MA",
    *,
    client: Client,
) -> Optional[
    Union[
        VoterregistrationbatchesstatesstatesupportedfieldsResponse200,
        VoterregistrationbatchesstatesstatesupportedfieldsResponse400,
    ]
]:
    """/voterRegistrationBatches/states/{state}/supportedFields

     Retrieve list of fields available for use when sending registrants via [POST
    /voterRegistrationBatches/{batchId}/people](ref:voter-registration-
    batches#voterregistrationbatchesbatchidpeople). Though the fields themselves are not currently
    state-specific, the possible values for dropdown fields are state-specific.

    State must be a valid US state abbreviation.

    Args:
        state (str):  Default: 'MA'.

    Returns:
        Response[Union[VoterregistrationbatchesstatesstatesupportedfieldsResponse200, VoterregistrationbatchesstatesstatesupportedfieldsResponse400]]
    """

    return sync_detailed(
        state=state,
        client=client,
    ).parsed


async def asyncio_detailed(
    state: str = "MA",
    *,
    client: Client,
) -> Response[
    Union[
        VoterregistrationbatchesstatesstatesupportedfieldsResponse200,
        VoterregistrationbatchesstatesstatesupportedfieldsResponse400,
    ]
]:
    """/voterRegistrationBatches/states/{state}/supportedFields

     Retrieve list of fields available for use when sending registrants via [POST
    /voterRegistrationBatches/{batchId}/people](ref:voter-registration-
    batches#voterregistrationbatchesbatchidpeople). Though the fields themselves are not currently
    state-specific, the possible values for dropdown fields are state-specific.

    State must be a valid US state abbreviation.

    Args:
        state (str):  Default: 'MA'.

    Returns:
        Response[Union[VoterregistrationbatchesstatesstatesupportedfieldsResponse200, VoterregistrationbatchesstatesstatesupportedfieldsResponse400]]
    """

    kwargs = _get_kwargs(
        state=state,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    state: str = "MA",
    *,
    client: Client,
) -> Optional[
    Union[
        VoterregistrationbatchesstatesstatesupportedfieldsResponse200,
        VoterregistrationbatchesstatesstatesupportedfieldsResponse400,
    ]
]:
    """/voterRegistrationBatches/states/{state}/supportedFields

     Retrieve list of fields available for use when sending registrants via [POST
    /voterRegistrationBatches/{batchId}/people](ref:voter-registration-
    batches#voterregistrationbatchesbatchidpeople). Though the fields themselves are not currently
    state-specific, the possible values for dropdown fields are state-specific.

    State must be a valid US state abbreviation.

    Args:
        state (str):  Default: 'MA'.

    Returns:
        Response[Union[VoterregistrationbatchesstatesstatesupportedfieldsResponse200, VoterregistrationbatchesstatesstatesupportedfieldsResponse400]]
    """

    return (
        await asyncio_detailed(
            state=state,
            client=client,
        )
    ).parsed
