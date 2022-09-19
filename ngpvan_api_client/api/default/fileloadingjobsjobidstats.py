from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.fileloadingjobsjobidstats_response_200 import FileloadingjobsjobidstatsResponse200
from ...models.fileloadingjobsjobidstats_response_400 import FileloadingjobsjobidstatsResponse400
from ...types import Response


def _get_kwargs(
    job_id: int = 123,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/fileLoadingJobs/{jobId}/stats".format(client.base_url, jobId=job_id)

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
) -> Optional[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]:
    if response.status_code == 200:
        response_200 = FileloadingjobsjobidstatsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = FileloadingjobsjobidstatsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    job_id: int = 123,
    *,
    client: Client,
) -> Response[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]:
    """/fileLoadingJobs/{jobId}/stats

     This endpoint returns status and metadata information about an existing Phone Loading job specified
    by the unique identifier `jobId`.  Note that this endpoint is only valid for the  `PhonesFile`
    action type.

    Args:
        job_id (int):  Default: 123.

    Returns:
        Response[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    job_id: int = 123,
    *,
    client: Client,
) -> Optional[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]:
    """/fileLoadingJobs/{jobId}/stats

     This endpoint returns status and metadata information about an existing Phone Loading job specified
    by the unique identifier `jobId`.  Note that this endpoint is only valid for the  `PhonesFile`
    action type.

    Args:
        job_id (int):  Default: 123.

    Returns:
        Response[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: int = 123,
    *,
    client: Client,
) -> Response[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]:
    """/fileLoadingJobs/{jobId}/stats

     This endpoint returns status and metadata information about an existing Phone Loading job specified
    by the unique identifier `jobId`.  Note that this endpoint is only valid for the  `PhonesFile`
    action type.

    Args:
        job_id (int):  Default: 123.

    Returns:
        Response[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    job_id: int = 123,
    *,
    client: Client,
) -> Optional[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]:
    """/fileLoadingJobs/{jobId}/stats

     This endpoint returns status and metadata information about an existing Phone Loading job specified
    by the unique identifier `jobId`.  Note that this endpoint is only valid for the  `PhonesFile`
    action type.

    Args:
        job_id (int):  Default: 123.

    Returns:
        Response[Union[FileloadingjobsjobidstatsResponse200, FileloadingjobsjobidstatsResponse400]]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
