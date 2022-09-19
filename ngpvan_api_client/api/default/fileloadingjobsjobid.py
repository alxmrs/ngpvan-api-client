from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.fileloadingjobsjobid_response_400 import FileloadingjobsjobidResponse400
from ...models.fileloadingjobsjobid_response_404 import FileloadingjobsjobidResponse404
from ...types import Response


def _get_kwargs(
    job_id: int = 998877,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/fileLoadingJobs/{jobId}".format(client.base_url, jobId=job_id)

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
) -> Optional[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = FileloadingjobsjobidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = FileloadingjobsjobidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    job_id: int = 998877,
    *,
    client: Client,
) -> Response[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]:
    """/fileLoadingJobs/{jobId}

     This endpoint returns status and metadata about an existing File Loading Job, which is specified by
    the unique identifier `jobId`. The `jobId` is provided as the response to a `POST` request to create
    a File Loading Job.

    Args:
        job_id (int):  Default: 998877.

    Returns:
        Response[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]
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
    job_id: int = 998877,
    *,
    client: Client,
) -> Optional[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]:
    """/fileLoadingJobs/{jobId}

     This endpoint returns status and metadata about an existing File Loading Job, which is specified by
    the unique identifier `jobId`. The `jobId` is provided as the response to a `POST` request to create
    a File Loading Job.

    Args:
        job_id (int):  Default: 998877.

    Returns:
        Response[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: int = 998877,
    *,
    client: Client,
) -> Response[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]:
    """/fileLoadingJobs/{jobId}

     This endpoint returns status and metadata about an existing File Loading Job, which is specified by
    the unique identifier `jobId`. The `jobId` is provided as the response to a `POST` request to create
    a File Loading Job.

    Args:
        job_id (int):  Default: 998877.

    Returns:
        Response[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    job_id: int = 998877,
    *,
    client: Client,
) -> Optional[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]:
    """/fileLoadingJobs/{jobId}

     This endpoint returns status and metadata about an existing File Loading Job, which is specified by
    the unique identifier `jobId`. The `jobId` is provided as the response to a `POST` request to create
    a File Loading Job.

    Args:
        job_id (int):  Default: 998877.

    Returns:
        Response[Union[Any, FileloadingjobsjobidResponse400, FileloadingjobsjobidResponse404]]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
