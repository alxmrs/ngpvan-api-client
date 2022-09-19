from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.smssync_json_body import SmssyncJsonBody
from ...models.smssync_response_200 import SmssyncResponse200
from ...models.smssync_response_400 import SmssyncResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SmssyncJsonBody,
) -> Dict[str, Any]:
    url = "{}/savedLists/smsSync".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[SmssyncResponse200, SmssyncResponse400]]:
    if response.status_code == 200:
        response_200 = SmssyncResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = SmssyncResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[SmssyncResponse200, SmssyncResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SmssyncJsonBody,
) -> Response[Union[SmssyncResponse200, SmssyncResponse400]]:
    """/savedLists/smsSync

     Call this endpoint to generate a list of the contacts in NGP VAN that have been recently updated
    with new address or phone number information. The result will be an identifier of the saved list
    which can be used in the [Canvass File Requests](ref:canvass-file-requests) endpoint.

    `SyncPeriodStart` and `SyncPeriodEnd` must be no more than 36 hours apart. If the specified time
    period exceeds 36 hours an HTTP `400 Bad Request` response will be returned.

    All dates passed to the API should be in Coordinated Universal Time (UTC) and formatted according to
    ISO 8601.

    Successful requests will return an `HTTP 200` response with a JSON body containing an integer
    identifying the saved list created by the API as `SavedListId`. This should be passed as a parameter
    to the subsequent request to the Canvass File Requests API.

    Args:
        json_body (SmssyncJsonBody):

    Returns:
        Response[Union[SmssyncResponse200, SmssyncResponse400]]
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
    json_body: SmssyncJsonBody,
) -> Optional[Union[SmssyncResponse200, SmssyncResponse400]]:
    """/savedLists/smsSync

     Call this endpoint to generate a list of the contacts in NGP VAN that have been recently updated
    with new address or phone number information. The result will be an identifier of the saved list
    which can be used in the [Canvass File Requests](ref:canvass-file-requests) endpoint.

    `SyncPeriodStart` and `SyncPeriodEnd` must be no more than 36 hours apart. If the specified time
    period exceeds 36 hours an HTTP `400 Bad Request` response will be returned.

    All dates passed to the API should be in Coordinated Universal Time (UTC) and formatted according to
    ISO 8601.

    Successful requests will return an `HTTP 200` response with a JSON body containing an integer
    identifying the saved list created by the API as `SavedListId`. This should be passed as a parameter
    to the subsequent request to the Canvass File Requests API.

    Args:
        json_body (SmssyncJsonBody):

    Returns:
        Response[Union[SmssyncResponse200, SmssyncResponse400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SmssyncJsonBody,
) -> Response[Union[SmssyncResponse200, SmssyncResponse400]]:
    """/savedLists/smsSync

     Call this endpoint to generate a list of the contacts in NGP VAN that have been recently updated
    with new address or phone number information. The result will be an identifier of the saved list
    which can be used in the [Canvass File Requests](ref:canvass-file-requests) endpoint.

    `SyncPeriodStart` and `SyncPeriodEnd` must be no more than 36 hours apart. If the specified time
    period exceeds 36 hours an HTTP `400 Bad Request` response will be returned.

    All dates passed to the API should be in Coordinated Universal Time (UTC) and formatted according to
    ISO 8601.

    Successful requests will return an `HTTP 200` response with a JSON body containing an integer
    identifying the saved list created by the API as `SavedListId`. This should be passed as a parameter
    to the subsequent request to the Canvass File Requests API.

    Args:
        json_body (SmssyncJsonBody):

    Returns:
        Response[Union[SmssyncResponse200, SmssyncResponse400]]
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
    json_body: SmssyncJsonBody,
) -> Optional[Union[SmssyncResponse200, SmssyncResponse400]]:
    """/savedLists/smsSync

     Call this endpoint to generate a list of the contacts in NGP VAN that have been recently updated
    with new address or phone number information. The result will be an identifier of the saved list
    which can be used in the [Canvass File Requests](ref:canvass-file-requests) endpoint.

    `SyncPeriodStart` and `SyncPeriodEnd` must be no more than 36 hours apart. If the specified time
    period exceeds 36 hours an HTTP `400 Bad Request` response will be returned.

    All dates passed to the API should be in Coordinated Universal Time (UTC) and formatted according to
    ISO 8601.

    Successful requests will return an `HTTP 200` response with a JSON body containing an integer
    identifying the saved list created by the API as `SavedListId`. This should be passed as a parameter
    to the subsequent request to the Canvass File Requests API.

    Args:
        json_body (SmssyncJsonBody):

    Returns:
        Response[Union[SmssyncResponse200, SmssyncResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
