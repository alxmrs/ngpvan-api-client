from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.commitmentscommitmentid_json_body import CommitmentscommitmentidJsonBody
from ...models.commitmentscommitmentid_response_400 import CommitmentscommitmentidResponse400
from ...models.commitmentscommitmentid_response_404 import CommitmentscommitmentidResponse404
from ...types import Response


def _get_kwargs(
    commitment_id: int = 222,
    *,
    client: Client,
    json_body: CommitmentscommitmentidJsonBody,
) -> Dict[str, Any]:
    url = "{}/commitments/{commitmentId}".format(client.base_url, commitmentId=commitment_id)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202
    if response.status_code == 400:
        response_400 = CommitmentscommitmentidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = CommitmentscommitmentidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    commitment_id: int = 222,
    *,
    client: Client,
    json_body: CommitmentscommitmentidJsonBody,
) -> Response[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]:
    """/commitments/{commitmentId}

     Use this endpoint to update a recurring commitment. You can currently:
    1. Cancel a commitment
    2. Update the next transaction date
    3. Update the commitment amount

    Please note that you **cannot** update a commitment you are attempting to cancel. **The cancellation
    will be processed first**, and any other changes will be ignored.

    Args:
        commitment_id (int):  Default: 222.
        json_body (CommitmentscommitmentidJsonBody):

    Returns:
        Response[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]
    """

    kwargs = _get_kwargs(
        commitment_id=commitment_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    commitment_id: int = 222,
    *,
    client: Client,
    json_body: CommitmentscommitmentidJsonBody,
) -> Optional[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]:
    """/commitments/{commitmentId}

     Use this endpoint to update a recurring commitment. You can currently:
    1. Cancel a commitment
    2. Update the next transaction date
    3. Update the commitment amount

    Please note that you **cannot** update a commitment you are attempting to cancel. **The cancellation
    will be processed first**, and any other changes will be ignored.

    Args:
        commitment_id (int):  Default: 222.
        json_body (CommitmentscommitmentidJsonBody):

    Returns:
        Response[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]
    """

    return sync_detailed(
        commitment_id=commitment_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    commitment_id: int = 222,
    *,
    client: Client,
    json_body: CommitmentscommitmentidJsonBody,
) -> Response[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]:
    """/commitments/{commitmentId}

     Use this endpoint to update a recurring commitment. You can currently:
    1. Cancel a commitment
    2. Update the next transaction date
    3. Update the commitment amount

    Please note that you **cannot** update a commitment you are attempting to cancel. **The cancellation
    will be processed first**, and any other changes will be ignored.

    Args:
        commitment_id (int):  Default: 222.
        json_body (CommitmentscommitmentidJsonBody):

    Returns:
        Response[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]
    """

    kwargs = _get_kwargs(
        commitment_id=commitment_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    commitment_id: int = 222,
    *,
    client: Client,
    json_body: CommitmentscommitmentidJsonBody,
) -> Optional[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]:
    """/commitments/{commitmentId}

     Use this endpoint to update a recurring commitment. You can currently:
    1. Cancel a commitment
    2. Update the next transaction date
    3. Update the commitment amount

    Please note that you **cannot** update a commitment you are attempting to cancel. **The cancellation
    will be processed first**, and any other changes will be ignored.

    Args:
        commitment_id (int):  Default: 222.
        json_body (CommitmentscommitmentidJsonBody):

    Returns:
        Response[Union[Any, CommitmentscommitmentidResponse400, CommitmentscommitmentidResponse404]]
    """

    return (
        await asyncio_detailed(
            commitment_id=commitment_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
