from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contributionscontributionidattributionsvanid_1_response_400 import (
    Contributionscontributionidattributionsvanid1Response400,
)
from ...models.contributionscontributionidattributionsvanid_1_response_404 import (
    Contributionscontributionidattributionsvanid1Response404,
)
from ...types import Response


def _get_kwargs(
    contribution_id: int = 4482,
    van_id: str = "215501",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/contributions/{contributionId}/attributions/{vanId}".format(
        client.base_url, contributionId=contribution_id, vanId=van_id
    )

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
) -> Optional[
    Union[
        Any,
        Contributionscontributionidattributionsvanid1Response400,
        Contributionscontributionidattributionsvanid1Response404,
    ]
]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = Contributionscontributionidattributionsvanid1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Contributionscontributionidattributionsvanid1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        Any,
        Contributionscontributionidattributionsvanid1Response400,
        Contributionscontributionidattributionsvanid1Response404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    contribution_id: int = 4482,
    van_id: str = "215501",
    *,
    client: Client,
) -> Response[
    Union[
        Any,
        Contributionscontributionidattributionsvanid1Response400,
        Contributionscontributionidattributionsvanid1Response404,
    ]
]:
    """/contributions/{contributionId}/attributions/{vanId}

     Use this endpoint to delete an Attribution for a Person from a Contribution.

    Args:
        contribution_id (int):  Default: 4482.
        van_id (str):  Default: '215501'.

    Returns:
        Response[Union[Any, Contributionscontributionidattributionsvanid1Response400, Contributionscontributionidattributionsvanid1Response404]]
    """

    kwargs = _get_kwargs(
        contribution_id=contribution_id,
        van_id=van_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    contribution_id: int = 4482,
    van_id: str = "215501",
    *,
    client: Client,
) -> Optional[
    Union[
        Any,
        Contributionscontributionidattributionsvanid1Response400,
        Contributionscontributionidattributionsvanid1Response404,
    ]
]:
    """/contributions/{contributionId}/attributions/{vanId}

     Use this endpoint to delete an Attribution for a Person from a Contribution.

    Args:
        contribution_id (int):  Default: 4482.
        van_id (str):  Default: '215501'.

    Returns:
        Response[Union[Any, Contributionscontributionidattributionsvanid1Response400, Contributionscontributionidattributionsvanid1Response404]]
    """

    return sync_detailed(
        contribution_id=contribution_id,
        van_id=van_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    contribution_id: int = 4482,
    van_id: str = "215501",
    *,
    client: Client,
) -> Response[
    Union[
        Any,
        Contributionscontributionidattributionsvanid1Response400,
        Contributionscontributionidattributionsvanid1Response404,
    ]
]:
    """/contributions/{contributionId}/attributions/{vanId}

     Use this endpoint to delete an Attribution for a Person from a Contribution.

    Args:
        contribution_id (int):  Default: 4482.
        van_id (str):  Default: '215501'.

    Returns:
        Response[Union[Any, Contributionscontributionidattributionsvanid1Response400, Contributionscontributionidattributionsvanid1Response404]]
    """

    kwargs = _get_kwargs(
        contribution_id=contribution_id,
        van_id=van_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    contribution_id: int = 4482,
    van_id: str = "215501",
    *,
    client: Client,
) -> Optional[
    Union[
        Any,
        Contributionscontributionidattributionsvanid1Response400,
        Contributionscontributionidattributionsvanid1Response404,
    ]
]:
    """/contributions/{contributionId}/attributions/{vanId}

     Use this endpoint to delete an Attribution for a Person from a Contribution.

    Args:
        contribution_id (int):  Default: 4482.
        van_id (str):  Default: '215501'.

    Returns:
        Response[Union[Any, Contributionscontributionidattributionsvanid1Response400, Contributionscontributionidattributionsvanid1Response404]]
    """

    return (
        await asyncio_detailed(
            contribution_id=contribution_id,
            van_id=van_id,
            client=client,
        )
    ).parsed
