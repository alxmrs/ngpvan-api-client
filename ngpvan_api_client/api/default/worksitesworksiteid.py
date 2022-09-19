from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.worksitesworksiteid_response_400 import WorksitesworksiteidResponse400
from ...models.worksitesworksiteid_response_404 import WorksitesworksiteidResponse404
from ...types import Response


def _get_kwargs(
    worksite_id: str = "126",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/worksites/{worksiteId}".format(client.base_url, worksiteId=worksite_id)

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
) -> Optional[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = WorksitesworksiteidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = WorksitesworksiteidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    worksite_id: str = "126",
    *,
    client: Client,
) -> Response[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]:
    """/worksites/{worksiteId}

     Use this endpoint to retrieve information about a specific Worksite available in the current
    context.

    A standard [Worksite](ref:worksites#common-models-16) object, if found.

    If the specified Worksite does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        worksite_id (str):  Default: '126'.

    Returns:
        Response[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]
    """

    kwargs = _get_kwargs(
        worksite_id=worksite_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    worksite_id: str = "126",
    *,
    client: Client,
) -> Optional[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]:
    """/worksites/{worksiteId}

     Use this endpoint to retrieve information about a specific Worksite available in the current
    context.

    A standard [Worksite](ref:worksites#common-models-16) object, if found.

    If the specified Worksite does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        worksite_id (str):  Default: '126'.

    Returns:
        Response[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]
    """

    return sync_detailed(
        worksite_id=worksite_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    worksite_id: str = "126",
    *,
    client: Client,
) -> Response[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]:
    """/worksites/{worksiteId}

     Use this endpoint to retrieve information about a specific Worksite available in the current
    context.

    A standard [Worksite](ref:worksites#common-models-16) object, if found.

    If the specified Worksite does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        worksite_id (str):  Default: '126'.

    Returns:
        Response[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]
    """

    kwargs = _get_kwargs(
        worksite_id=worksite_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    worksite_id: str = "126",
    *,
    client: Client,
) -> Optional[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]:
    """/worksites/{worksiteId}

     Use this endpoint to retrieve information about a specific Worksite available in the current
    context.

    A standard [Worksite](ref:worksites#common-models-16) object, if found.

    If the specified Worksite does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        worksite_id (str):  Default: '126'.

    Returns:
        Response[Union[Any, WorksitesworksiteidResponse400, WorksitesworksiteidResponse404]]
    """

    return (
        await asyncio_detailed(
            worksite_id=worksite_id,
            client=client,
        )
    ).parsed
