from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.exportjobs_json_body import ExportjobsJsonBody
from ...models.exportjobs_response_400 import ExportjobsResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: ExportjobsJsonBody,
) -> Dict[str, Any]:
    url = "{}/exportJobs".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ExportjobsResponse400]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 400:
        response_400 = ExportjobsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ExportjobsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ExportjobsJsonBody,
) -> Response[Union[Any, ExportjobsResponse400]]:
    """/exportJobs

     Create a new Export Job

    An Export Job object, indicating the ID of the Export Job as well as the status of the job.

    When the job completes, the JSON-formatted Export Job object will be POSTed to the `webhookUrl`
    indicated below.

    Args:
        json_body (ExportjobsJsonBody):

    Returns:
        Response[Union[Any, ExportjobsResponse400]]
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
    json_body: ExportjobsJsonBody,
) -> Optional[Union[Any, ExportjobsResponse400]]:
    """/exportJobs

     Create a new Export Job

    An Export Job object, indicating the ID of the Export Job as well as the status of the job.

    When the job completes, the JSON-formatted Export Job object will be POSTed to the `webhookUrl`
    indicated below.

    Args:
        json_body (ExportjobsJsonBody):

    Returns:
        Response[Union[Any, ExportjobsResponse400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ExportjobsJsonBody,
) -> Response[Union[Any, ExportjobsResponse400]]:
    """/exportJobs

     Create a new Export Job

    An Export Job object, indicating the ID of the Export Job as well as the status of the job.

    When the job completes, the JSON-formatted Export Job object will be POSTed to the `webhookUrl`
    indicated below.

    Args:
        json_body (ExportjobsJsonBody):

    Returns:
        Response[Union[Any, ExportjobsResponse400]]
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
    json_body: ExportjobsJsonBody,
) -> Optional[Union[Any, ExportjobsResponse400]]:
    """/exportJobs

     Create a new Export Job

    An Export Job object, indicating the ID of the Export Job as well as the status of the job.

    When the job completes, the JSON-formatted Export Job object will be POSTed to the `webhookUrl`
    indicated below.

    Args:
        json_body (ExportjobsJsonBody):

    Returns:
        Response[Union[Any, ExportjobsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
