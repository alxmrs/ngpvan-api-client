from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.canvassfilerequests_json_body import CanvassfilerequestsJsonBody
from ...models.canvassfilerequests_response_200 import CanvassfilerequestsResponse200
from ...models.canvassfilerequests_response_400 import CanvassfilerequestsResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CanvassfilerequestsJsonBody,
) -> Dict[str, Any]:
    url = "{}/canvassFileRequests".format(client.base_url)

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
) -> Optional[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]:
    if response.status_code == 200:
        response_200 = CanvassfilerequestsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CanvassfilerequestsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CanvassfilerequestsJsonBody,
) -> Response[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]:
    """/canvassFileRequests

     Use this endpoint to create a CSV (comma-separated values) file with details of contacts from a
    saved list.

    Args:
        json_body (CanvassfilerequestsJsonBody):

    Returns:
        Response[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]
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
    json_body: CanvassfilerequestsJsonBody,
) -> Optional[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]:
    """/canvassFileRequests

     Use this endpoint to create a CSV (comma-separated values) file with details of contacts from a
    saved list.

    Args:
        json_body (CanvassfilerequestsJsonBody):

    Returns:
        Response[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CanvassfilerequestsJsonBody,
) -> Response[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]:
    """/canvassFileRequests

     Use this endpoint to create a CSV (comma-separated values) file with details of contacts from a
    saved list.

    Args:
        json_body (CanvassfilerequestsJsonBody):

    Returns:
        Response[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]
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
    json_body: CanvassfilerequestsJsonBody,
) -> Optional[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]:
    """/canvassFileRequests

     Use this endpoint to create a CSV (comma-separated values) file with details of contacts from a
    saved list.

    Args:
        json_body (CanvassfilerequestsJsonBody):

    Returns:
        Response[Union[CanvassfilerequestsResponse200, CanvassfilerequestsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
