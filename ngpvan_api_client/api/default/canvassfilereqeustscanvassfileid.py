from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.canvassfilereqeustscanvassfileid_response_200 import CanvassfilereqeustscanvassfileidResponse200
from ...models.canvassfilereqeustscanvassfileid_response_400 import CanvassfilereqeustscanvassfileidResponse400
from ...types import Response


def _get_kwargs(
    canvass_file_request_id: int = 123,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/canvassFileRequests/{canvassFileRequestId}".format(
        client.base_url, canvassFileRequestId=canvass_file_request_id
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
) -> Optional[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]:
    if response.status_code == 200:
        response_200 = CanvassfilereqeustscanvassfileidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CanvassfilereqeustscanvassfileidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    canvass_file_request_id: int = 123,
    *,
    client: Client,
) -> Response[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]:
    """/canvassFileRequests/{canvassFileRequestId}

     Is identical to the [message which is sent to the canvass file request's webhook](ref:canvass-file-
    requests#canvassfilerequests), if found.

    Args:
        canvass_file_request_id (int):  Default: 123.

    Returns:
        Response[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]
    """

    kwargs = _get_kwargs(
        canvass_file_request_id=canvass_file_request_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    canvass_file_request_id: int = 123,
    *,
    client: Client,
) -> Optional[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]:
    """/canvassFileRequests/{canvassFileRequestId}

     Is identical to the [message which is sent to the canvass file request's webhook](ref:canvass-file-
    requests#canvassfilerequests), if found.

    Args:
        canvass_file_request_id (int):  Default: 123.

    Returns:
        Response[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]
    """

    return sync_detailed(
        canvass_file_request_id=canvass_file_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    canvass_file_request_id: int = 123,
    *,
    client: Client,
) -> Response[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]:
    """/canvassFileRequests/{canvassFileRequestId}

     Is identical to the [message which is sent to the canvass file request's webhook](ref:canvass-file-
    requests#canvassfilerequests), if found.

    Args:
        canvass_file_request_id (int):  Default: 123.

    Returns:
        Response[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]
    """

    kwargs = _get_kwargs(
        canvass_file_request_id=canvass_file_request_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    canvass_file_request_id: int = 123,
    *,
    client: Client,
) -> Optional[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]:
    """/canvassFileRequests/{canvassFileRequestId}

     Is identical to the [message which is sent to the canvass file request's webhook](ref:canvass-file-
    requests#canvassfilerequests), if found.

    Args:
        canvass_file_request_id (int):  Default: 123.

    Returns:
        Response[Union[Any, CanvassfilereqeustscanvassfileidResponse200, CanvassfilereqeustscanvassfileidResponse400]]
    """

    return (
        await asyncio_detailed(
            canvass_file_request_id=canvass_file_request_id,
            client=client,
        )
    ).parsed
