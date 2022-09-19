from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bulkimportmappingtypes_response_200 import BulkimportmappingtypesResponse200
from ...models.bulkimportmappingtypes_response_400 import BulkimportmappingtypesResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bulkImportMappingTypes".format(client.base_url)

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
) -> Optional[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]:
    if response.status_code == 200:
        response_200 = BulkimportmappingtypesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BulkimportmappingtypesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]:
    """/bulkImportMappingTypes

     This endpoint returns all the available ways you can map your file columns and values to accepted
    models that can be imported during a bulk import operation.

    This information lets you know what can be imported during your operation, what are the
    characteristics of those fields and their columns, which columns have a predefined list of possible
    data, etc.

    With this information, you can build your request payload to `POST /bulkImportJobs` endpoint to map
    some information directly from your uploaded file, hardcode some information as static, map your
    uploaded data to other values, or make whatever mappings are necessary to create your import.

    Returns:
        Response[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]
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
) -> Optional[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]:
    """/bulkImportMappingTypes

     This endpoint returns all the available ways you can map your file columns and values to accepted
    models that can be imported during a bulk import operation.

    This information lets you know what can be imported during your operation, what are the
    characteristics of those fields and their columns, which columns have a predefined list of possible
    data, etc.

    With this information, you can build your request payload to `POST /bulkImportJobs` endpoint to map
    some information directly from your uploaded file, hardcode some information as static, map your
    uploaded data to other values, or make whatever mappings are necessary to create your import.

    Returns:
        Response[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]:
    """/bulkImportMappingTypes

     This endpoint returns all the available ways you can map your file columns and values to accepted
    models that can be imported during a bulk import operation.

    This information lets you know what can be imported during your operation, what are the
    characteristics of those fields and their columns, which columns have a predefined list of possible
    data, etc.

    With this information, you can build your request payload to `POST /bulkImportJobs` endpoint to map
    some information directly from your uploaded file, hardcode some information as static, map your
    uploaded data to other values, or make whatever mappings are necessary to create your import.

    Returns:
        Response[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]
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
) -> Optional[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]:
    """/bulkImportMappingTypes

     This endpoint returns all the available ways you can map your file columns and values to accepted
    models that can be imported during a bulk import operation.

    This information lets you know what can be imported during your operation, what are the
    characteristics of those fields and their columns, which columns have a predefined list of possible
    data, etc.

    With this information, you can build your request payload to `POST /bulkImportJobs` endpoint to map
    some information directly from your uploaded file, hardcode some information as static, map your
    uploaded data to other values, or make whatever mappings are necessary to create your import.

    Returns:
        Response[Union[BulkimportmappingtypesResponse200, BulkimportmappingtypesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
