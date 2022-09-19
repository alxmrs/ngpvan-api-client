from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.voterregistrationbatchesbatchid_json_body import VoterregistrationbatchesbatchidJsonBody
from ...models.voterregistrationbatchesbatchid_response_400 import VoterregistrationbatchesbatchidResponse400
from ...types import Response


def _get_kwargs(
    batch_id: int = 100,
    *,
    client: Client,
    json_body: VoterregistrationbatchesbatchidJsonBody,
) -> Dict[str, Any]:
    url = "{}/voterRegistrationBatches/{batchId}".format(client.base_url, batchId=batch_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, VoterregistrationbatchesbatchidResponse400]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = VoterregistrationbatchesbatchidResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, VoterregistrationbatchesbatchidResponse400]]:
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
    json_body: VoterregistrationbatchesbatchidJsonBody,
) -> Response[Union[Any, VoterregistrationbatchesbatchidResponse400]]:
    """/voterRegistrationBatches/{batchId}

     Update the status of a voter registration batch.

    The current status of the specified batch dictates which batch status values are valid. When a new
    batch is created via `POST /voterRegistrationBatches`, it is set to the default status of Entering.
    From Entering, a batch can only change to Completed. Then, from Completed, a batch can either be
    changed back to Entering or to Committed. Once a batch is committed, it cannot be changed to any
    other status. No other status values are accepted.

    Changing a status to Committed processes the batch and makes registrants available for searching in
    the VAN interface.

    Args:
        batch_id (int):  Default: 100.
        json_body (VoterregistrationbatchesbatchidJsonBody):

    Returns:
        Response[Union[Any, VoterregistrationbatchesbatchidResponse400]]
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
    json_body: VoterregistrationbatchesbatchidJsonBody,
) -> Optional[Union[Any, VoterregistrationbatchesbatchidResponse400]]:
    """/voterRegistrationBatches/{batchId}

     Update the status of a voter registration batch.

    The current status of the specified batch dictates which batch status values are valid. When a new
    batch is created via `POST /voterRegistrationBatches`, it is set to the default status of Entering.
    From Entering, a batch can only change to Completed. Then, from Completed, a batch can either be
    changed back to Entering or to Committed. Once a batch is committed, it cannot be changed to any
    other status. No other status values are accepted.

    Changing a status to Committed processes the batch and makes registrants available for searching in
    the VAN interface.

    Args:
        batch_id (int):  Default: 100.
        json_body (VoterregistrationbatchesbatchidJsonBody):

    Returns:
        Response[Union[Any, VoterregistrationbatchesbatchidResponse400]]
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
    json_body: VoterregistrationbatchesbatchidJsonBody,
) -> Response[Union[Any, VoterregistrationbatchesbatchidResponse400]]:
    """/voterRegistrationBatches/{batchId}

     Update the status of a voter registration batch.

    The current status of the specified batch dictates which batch status values are valid. When a new
    batch is created via `POST /voterRegistrationBatches`, it is set to the default status of Entering.
    From Entering, a batch can only change to Completed. Then, from Completed, a batch can either be
    changed back to Entering or to Committed. Once a batch is committed, it cannot be changed to any
    other status. No other status values are accepted.

    Changing a status to Committed processes the batch and makes registrants available for searching in
    the VAN interface.

    Args:
        batch_id (int):  Default: 100.
        json_body (VoterregistrationbatchesbatchidJsonBody):

    Returns:
        Response[Union[Any, VoterregistrationbatchesbatchidResponse400]]
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
    json_body: VoterregistrationbatchesbatchidJsonBody,
) -> Optional[Union[Any, VoterregistrationbatchesbatchidResponse400]]:
    """/voterRegistrationBatches/{batchId}

     Update the status of a voter registration batch.

    The current status of the specified batch dictates which batch status values are valid. When a new
    batch is created via `POST /voterRegistrationBatches`, it is set to the default status of Entering.
    From Entering, a batch can only change to Completed. Then, from Completed, a batch can either be
    changed back to Entering or to Committed. Once a batch is committed, it cannot be changed to any
    other status. No other status values are accepted.

    Changing a status to Committed processes the batch and makes registrants available for searching in
    the VAN interface.

    Args:
        batch_id (int):  Default: 100.
        json_body (VoterregistrationbatchesbatchidJsonBody):

    Returns:
        Response[Union[Any, VoterregistrationbatchesbatchidResponse400]]
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
