from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.targetexportjobs_json_body import TargetexportjobsJsonBody
from ...models.targetexportjobs_response_201 import TargetexportjobsResponse201
from ...models.targetexportjobs_response_400 import TargetexportjobsResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: TargetexportjobsJsonBody,
) -> Dict[str, Any]:
    url = "{}/targetExportJobs".format(client.base_url)

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
) -> Optional[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]:
    if response.status_code == 201:
        response_201 = TargetexportjobsResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = TargetexportjobsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: TargetexportjobsJsonBody,
) -> Response[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]:
    """/targetExportJobs

     Use this endpoint to request a new Target Export Job for a specified [Target](ref:targets).

    Args:
        json_body (TargetexportjobsJsonBody):

    Returns:
        Response[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]
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
    json_body: TargetexportjobsJsonBody,
) -> Optional[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]:
    """/targetExportJobs

     Use this endpoint to request a new Target Export Job for a specified [Target](ref:targets).

    Args:
        json_body (TargetexportjobsJsonBody):

    Returns:
        Response[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: TargetexportjobsJsonBody,
) -> Response[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]:
    """/targetExportJobs

     Use this endpoint to request a new Target Export Job for a specified [Target](ref:targets).

    Args:
        json_body (TargetexportjobsJsonBody):

    Returns:
        Response[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]
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
    json_body: TargetexportjobsJsonBody,
) -> Optional[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]:
    """/targetExportJobs

     Use this endpoint to request a new Target Export Job for a specified [Target](ref:targets).

    Args:
        json_body (TargetexportjobsJsonBody):

    Returns:
        Response[Union[TargetexportjobsResponse201, TargetexportjobsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
