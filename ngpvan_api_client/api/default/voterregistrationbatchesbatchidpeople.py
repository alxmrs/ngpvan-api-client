from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.voterregistrationbatchesbatchidpeople_json_body import VoterregistrationbatchesbatchidpeopleJsonBody
from ...models.voterregistrationbatchesbatchidpeople_response_200_item import (
    VoterregistrationbatchesbatchidpeopleResponse200Item,
)
from ...models.voterregistrationbatchesbatchidpeople_response_400 import (
    VoterregistrationbatchesbatchidpeopleResponse400,
)
from ...types import Response


def _get_kwargs(
    batch_id: int = 100,
    *,
    client: Client,
    json_body: VoterregistrationbatchesbatchidpeopleJsonBody,
) -> Dict[str, Any]:
    url = "{}/voterRegistrationBatches/{batchId}/people".format(client.base_url, batchId=batch_id)

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
) -> Optional[
    Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VoterregistrationbatchesbatchidpeopleResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = VoterregistrationbatchesbatchidpeopleResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    batch_id: int = 100,
    *,
    client: Client,
    json_body: VoterregistrationbatchesbatchidpeopleJsonBody,
) -> Response[
    Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]
]:
    """/voterRegistrationBatches/{batchId}/people

     Add Registrants to a Voter Registration Batch

    *Description*

    Use this endpoint to submit up to 25 registrants to a Voter Registration Batch. Fields published via
    `POST /voterRegistrationBatches` should be specified in CustomProperties.

    Args:
        batch_id (int):  Default: 100.
        json_body (VoterregistrationbatchesbatchidpeopleJsonBody):

    Returns:
        Response[Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    batch_id: int = 100,
    *,
    client: Client,
    json_body: VoterregistrationbatchesbatchidpeopleJsonBody,
) -> Optional[
    Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]
]:
    """/voterRegistrationBatches/{batchId}/people

     Add Registrants to a Voter Registration Batch

    *Description*

    Use this endpoint to submit up to 25 registrants to a Voter Registration Batch. Fields published via
    `POST /voterRegistrationBatches` should be specified in CustomProperties.

    Args:
        batch_id (int):  Default: 100.
        json_body (VoterregistrationbatchesbatchidpeopleJsonBody):

    Returns:
        Response[Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]]
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    batch_id: int = 100,
    *,
    client: Client,
    json_body: VoterregistrationbatchesbatchidpeopleJsonBody,
) -> Response[
    Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]
]:
    """/voterRegistrationBatches/{batchId}/people

     Add Registrants to a Voter Registration Batch

    *Description*

    Use this endpoint to submit up to 25 registrants to a Voter Registration Batch. Fields published via
    `POST /voterRegistrationBatches` should be specified in CustomProperties.

    Args:
        batch_id (int):  Default: 100.
        json_body (VoterregistrationbatchesbatchidpeopleJsonBody):

    Returns:
        Response[Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    batch_id: int = 100,
    *,
    client: Client,
    json_body: VoterregistrationbatchesbatchidpeopleJsonBody,
) -> Optional[
    Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]
]:
    """/voterRegistrationBatches/{batchId}/people

     Add Registrants to a Voter Registration Batch

    *Description*

    Use this endpoint to submit up to 25 registrants to a Voter Registration Batch. Fields published via
    `POST /voterRegistrationBatches` should be specified in CustomProperties.

    Args:
        batch_id (int):  Default: 100.
        json_body (VoterregistrationbatchesbatchidpeopleJsonBody):

    Returns:
        Response[Union[List[VoterregistrationbatchesbatchidpeopleResponse200Item], VoterregistrationbatchesbatchidpeopleResponse400]]
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
