from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.jobclassesjobclassid_response_200 import JobclassesjobclassidResponse200
from ...models.jobclassesjobclassid_response_400 import JobclassesjobclassidResponse400
from ...models.jobclassesjobclassid_response_404 import JobclassesjobclassidResponse404
from ...types import Response


def _get_kwargs(
    job_class_id: int = 123,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/jobClasses/{jobClassId}".format(client.base_url, jobClassId=job_class_id)

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
) -> Optional[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]:
    if response.status_code == 200:
        response_200 = JobclassesjobclassidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = JobclassesjobclassidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = JobclassesjobclassidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    job_class_id: int = 123,
    *,
    client: Client,
) -> Response[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]:
    """/jobClasses/{jobClassId}

     Use this endpoint to retrieve the details of a specific Job Class.

    *Response*

    Returns a standard [Job Class](ref:job-classes#common-models-22) object, if found.

    If the specified Job Class does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        job_class_id (int):  Default: 123.

    Returns:
        Response[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]
    """

    kwargs = _get_kwargs(
        job_class_id=job_class_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    job_class_id: int = 123,
    *,
    client: Client,
) -> Optional[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]:
    """/jobClasses/{jobClassId}

     Use this endpoint to retrieve the details of a specific Job Class.

    *Response*

    Returns a standard [Job Class](ref:job-classes#common-models-22) object, if found.

    If the specified Job Class does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        job_class_id (int):  Default: 123.

    Returns:
        Response[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]
    """

    return sync_detailed(
        job_class_id=job_class_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_class_id: int = 123,
    *,
    client: Client,
) -> Response[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]:
    """/jobClasses/{jobClassId}

     Use this endpoint to retrieve the details of a specific Job Class.

    *Response*

    Returns a standard [Job Class](ref:job-classes#common-models-22) object, if found.

    If the specified Job Class does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        job_class_id (int):  Default: 123.

    Returns:
        Response[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]
    """

    kwargs = _get_kwargs(
        job_class_id=job_class_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    job_class_id: int = 123,
    *,
    client: Client,
) -> Optional[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]:
    """/jobClasses/{jobClassId}

     Use this endpoint to retrieve the details of a specific Job Class.

    *Response*

    Returns a standard [Job Class](ref:job-classes#common-models-22) object, if found.

    If the specified Job Class does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        job_class_id (int):  Default: 123.

    Returns:
        Response[Union[JobclassesjobclassidResponse200, JobclassesjobclassidResponse400, JobclassesjobclassidResponse404]]
    """

    return (
        await asyncio_detailed(
            job_class_id=job_class_id,
            client=client,
        )
    ).parsed
