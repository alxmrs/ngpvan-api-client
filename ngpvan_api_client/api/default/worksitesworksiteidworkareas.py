from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.worksitesworksiteidworkareas_json_body import WorksitesworksiteidworkareasJsonBody
from ...models.worksitesworksiteidworkareas_response_201 import WorksitesworksiteidworkareasResponse201
from ...models.worksitesworksiteidworkareas_response_400 import WorksitesworksiteidworkareasResponse400
from ...models.worksitesworksiteidworkareas_response_404 import WorksitesworksiteidworkareasResponse404
from ...types import Response


def _get_kwargs(
    worksite_id: str = "126",
    *,
    client: Client,
    json_body: WorksitesworksiteidworkareasJsonBody,
) -> Dict[str, Any]:
    url = "{}/worksites/{worksiteId}/workAreas".format(client.base_url, worksiteId=worksite_id)

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
        WorksitesworksiteidworkareasResponse201,
        WorksitesworksiteidworkareasResponse400,
        WorksitesworksiteidworkareasResponse404,
    ]
]:
    if response.status_code == 201:
        response_201 = WorksitesworksiteidworkareasResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = WorksitesworksiteidworkareasResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = WorksitesworksiteidworkareasResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        WorksitesworksiteidworkareasResponse201,
        WorksitesworksiteidworkareasResponse400,
        WorksitesworksiteidworkareasResponse404,
    ]
]:
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
    json_body: WorksitesworksiteidworkareasJsonBody,
) -> Response[
    Union[
        WorksitesworksiteidworkareasResponse201,
        WorksitesworksiteidworkareasResponse400,
        WorksitesworksiteidworkareasResponse404,
    ]
]:
    """/worksites/{worksiteId}/workAreas

     Use this endpoint to add a new Work Area to an existing Worksite.

    If the specified Worksite does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Work Area in the response body.

    Args:
        worksite_id (str):  Default: '126'.
        json_body (WorksitesworksiteidworkareasJsonBody):

    Returns:
        Response[Union[WorksitesworksiteidworkareasResponse201, WorksitesworksiteidworkareasResponse400, WorksitesworksiteidworkareasResponse404]]
    """

    kwargs = _get_kwargs(
        worksite_id=worksite_id,
        client=client,
        json_body=json_body,
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
    json_body: WorksitesworksiteidworkareasJsonBody,
) -> Optional[
    Union[
        WorksitesworksiteidworkareasResponse201,
        WorksitesworksiteidworkareasResponse400,
        WorksitesworksiteidworkareasResponse404,
    ]
]:
    """/worksites/{worksiteId}/workAreas

     Use this endpoint to add a new Work Area to an existing Worksite.

    If the specified Worksite does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Work Area in the response body.

    Args:
        worksite_id (str):  Default: '126'.
        json_body (WorksitesworksiteidworkareasJsonBody):

    Returns:
        Response[Union[WorksitesworksiteidworkareasResponse201, WorksitesworksiteidworkareasResponse400, WorksitesworksiteidworkareasResponse404]]
    """

    return sync_detailed(
        worksite_id=worksite_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    worksite_id: str = "126",
    *,
    client: Client,
    json_body: WorksitesworksiteidworkareasJsonBody,
) -> Response[
    Union[
        WorksitesworksiteidworkareasResponse201,
        WorksitesworksiteidworkareasResponse400,
        WorksitesworksiteidworkareasResponse404,
    ]
]:
    """/worksites/{worksiteId}/workAreas

     Use this endpoint to add a new Work Area to an existing Worksite.

    If the specified Worksite does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Work Area in the response body.

    Args:
        worksite_id (str):  Default: '126'.
        json_body (WorksitesworksiteidworkareasJsonBody):

    Returns:
        Response[Union[WorksitesworksiteidworkareasResponse201, WorksitesworksiteidworkareasResponse400, WorksitesworksiteidworkareasResponse404]]
    """

    kwargs = _get_kwargs(
        worksite_id=worksite_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    worksite_id: str = "126",
    *,
    client: Client,
    json_body: WorksitesworksiteidworkareasJsonBody,
) -> Optional[
    Union[
        WorksitesworksiteidworkareasResponse201,
        WorksitesworksiteidworkareasResponse400,
        WorksitesworksiteidworkareasResponse404,
    ]
]:
    """/worksites/{worksiteId}/workAreas

     Use this endpoint to add a new Work Area to an existing Worksite.

    If the specified Worksite does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Work Area in the response body.

    Args:
        worksite_id (str):  Default: '126'.
        json_body (WorksitesworksiteidworkareasJsonBody):

    Returns:
        Response[Union[WorksitesworksiteidworkareasResponse201, WorksitesworksiteidworkareasResponse400, WorksitesworksiteidworkareasResponse404]]
    """

    return (
        await asyncio_detailed(
            worksite_id=worksite_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
