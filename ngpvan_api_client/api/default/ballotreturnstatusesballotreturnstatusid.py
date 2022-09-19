from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ballotreturnstatusesballotreturnstatusid_response_200 import (
    BallotreturnstatusesballotreturnstatusidResponse200,
)
from ...models.ballotreturnstatusesballotreturnstatusid_response_400 import (
    BallotreturnstatusesballotreturnstatusidResponse400,
)
from ...types import Response


def _get_kwargs(
    ballot_return_status_id: int = 14,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ballotReturnStatuses/{ballotReturnStatusId}".format(
        client.base_url, ballotReturnStatusId=ballot_return_status_id
    )

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
    Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]
]:
    if response.status_code == 200:
        response_200 = BallotreturnstatusesballotreturnstatusidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BallotreturnstatusesballotreturnstatusidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    ballot_return_status_id: int = 14,
    *,
    client: Client,
) -> Response[
    Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]
]:
    """/ballotReturnStatuses/{ballotReturnStatusId}

     Retrieve ballot return status if it is available

    Use this endpoint to retrieve information about a specific Ballot Return Status available in the
    current context.

    Args:
        ballot_return_status_id (int):  Default: 14.

    Returns:
        Response[Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]]
    """

    kwargs = _get_kwargs(
        ballot_return_status_id=ballot_return_status_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    ballot_return_status_id: int = 14,
    *,
    client: Client,
) -> Optional[
    Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]
]:
    """/ballotReturnStatuses/{ballotReturnStatusId}

     Retrieve ballot return status if it is available

    Use this endpoint to retrieve information about a specific Ballot Return Status available in the
    current context.

    Args:
        ballot_return_status_id (int):  Default: 14.

    Returns:
        Response[Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]]
    """

    return sync_detailed(
        ballot_return_status_id=ballot_return_status_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ballot_return_status_id: int = 14,
    *,
    client: Client,
) -> Response[
    Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]
]:
    """/ballotReturnStatuses/{ballotReturnStatusId}

     Retrieve ballot return status if it is available

    Use this endpoint to retrieve information about a specific Ballot Return Status available in the
    current context.

    Args:
        ballot_return_status_id (int):  Default: 14.

    Returns:
        Response[Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]]
    """

    kwargs = _get_kwargs(
        ballot_return_status_id=ballot_return_status_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    ballot_return_status_id: int = 14,
    *,
    client: Client,
) -> Optional[
    Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]
]:
    """/ballotReturnStatuses/{ballotReturnStatusId}

     Retrieve ballot return status if it is available

    Use this endpoint to retrieve information about a specific Ballot Return Status available in the
    current context.

    Args:
        ballot_return_status_id (int):  Default: 14.

    Returns:
        Response[Union[Any, BallotreturnstatusesballotreturnstatusidResponse200, BallotreturnstatusesballotreturnstatusidResponse400]]
    """

    return (
        await asyncio_detailed(
            ballot_return_status_id=ballot_return_status_id,
            client=client,
        )
    ).parsed
