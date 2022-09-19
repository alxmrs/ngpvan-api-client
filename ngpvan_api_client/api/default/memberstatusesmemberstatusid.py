from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.memberstatusesmemberstatusid_response_200 import MemberstatusesmemberstatusidResponse200
from ...models.memberstatusesmemberstatusid_response_400 import MemberstatusesmemberstatusidResponse400
from ...models.memberstatusesmemberstatusid_response_404 import MemberstatusesmemberstatusidResponse404
from ...types import Response


def _get_kwargs(
    member_status_id: str = "123",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/memberStatuses/{memberStatusId}".format(client.base_url, memberStatusId=member_status_id)

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
        MemberstatusesmemberstatusidResponse200,
        MemberstatusesmemberstatusidResponse400,
        MemberstatusesmemberstatusidResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = MemberstatusesmemberstatusidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = MemberstatusesmemberstatusidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = MemberstatusesmemberstatusidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        MemberstatusesmemberstatusidResponse200,
        MemberstatusesmemberstatusidResponse400,
        MemberstatusesmemberstatusidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    member_status_id: str = "123",
    *,
    client: Client,
) -> Response[
    Union[
        MemberstatusesmemberstatusidResponse200,
        MemberstatusesmemberstatusidResponse400,
        MemberstatusesmemberstatusidResponse404,
    ]
]:
    """/memberStatuses/{memberStatusId}

     Use this endpoint to retrieve the details of a specific Member Status.

    Returns a standard [Member Status](ref:member-statuses#common-models-24) object, if found.

    If the specified Member Status does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        member_status_id (str):  Default: '123'.

    Returns:
        Response[Union[MemberstatusesmemberstatusidResponse200, MemberstatusesmemberstatusidResponse400, MemberstatusesmemberstatusidResponse404]]
    """

    kwargs = _get_kwargs(
        member_status_id=member_status_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    member_status_id: str = "123",
    *,
    client: Client,
) -> Optional[
    Union[
        MemberstatusesmemberstatusidResponse200,
        MemberstatusesmemberstatusidResponse400,
        MemberstatusesmemberstatusidResponse404,
    ]
]:
    """/memberStatuses/{memberStatusId}

     Use this endpoint to retrieve the details of a specific Member Status.

    Returns a standard [Member Status](ref:member-statuses#common-models-24) object, if found.

    If the specified Member Status does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        member_status_id (str):  Default: '123'.

    Returns:
        Response[Union[MemberstatusesmemberstatusidResponse200, MemberstatusesmemberstatusidResponse400, MemberstatusesmemberstatusidResponse404]]
    """

    return sync_detailed(
        member_status_id=member_status_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    member_status_id: str = "123",
    *,
    client: Client,
) -> Response[
    Union[
        MemberstatusesmemberstatusidResponse200,
        MemberstatusesmemberstatusidResponse400,
        MemberstatusesmemberstatusidResponse404,
    ]
]:
    """/memberStatuses/{memberStatusId}

     Use this endpoint to retrieve the details of a specific Member Status.

    Returns a standard [Member Status](ref:member-statuses#common-models-24) object, if found.

    If the specified Member Status does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        member_status_id (str):  Default: '123'.

    Returns:
        Response[Union[MemberstatusesmemberstatusidResponse200, MemberstatusesmemberstatusidResponse400, MemberstatusesmemberstatusidResponse404]]
    """

    kwargs = _get_kwargs(
        member_status_id=member_status_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    member_status_id: str = "123",
    *,
    client: Client,
) -> Optional[
    Union[
        MemberstatusesmemberstatusidResponse200,
        MemberstatusesmemberstatusidResponse400,
        MemberstatusesmemberstatusidResponse404,
    ]
]:
    """/memberStatuses/{memberStatusId}

     Use this endpoint to retrieve the details of a specific Member Status.

    Returns a standard [Member Status](ref:member-statuses#common-models-24) object, if found.

    If the specified Member Status does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        member_status_id (str):  Default: '123'.

    Returns:
        Response[Union[MemberstatusesmemberstatusidResponse200, MemberstatusesmemberstatusidResponse400, MemberstatusesmemberstatusidResponse404]]
    """

    return (
        await asyncio_detailed(
            member_status_id=member_status_id,
            client=client,
        )
    ).parsed
