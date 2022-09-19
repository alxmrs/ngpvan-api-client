from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bulkimportjobs_response_200 import BulkimportjobsResponse200
from ...models.bulkimportjobs_response_400 import BulkimportjobsResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bulkImportJobs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]:
    if response.status_code == 200:
        response_200 = BulkimportjobsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BulkimportjobsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]:
    """/bulkImportJobs

     Initiates a bulk import job by specifying the url for a zipped, delimited file, of no more than
    100MB. A bulk import job can update and/or create multiple data types including, but not limited to,
    `Contacts`, `Contributions`, and `ActivistCodes`. For a complete list of supported types, see the
    [resources](ref:bulk-import#bulkimportjobsresources) endpoint.

    The zipped file can contain both update and creation records for a single resource type. It can also
    contain a header row. The header row is only there as a debugging aid, and is not used by the import
    process. See Property `hasHeader` in the [File](ref:file-loading-jobs) object for more information
    on headers.

    When the bulk import job is updating resources, if any non-required columns are left blank, those
    fields will not be updated. This process cannot be used to delete information; it can only update or
    create.

    Returns:
        Response[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]:
    """/bulkImportJobs

     Initiates a bulk import job by specifying the url for a zipped, delimited file, of no more than
    100MB. A bulk import job can update and/or create multiple data types including, but not limited to,
    `Contacts`, `Contributions`, and `ActivistCodes`. For a complete list of supported types, see the
    [resources](ref:bulk-import#bulkimportjobsresources) endpoint.

    The zipped file can contain both update and creation records for a single resource type. It can also
    contain a header row. The header row is only there as a debugging aid, and is not used by the import
    process. See Property `hasHeader` in the [File](ref:file-loading-jobs) object for more information
    on headers.

    When the bulk import job is updating resources, if any non-required columns are left blank, those
    fields will not be updated. This process cannot be used to delete information; it can only update or
    create.

    Returns:
        Response[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]:
    """/bulkImportJobs

     Initiates a bulk import job by specifying the url for a zipped, delimited file, of no more than
    100MB. A bulk import job can update and/or create multiple data types including, but not limited to,
    `Contacts`, `Contributions`, and `ActivistCodes`. For a complete list of supported types, see the
    [resources](ref:bulk-import#bulkimportjobsresources) endpoint.

    The zipped file can contain both update and creation records for a single resource type. It can also
    contain a header row. The header row is only there as a debugging aid, and is not used by the import
    process. See Property `hasHeader` in the [File](ref:file-loading-jobs) object for more information
    on headers.

    When the bulk import job is updating resources, if any non-required columns are left blank, those
    fields will not be updated. This process cannot be used to delete information; it can only update or
    create.

    Returns:
        Response[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]:
    """/bulkImportJobs

     Initiates a bulk import job by specifying the url for a zipped, delimited file, of no more than
    100MB. A bulk import job can update and/or create multiple data types including, but not limited to,
    `Contacts`, `Contributions`, and `ActivistCodes`. For a complete list of supported types, see the
    [resources](ref:bulk-import#bulkimportjobsresources) endpoint.

    The zipped file can contain both update and creation records for a single resource type. It can also
    contain a header row. The header row is only there as a debugging aid, and is not used by the import
    process. See Property `hasHeader` in the [File](ref:file-loading-jobs) object for more information
    on headers.

    When the bulk import job is updating resources, if any non-required columns are left blank, those
    fields will not be updated. This process cannot be used to delete information; it can only update or
    create.

    Returns:
        Response[Union[BulkimportjobsResponse200, BulkimportjobsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
