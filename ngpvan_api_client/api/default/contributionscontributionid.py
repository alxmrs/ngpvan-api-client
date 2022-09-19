from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contributionscontributionid_response_400 import ContributionscontributionidResponse400
from ...models.contributionscontributionid_response_404 import ContributionscontributionidResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    contribution_id: int = 4482,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/contributions/{contributionId}".format(client.base_url, contributionId=contribution_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$expand"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = ContributionscontributionidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ContributionscontributionidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    contribution_id: int = 4482,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]:
    """/contributions/{contributionId}

     Retrieve a Contribution by `contributionId`

    If the specified Contribution does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        contribution_id (int):  Default: 4482.
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]
    """

    kwargs = _get_kwargs(
        contribution_id=contribution_id,
        client=client,
        expand=expand,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    contribution_id: int = 4482,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]:
    """/contributions/{contributionId}

     Retrieve a Contribution by `contributionId`

    If the specified Contribution does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        contribution_id (int):  Default: 4482.
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]
    """

    return sync_detailed(
        contribution_id=contribution_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    contribution_id: int = 4482,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]:
    """/contributions/{contributionId}

     Retrieve a Contribution by `contributionId`

    If the specified Contribution does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        contribution_id (int):  Default: 4482.
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]
    """

    kwargs = _get_kwargs(
        contribution_id=contribution_id,
        client=client,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    contribution_id: int = 4482,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]:
    """/contributions/{contributionId}

     Retrieve a Contribution by `contributionId`

    If the specified Contribution does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        contribution_id (int):  Default: 4482.
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ContributionscontributionidResponse400, ContributionscontributionidResponse404]]
    """

    return (
        await asyncio_detailed(
            contribution_id=contribution_id,
            client=client,
            expand=expand,
        )
    ).parsed
