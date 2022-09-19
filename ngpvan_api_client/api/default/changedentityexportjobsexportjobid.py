from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.changedentityexportjobsexportjobid_response_200 import ChangedentityexportjobsexportjobidResponse200
from ...models.changedentityexportjobsexportjobid_response_400 import ChangedentityexportjobsexportjobidResponse400
from ...models.changedentityexportjobsexportjobid_response_404 import ChangedentityexportjobsexportjobidResponse404
from ...types import Response


def _get_kwargs(
    export_job_id: int = 12345,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/changedEntityExportJobs/{exportJobId}".format(client.base_url, exportJobId=export_job_id)

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
        ChangedentityexportjobsexportjobidResponse200,
        ChangedentityexportjobsexportjobidResponse400,
        ChangedentityexportjobsexportjobidResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = ChangedentityexportjobsexportjobidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ChangedentityexportjobsexportjobidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ChangedentityexportjobsexportjobidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        ChangedentityexportjobsexportjobidResponse200,
        ChangedentityexportjobsexportjobidResponse400,
        ChangedentityexportjobsexportjobidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    export_job_id: int = 12345,
    *,
    client: Client,
) -> Response[
    Union[
        ChangedentityexportjobsexportjobidResponse200,
        ChangedentityexportjobsexportjobidResponse400,
        ChangedentityexportjobsexportjobidResponse404,
    ]
]:
    """/changedEntityExportJobs/{exportJobId}

     This endpoint returns status and metadata about an existing Changed Entity Export Job, which is
    specified by the unique identifier `exportJobId`.

    Args:
        export_job_id (int):  Default: 12345.

    Returns:
        Response[Union[ChangedentityexportjobsexportjobidResponse200, ChangedentityexportjobsexportjobidResponse400, ChangedentityexportjobsexportjobidResponse404]]
    """

    kwargs = _get_kwargs(
        export_job_id=export_job_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    export_job_id: int = 12345,
    *,
    client: Client,
) -> Optional[
    Union[
        ChangedentityexportjobsexportjobidResponse200,
        ChangedentityexportjobsexportjobidResponse400,
        ChangedentityexportjobsexportjobidResponse404,
    ]
]:
    """/changedEntityExportJobs/{exportJobId}

     This endpoint returns status and metadata about an existing Changed Entity Export Job, which is
    specified by the unique identifier `exportJobId`.

    Args:
        export_job_id (int):  Default: 12345.

    Returns:
        Response[Union[ChangedentityexportjobsexportjobidResponse200, ChangedentityexportjobsexportjobidResponse400, ChangedentityexportjobsexportjobidResponse404]]
    """

    return sync_detailed(
        export_job_id=export_job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    export_job_id: int = 12345,
    *,
    client: Client,
) -> Response[
    Union[
        ChangedentityexportjobsexportjobidResponse200,
        ChangedentityexportjobsexportjobidResponse400,
        ChangedentityexportjobsexportjobidResponse404,
    ]
]:
    """/changedEntityExportJobs/{exportJobId}

     This endpoint returns status and metadata about an existing Changed Entity Export Job, which is
    specified by the unique identifier `exportJobId`.

    Args:
        export_job_id (int):  Default: 12345.

    Returns:
        Response[Union[ChangedentityexportjobsexportjobidResponse200, ChangedentityexportjobsexportjobidResponse400, ChangedentityexportjobsexportjobidResponse404]]
    """

    kwargs = _get_kwargs(
        export_job_id=export_job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    export_job_id: int = 12345,
    *,
    client: Client,
) -> Optional[
    Union[
        ChangedentityexportjobsexportjobidResponse200,
        ChangedentityexportjobsexportjobidResponse400,
        ChangedentityexportjobsexportjobidResponse404,
    ]
]:
    """/changedEntityExportJobs/{exportJobId}

     This endpoint returns status and metadata about an existing Changed Entity Export Job, which is
    specified by the unique identifier `exportJobId`.

    Args:
        export_job_id (int):  Default: 12345.

    Returns:
        Response[Union[ChangedentityexportjobsexportjobidResponse200, ChangedentityexportjobsexportjobidResponse400, ChangedentityexportjobsexportjobidResponse404]]
    """

    return (
        await asyncio_detailed(
            export_job_id=export_job_id,
            client=client,
        )
    ).parsed
