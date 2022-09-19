from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contributionscontributionidattributionsvanid_json_body import (
    ContributionscontributionidattributionsvanidJsonBody,
)
from ...models.contributionscontributionidattributionsvanid_response_400 import (
    ContributionscontributionidattributionsvanidResponse400,
)
from ...models.contributionscontributionidattributionsvanid_response_404 import (
    ContributionscontributionidattributionsvanidResponse404,
)
from ...types import Response


def _get_kwargs(
    contribution_id: int = 4482,
    van_id: str = "215501",
    *,
    client: Client,
    json_body: ContributionscontributionidattributionsvanidJsonBody,
) -> Dict[str, Any]:
    url = "{}/contributions/{contributionId}/attributions/{vanId}".format(
        client.base_url, contributionId=contribution_id, vanId=van_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[
        Any,
        ContributionscontributionidattributionsvanidResponse400,
        ContributionscontributionidattributionsvanidResponse404,
    ]
]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = ContributionscontributionidattributionsvanidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ContributionscontributionidattributionsvanidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        Any,
        ContributionscontributionidattributionsvanidResponse400,
        ContributionscontributionidattributionsvanidResponse404,
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
    json_body: ContributionscontributionidattributionsvanidJsonBody,
) -> Response[
    Union[
        Any,
        ContributionscontributionidattributionsvanidResponse400,
        ContributionscontributionidattributionsvanidResponse404,
    ]
]:
    """/contributions/{contributionId}/attributions/{vanId}

     Create or update an Attribution record on the given Contribution for a Person.

    If there is an existing Attribution for the given Person on the given Contribution, it will be
    updated to match the Attribution provided with this request. If there is not an existing
    Attribution, one will be created.

    Accepts an [Attribution](ref:contributions#attributions) object. The `vanId` property of the
    Attribution object must match the value of the `vanId` parameter provided in the route. If
    `amountAttributed` is not provided, it will default to the remaining amount of the Contribution. If
    `attributionType` is not provided, it will default to `DefaultAttribution`.


    If the specified Contribution or Person does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` if an existing
    Attribution has been updated. If a new Attribution has been created, this endpoint responds with
    HTTP Status Code `201 Created`.

    Args:
        contribution_id (int):  Default: 4482.
        van_id (str):  Default: '215501'.
        json_body (ContributionscontributionidattributionsvanidJsonBody):

    Returns:
        Response[Union[Any, ContributionscontributionidattributionsvanidResponse400, ContributionscontributionidattributionsvanidResponse404]]
    """

    kwargs = _get_kwargs(
        contribution_id=contribution_id,
        van_id=van_id,
        client=client,
        json_body=json_body,
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
    json_body: ContributionscontributionidattributionsvanidJsonBody,
) -> Optional[
    Union[
        Any,
        ContributionscontributionidattributionsvanidResponse400,
        ContributionscontributionidattributionsvanidResponse404,
    ]
]:
    """/contributions/{contributionId}/attributions/{vanId}

     Create or update an Attribution record on the given Contribution for a Person.

    If there is an existing Attribution for the given Person on the given Contribution, it will be
    updated to match the Attribution provided with this request. If there is not an existing
    Attribution, one will be created.

    Accepts an [Attribution](ref:contributions#attributions) object. The `vanId` property of the
    Attribution object must match the value of the `vanId` parameter provided in the route. If
    `amountAttributed` is not provided, it will default to the remaining amount of the Contribution. If
    `attributionType` is not provided, it will default to `DefaultAttribution`.


    If the specified Contribution or Person does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` if an existing
    Attribution has been updated. If a new Attribution has been created, this endpoint responds with
    HTTP Status Code `201 Created`.

    Args:
        contribution_id (int):  Default: 4482.
        van_id (str):  Default: '215501'.
        json_body (ContributionscontributionidattributionsvanidJsonBody):

    Returns:
        Response[Union[Any, ContributionscontributionidattributionsvanidResponse400, ContributionscontributionidattributionsvanidResponse404]]
    """

    return sync_detailed(
        contribution_id=contribution_id,
        van_id=van_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    contribution_id: int = 4482,
    van_id: str = "215501",
    *,
    client: Client,
    json_body: ContributionscontributionidattributionsvanidJsonBody,
) -> Response[
    Union[
        Any,
        ContributionscontributionidattributionsvanidResponse400,
        ContributionscontributionidattributionsvanidResponse404,
    ]
]:
    """/contributions/{contributionId}/attributions/{vanId}

     Create or update an Attribution record on the given Contribution for a Person.

    If there is an existing Attribution for the given Person on the given Contribution, it will be
    updated to match the Attribution provided with this request. If there is not an existing
    Attribution, one will be created.

    Accepts an [Attribution](ref:contributions#attributions) object. The `vanId` property of the
    Attribution object must match the value of the `vanId` parameter provided in the route. If
    `amountAttributed` is not provided, it will default to the remaining amount of the Contribution. If
    `attributionType` is not provided, it will default to `DefaultAttribution`.


    If the specified Contribution or Person does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` if an existing
    Attribution has been updated. If a new Attribution has been created, this endpoint responds with
    HTTP Status Code `201 Created`.

    Args:
        contribution_id (int):  Default: 4482.
        van_id (str):  Default: '215501'.
        json_body (ContributionscontributionidattributionsvanidJsonBody):

    Returns:
        Response[Union[Any, ContributionscontributionidattributionsvanidResponse400, ContributionscontributionidattributionsvanidResponse404]]
    """

    kwargs = _get_kwargs(
        contribution_id=contribution_id,
        van_id=van_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    contribution_id: int = 4482,
    van_id: str = "215501",
    *,
    client: Client,
    json_body: ContributionscontributionidattributionsvanidJsonBody,
) -> Optional[
    Union[
        Any,
        ContributionscontributionidattributionsvanidResponse400,
        ContributionscontributionidattributionsvanidResponse404,
    ]
]:
    """/contributions/{contributionId}/attributions/{vanId}

     Create or update an Attribution record on the given Contribution for a Person.

    If there is an existing Attribution for the given Person on the given Contribution, it will be
    updated to match the Attribution provided with this request. If there is not an existing
    Attribution, one will be created.

    Accepts an [Attribution](ref:contributions#attributions) object. The `vanId` property of the
    Attribution object must match the value of the `vanId` parameter provided in the route. If
    `amountAttributed` is not provided, it will default to the remaining amount of the Contribution. If
    `attributionType` is not provided, it will default to `DefaultAttribution`.


    If the specified Contribution or Person does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` if an existing
    Attribution has been updated. If a new Attribution has been created, this endpoint responds with
    HTTP Status Code `201 Created`.

    Args:
        contribution_id (int):  Default: 4482.
        van_id (str):  Default: '215501'.
        json_body (ContributionscontributionidattributionsvanidJsonBody):

    Returns:
        Response[Union[Any, ContributionscontributionidattributionsvanidResponse400, ContributionscontributionidattributionsvanidResponse404]]
    """

    return (
        await asyncio_detailed(
            contribution_id=contribution_id,
            van_id=van_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
