from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.bulkimportmappingtypesmappingtypenamefieldnamevalues_response_200 import (
    BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200,
)
from ...models.bulkimportmappingtypesmappingtypenamefieldnamevalues_response_400 import (
    BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400,
)
from ...types import Response


def _get_kwargs(
    mapping_type_name: str = "MailingAddress",
    field_name: str = "name",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bulkImportMappingTypes/{mappingTypeName}/{fieldName}/values".format(
        client.base_url, mappingTypeName=mapping_type_name, fieldName=field_name
    )

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
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200,
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400,
    ]
]:
    if response.status_code == 200:
        response_200 = BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200,
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    mapping_type_name: str = "MailingAddress",
    field_name: str = "name",
    *,
    client: Client,
) -> Response[
    Union[
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200,
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400,
    ]
]:
    """/bulkImportMappingTypes/{mappingTypeName}/{fieldName}/values

     Retrieve a collection of the complete list of values that can be applied to a given column in a
    field during a bulk import

    Some fields have a predefined list of possible values which can be applied during a bulk import,
    corresponding, for example, to a drop-down list or a checkbox. This endpoint returns an ID and name
    property for each value that is allowed as an input. When preparing input data, input values should
    take the form of the ID of the value rather than the name to avoid potential collisions. However, if
    available value names are unique, names will be accepted as input values.

    Args:
        mapping_type_name (str):  Default: 'MailingAddress'.
        field_name (str):  Default: 'name'.

    Returns:
        Response[Union[BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200, BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400]]
    """

    kwargs = _get_kwargs(
        mapping_type_name=mapping_type_name,
        field_name=field_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    mapping_type_name: str = "MailingAddress",
    field_name: str = "name",
    *,
    client: Client,
) -> Optional[
    Union[
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200,
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400,
    ]
]:
    """/bulkImportMappingTypes/{mappingTypeName}/{fieldName}/values

     Retrieve a collection of the complete list of values that can be applied to a given column in a
    field during a bulk import

    Some fields have a predefined list of possible values which can be applied during a bulk import,
    corresponding, for example, to a drop-down list or a checkbox. This endpoint returns an ID and name
    property for each value that is allowed as an input. When preparing input data, input values should
    take the form of the ID of the value rather than the name to avoid potential collisions. However, if
    available value names are unique, names will be accepted as input values.

    Args:
        mapping_type_name (str):  Default: 'MailingAddress'.
        field_name (str):  Default: 'name'.

    Returns:
        Response[Union[BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200, BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400]]
    """

    return sync_detailed(
        mapping_type_name=mapping_type_name,
        field_name=field_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    mapping_type_name: str = "MailingAddress",
    field_name: str = "name",
    *,
    client: Client,
) -> Response[
    Union[
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200,
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400,
    ]
]:
    """/bulkImportMappingTypes/{mappingTypeName}/{fieldName}/values

     Retrieve a collection of the complete list of values that can be applied to a given column in a
    field during a bulk import

    Some fields have a predefined list of possible values which can be applied during a bulk import,
    corresponding, for example, to a drop-down list or a checkbox. This endpoint returns an ID and name
    property for each value that is allowed as an input. When preparing input data, input values should
    take the form of the ID of the value rather than the name to avoid potential collisions. However, if
    available value names are unique, names will be accepted as input values.

    Args:
        mapping_type_name (str):  Default: 'MailingAddress'.
        field_name (str):  Default: 'name'.

    Returns:
        Response[Union[BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200, BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400]]
    """

    kwargs = _get_kwargs(
        mapping_type_name=mapping_type_name,
        field_name=field_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    mapping_type_name: str = "MailingAddress",
    field_name: str = "name",
    *,
    client: Client,
) -> Optional[
    Union[
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200,
        BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400,
    ]
]:
    """/bulkImportMappingTypes/{mappingTypeName}/{fieldName}/values

     Retrieve a collection of the complete list of values that can be applied to a given column in a
    field during a bulk import

    Some fields have a predefined list of possible values which can be applied during a bulk import,
    corresponding, for example, to a drop-down list or a checkbox. This endpoint returns an ID and name
    property for each value that is allowed as an input. When preparing input data, input values should
    take the form of the ID of the value rather than the name to avoid potential collisions. However, if
    available value names are unique, names will be accepted as input values.

    Args:
        mapping_type_name (str):  Default: 'MailingAddress'.
        field_name (str):  Default: 'name'.

    Returns:
        Response[Union[BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse200, BulkimportmappingtypesmappingtypenamefieldnamevaluesResponse400]]
    """

    return (
        await asyncio_detailed(
            mapping_type_name=mapping_type_name,
            field_name=field_name,
            client=client,
        )
    ).parsed
