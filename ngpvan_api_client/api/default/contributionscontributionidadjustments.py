from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contributionscontributionidadjustments_json_body import ContributionscontributionidadjustmentsJsonBody
from ...models.contributionscontributionidadjustments_response_200 import (
    ContributionscontributionidadjustmentsResponse200,
)
from ...models.contributionscontributionidadjustments_response_400 import (
    ContributionscontributionidadjustmentsResponse400,
)
from ...models.contributionscontributionidadjustments_response_404 import (
    ContributionscontributionidadjustmentsResponse404,
)
from ...types import Response


def _get_kwargs(
    contribution_id: int = 4482,
    *,
    client: Client,
    json_body: ContributionscontributionidadjustmentsJsonBody,
) -> Dict[str, Any]:
    url = "{}/contributions/{contributionId}/adjustments".format(client.base_url, contributionId=contribution_id)

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
    Union[
        Any,
        ContributionscontributionidadjustmentsResponse200,
        ContributionscontributionidadjustmentsResponse400,
        ContributionscontributionidadjustmentsResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = ContributionscontributionidadjustmentsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ContributionscontributionidadjustmentsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ContributionscontributionidadjustmentsResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        Any,
        ContributionscontributionidadjustmentsResponse200,
        ContributionscontributionidadjustmentsResponse400,
        ContributionscontributionidadjustmentsResponse404,
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
    *,
    client: Client,
    json_body: ContributionscontributionidadjustmentsJsonBody,
) -> Response[
    Union[
        Any,
        ContributionscontributionidadjustmentsResponse200,
        ContributionscontributionidadjustmentsResponse400,
        ContributionscontributionidadjustmentsResponse404,
    ]
]:
    """/contributions/{contributionId}/adjustments

     Use this endpoint to adjust an existing contribution with the properties provided in the request
    body. Only contributions processed by the CRM are supported.

    **Currently “Refund” is the only adjustment type supported by the API. Using this adjustment type
    will issue a refund to the donor.**

    Args:
        contribution_id (int):  Default: 4482.
        json_body (ContributionscontributionidadjustmentsJsonBody):

    Returns:
        Response[Union[Any, ContributionscontributionidadjustmentsResponse200, ContributionscontributionidadjustmentsResponse400, ContributionscontributionidadjustmentsResponse404]]
    """

    kwargs = _get_kwargs(
        contribution_id=contribution_id,
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
    *,
    client: Client,
    json_body: ContributionscontributionidadjustmentsJsonBody,
) -> Optional[
    Union[
        Any,
        ContributionscontributionidadjustmentsResponse200,
        ContributionscontributionidadjustmentsResponse400,
        ContributionscontributionidadjustmentsResponse404,
    ]
]:
    """/contributions/{contributionId}/adjustments

     Use this endpoint to adjust an existing contribution with the properties provided in the request
    body. Only contributions processed by the CRM are supported.

    **Currently “Refund” is the only adjustment type supported by the API. Using this adjustment type
    will issue a refund to the donor.**

    Args:
        contribution_id (int):  Default: 4482.
        json_body (ContributionscontributionidadjustmentsJsonBody):

    Returns:
        Response[Union[Any, ContributionscontributionidadjustmentsResponse200, ContributionscontributionidadjustmentsResponse400, ContributionscontributionidadjustmentsResponse404]]
    """

    return sync_detailed(
        contribution_id=contribution_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    contribution_id: int = 4482,
    *,
    client: Client,
    json_body: ContributionscontributionidadjustmentsJsonBody,
) -> Response[
    Union[
        Any,
        ContributionscontributionidadjustmentsResponse200,
        ContributionscontributionidadjustmentsResponse400,
        ContributionscontributionidadjustmentsResponse404,
    ]
]:
    """/contributions/{contributionId}/adjustments

     Use this endpoint to adjust an existing contribution with the properties provided in the request
    body. Only contributions processed by the CRM are supported.

    **Currently “Refund” is the only adjustment type supported by the API. Using this adjustment type
    will issue a refund to the donor.**

    Args:
        contribution_id (int):  Default: 4482.
        json_body (ContributionscontributionidadjustmentsJsonBody):

    Returns:
        Response[Union[Any, ContributionscontributionidadjustmentsResponse200, ContributionscontributionidadjustmentsResponse400, ContributionscontributionidadjustmentsResponse404]]
    """

    kwargs = _get_kwargs(
        contribution_id=contribution_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    contribution_id: int = 4482,
    *,
    client: Client,
    json_body: ContributionscontributionidadjustmentsJsonBody,
) -> Optional[
    Union[
        Any,
        ContributionscontributionidadjustmentsResponse200,
        ContributionscontributionidadjustmentsResponse400,
        ContributionscontributionidadjustmentsResponse404,
    ]
]:
    """/contributions/{contributionId}/adjustments

     Use this endpoint to adjust an existing contribution with the properties provided in the request
    body. Only contributions processed by the CRM are supported.

    **Currently “Refund” is the only adjustment type supported by the API. Using this adjustment type
    will issue a refund to the donor.**

    Args:
        contribution_id (int):  Default: 4482.
        json_body (ContributionscontributionidadjustmentsJsonBody):

    Returns:
        Response[Union[Any, ContributionscontributionidadjustmentsResponse200, ContributionscontributionidadjustmentsResponse400, ContributionscontributionidadjustmentsResponse404]]
    """

    return (
        await asyncio_detailed(
            contribution_id=contribution_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
