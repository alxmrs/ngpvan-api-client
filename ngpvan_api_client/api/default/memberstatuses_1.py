from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.memberstatuses_1_json_body import Memberstatuses1JsonBody
from ...models.memberstatuses_1_response_201 import Memberstatuses1Response201
from ...models.memberstatuses_1_response_400 import Memberstatuses1Response400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Memberstatuses1JsonBody,
) -> Dict[str, Any]:
    url = "{}/memberStatuses".format(client.base_url)

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
) -> Optional[Union[Memberstatuses1Response201, Memberstatuses1Response400]]:
    if response.status_code == 201:
        response_201 = Memberstatuses1Response201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Memberstatuses1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Memberstatuses1Response201, Memberstatuses1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Memberstatuses1JsonBody,
) -> Response[Union[Memberstatuses1Response201, Memberstatuses1Response400]]:
    """/memberStatuses

     Use this endpoint to create a new Member Status.

    Accepts a standard [Member Status](ref:member-statuses#common-models-24) object with no read-only
    values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Member Status object
    with the integer ID of the created Member Status in the response body. It also sets the **Location**
    header to the [location](ref:memberstatusesmemberstatusid) of the Member Status.

    Args:
        json_body (Memberstatuses1JsonBody):

    Returns:
        Response[Union[Memberstatuses1Response201, Memberstatuses1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: Memberstatuses1JsonBody,
) -> Optional[Union[Memberstatuses1Response201, Memberstatuses1Response400]]:
    """/memberStatuses

     Use this endpoint to create a new Member Status.

    Accepts a standard [Member Status](ref:member-statuses#common-models-24) object with no read-only
    values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Member Status object
    with the integer ID of the created Member Status in the response body. It also sets the **Location**
    header to the [location](ref:memberstatusesmemberstatusid) of the Member Status.

    Args:
        json_body (Memberstatuses1JsonBody):

    Returns:
        Response[Union[Memberstatuses1Response201, Memberstatuses1Response400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Memberstatuses1JsonBody,
) -> Response[Union[Memberstatuses1Response201, Memberstatuses1Response400]]:
    """/memberStatuses

     Use this endpoint to create a new Member Status.

    Accepts a standard [Member Status](ref:member-statuses#common-models-24) object with no read-only
    values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Member Status object
    with the integer ID of the created Member Status in the response body. It also sets the **Location**
    header to the [location](ref:memberstatusesmemberstatusid) of the Member Status.

    Args:
        json_body (Memberstatuses1JsonBody):

    Returns:
        Response[Union[Memberstatuses1Response201, Memberstatuses1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Memberstatuses1JsonBody,
) -> Optional[Union[Memberstatuses1Response201, Memberstatuses1Response400]]:
    """/memberStatuses

     Use this endpoint to create a new Member Status.

    Accepts a standard [Member Status](ref:member-statuses#common-models-24) object with no read-only
    values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Member Status object
    with the integer ID of the created Member Status in the response body. It also sets the **Location**
    header to the [location](ref:memberstatusesmemberstatusid) of the Member Status.

    Args:
        json_body (Memberstatuses1JsonBody):

    Returns:
        Response[Union[Memberstatuses1Response201, Memberstatuses1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
