from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.targetexportjobsexportjobid_response_200 import TargetexportjobsexportjobidResponse200
from ...models.targetexportjobsexportjobid_response_400 import TargetexportjobsexportjobidResponse400
from ...models.targetexportjobsexportjobid_response_404 import TargetexportjobsexportjobidResponse404
from ...types import Response


def _get_kwargs(
    export_job_id: int = 1234,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/targetExportJobs/{exportJobId}".format(client.base_url, exportJobId=export_job_id)

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
        TargetexportjobsexportjobidResponse200,
        TargetexportjobsexportjobidResponse400,
        TargetexportjobsexportjobidResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = TargetexportjobsexportjobidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = TargetexportjobsexportjobidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = TargetexportjobsexportjobidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        TargetexportjobsexportjobidResponse200,
        TargetexportjobsexportjobidResponse400,
        TargetexportjobsexportjobidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    export_job_id: int = 1234,
    *,
    client: Client,
) -> Response[
    Union[
        TargetexportjobsexportjobidResponse200,
        TargetexportjobsexportjobidResponse400,
        TargetexportjobsexportjobidResponse404,
    ]
]:
    """/targetExportJobs/{exportJobId}

     Use this endpoint to retrieve information about the status of a specific Target Export Job available
    in the current context.

    Args:
        export_job_id (int):  Default: 1234.

    Returns:
        Response[Union[TargetexportjobsexportjobidResponse200, TargetexportjobsexportjobidResponse400, TargetexportjobsexportjobidResponse404]]
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
    export_job_id: int = 1234,
    *,
    client: Client,
) -> Optional[
    Union[
        TargetexportjobsexportjobidResponse200,
        TargetexportjobsexportjobidResponse400,
        TargetexportjobsexportjobidResponse404,
    ]
]:
    """/targetExportJobs/{exportJobId}

     Use this endpoint to retrieve information about the status of a specific Target Export Job available
    in the current context.

    Args:
        export_job_id (int):  Default: 1234.

    Returns:
        Response[Union[TargetexportjobsexportjobidResponse200, TargetexportjobsexportjobidResponse400, TargetexportjobsexportjobidResponse404]]
    """

    return sync_detailed(
        export_job_id=export_job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    export_job_id: int = 1234,
    *,
    client: Client,
) -> Response[
    Union[
        TargetexportjobsexportjobidResponse200,
        TargetexportjobsexportjobidResponse400,
        TargetexportjobsexportjobidResponse404,
    ]
]:
    """/targetExportJobs/{exportJobId}

     Use this endpoint to retrieve information about the status of a specific Target Export Job available
    in the current context.

    Args:
        export_job_id (int):  Default: 1234.

    Returns:
        Response[Union[TargetexportjobsexportjobidResponse200, TargetexportjobsexportjobidResponse400, TargetexportjobsexportjobidResponse404]]
    """

    kwargs = _get_kwargs(
        export_job_id=export_job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    export_job_id: int = 1234,
    *,
    client: Client,
) -> Optional[
    Union[
        TargetexportjobsexportjobidResponse200,
        TargetexportjobsexportjobidResponse400,
        TargetexportjobsexportjobidResponse404,
    ]
]:
    """/targetExportJobs/{exportJobId}

     Use this endpoint to retrieve information about the status of a specific Target Export Job available
    in the current context.

    Args:
        export_job_id (int):  Default: 1234.

    Returns:
        Response[Union[TargetexportjobsexportjobidResponse200, TargetexportjobsexportjobidResponse400, TargetexportjobsexportjobidResponse404]]
    """

    return (
        await asyncio_detailed(
            export_job_id=export_job_id,
            client=client,
        )
    ).parsed
