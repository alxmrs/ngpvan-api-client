from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.onlineactionsformsformtrackingid_response_200 import OnlineactionsformsformtrackingidResponse200
from ...models.onlineactionsformsformtrackingid_response_400 import OnlineactionsformsformtrackingidResponse400
from ...models.onlineactionsformsformtrackingid_response_404 import OnlineactionsformsformtrackingidResponse404
from ...types import Response


def _get_kwargs(
    form_tracking_id: str = "TdcRQrFOH3zqmWjy9vA2",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/onlineActionsForms/{formTrackingId}".format(client.base_url, formTrackingId=form_tracking_id)

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
        OnlineactionsformsformtrackingidResponse200,
        OnlineactionsformsformtrackingidResponse400,
        OnlineactionsformsformtrackingidResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = OnlineactionsformsformtrackingidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = OnlineactionsformsformtrackingidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = OnlineactionsformsformtrackingidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        OnlineactionsformsformtrackingidResponse200,
        OnlineactionsformsformtrackingidResponse400,
        OnlineactionsformsformtrackingidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    form_tracking_id: str = "TdcRQrFOH3zqmWjy9vA2",
    *,
    client: Client,
) -> Response[
    Union[
        OnlineactionsformsformtrackingidResponse200,
        OnlineactionsformsformtrackingidResponse400,
        OnlineactionsformsformtrackingidResponse404,
    ]
]:
    """/onlineActionsForms/{formTrackingId}

     Use this endpoint to retrieve information about a specific Online Actions Form available in the
    current context.

    This endpoint accepts standard list parameters, returns a standard [Online Actions Form](ref:online-
    actions-forms#common-models-27) object.

    Args:
        form_tracking_id (str):  Default: 'TdcRQrFOH3zqmWjy9vA2'.

    Returns:
        Response[Union[OnlineactionsformsformtrackingidResponse200, OnlineactionsformsformtrackingidResponse400, OnlineactionsformsformtrackingidResponse404]]
    """

    kwargs = _get_kwargs(
        form_tracking_id=form_tracking_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    form_tracking_id: str = "TdcRQrFOH3zqmWjy9vA2",
    *,
    client: Client,
) -> Optional[
    Union[
        OnlineactionsformsformtrackingidResponse200,
        OnlineactionsformsformtrackingidResponse400,
        OnlineactionsformsformtrackingidResponse404,
    ]
]:
    """/onlineActionsForms/{formTrackingId}

     Use this endpoint to retrieve information about a specific Online Actions Form available in the
    current context.

    This endpoint accepts standard list parameters, returns a standard [Online Actions Form](ref:online-
    actions-forms#common-models-27) object.

    Args:
        form_tracking_id (str):  Default: 'TdcRQrFOH3zqmWjy9vA2'.

    Returns:
        Response[Union[OnlineactionsformsformtrackingidResponse200, OnlineactionsformsformtrackingidResponse400, OnlineactionsformsformtrackingidResponse404]]
    """

    return sync_detailed(
        form_tracking_id=form_tracking_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    form_tracking_id: str = "TdcRQrFOH3zqmWjy9vA2",
    *,
    client: Client,
) -> Response[
    Union[
        OnlineactionsformsformtrackingidResponse200,
        OnlineactionsformsformtrackingidResponse400,
        OnlineactionsformsformtrackingidResponse404,
    ]
]:
    """/onlineActionsForms/{formTrackingId}

     Use this endpoint to retrieve information about a specific Online Actions Form available in the
    current context.

    This endpoint accepts standard list parameters, returns a standard [Online Actions Form](ref:online-
    actions-forms#common-models-27) object.

    Args:
        form_tracking_id (str):  Default: 'TdcRQrFOH3zqmWjy9vA2'.

    Returns:
        Response[Union[OnlineactionsformsformtrackingidResponse200, OnlineactionsformsformtrackingidResponse400, OnlineactionsformsformtrackingidResponse404]]
    """

    kwargs = _get_kwargs(
        form_tracking_id=form_tracking_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    form_tracking_id: str = "TdcRQrFOH3zqmWjy9vA2",
    *,
    client: Client,
) -> Optional[
    Union[
        OnlineactionsformsformtrackingidResponse200,
        OnlineactionsformsformtrackingidResponse400,
        OnlineactionsformsformtrackingidResponse404,
    ]
]:
    """/onlineActionsForms/{formTrackingId}

     Use this endpoint to retrieve information about a specific Online Actions Form available in the
    current context.

    This endpoint accepts standard list parameters, returns a standard [Online Actions Form](ref:online-
    actions-forms#common-models-27) object.

    Args:
        form_tracking_id (str):  Default: 'TdcRQrFOH3zqmWjy9vA2'.

    Returns:
        Response[Union[OnlineactionsformsformtrackingidResponse200, OnlineactionsformsformtrackingidResponse400, OnlineactionsformsformtrackingidResponse404]]
    """

    return (
        await asyncio_detailed(
            form_tracking_id=form_tracking_id,
            client=client,
        )
    ).parsed
