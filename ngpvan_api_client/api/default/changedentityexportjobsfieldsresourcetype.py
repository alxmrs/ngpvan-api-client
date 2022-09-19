from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.changedentityexportjobsfieldsresourcetype_response_200_item import (
    ChangedentityexportjobsfieldsresourcetypeResponse200Item,
)
from ...models.changedentityexportjobsfieldsresourcetype_response_400 import (
    ChangedentityexportjobsfieldsresourcetypeResponse400,
)
from ...types import Response


def _get_kwargs(
    resource_type: str = "Contacts",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/changedEntityExportJobs/fields/{resourceType}".format(client.base_url, resourceType=resource_type)

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
        ChangedentityexportjobsfieldsresourcetypeResponse400,
        List[ChangedentityexportjobsfieldsresourcetypeResponse200Item],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChangedentityexportjobsfieldsresourcetypeResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ChangedentityexportjobsfieldsresourcetypeResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        ChangedentityexportjobsfieldsresourcetypeResponse400,
        List[ChangedentityexportjobsfieldsresourcetypeResponse200Item],
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    resource_type: str = "Contacts",
    *,
    client: Client,
) -> Response[
    Union[
        ChangedentityexportjobsfieldsresourcetypeResponse400,
        List[ChangedentityexportjobsfieldsresourcetypeResponse200Item],
    ]
]:
    """/changedEntityExportJobs/fields/{resourceType}

     Retrieve a collection of available fields for a specified `resourceType` with metadata about each
    field.

    Args:
        resource_type (str):  Default: 'Contacts'.

    Returns:
        Response[Union[ChangedentityexportjobsfieldsresourcetypeResponse400, List[ChangedentityexportjobsfieldsresourcetypeResponse200Item]]]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    resource_type: str = "Contacts",
    *,
    client: Client,
) -> Optional[
    Union[
        ChangedentityexportjobsfieldsresourcetypeResponse400,
        List[ChangedentityexportjobsfieldsresourcetypeResponse200Item],
    ]
]:
    """/changedEntityExportJobs/fields/{resourceType}

     Retrieve a collection of available fields for a specified `resourceType` with metadata about each
    field.

    Args:
        resource_type (str):  Default: 'Contacts'.

    Returns:
        Response[Union[ChangedentityexportjobsfieldsresourcetypeResponse400, List[ChangedentityexportjobsfieldsresourcetypeResponse200Item]]]
    """

    return sync_detailed(
        resource_type=resource_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_type: str = "Contacts",
    *,
    client: Client,
) -> Response[
    Union[
        ChangedentityexportjobsfieldsresourcetypeResponse400,
        List[ChangedentityexportjobsfieldsresourcetypeResponse200Item],
    ]
]:
    """/changedEntityExportJobs/fields/{resourceType}

     Retrieve a collection of available fields for a specified `resourceType` with metadata about each
    field.

    Args:
        resource_type (str):  Default: 'Contacts'.

    Returns:
        Response[Union[ChangedentityexportjobsfieldsresourcetypeResponse400, List[ChangedentityexportjobsfieldsresourcetypeResponse200Item]]]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    resource_type: str = "Contacts",
    *,
    client: Client,
) -> Optional[
    Union[
        ChangedentityexportjobsfieldsresourcetypeResponse400,
        List[ChangedentityexportjobsfieldsresourcetypeResponse200Item],
    ]
]:
    """/changedEntityExportJobs/fields/{resourceType}

     Retrieve a collection of available fields for a specified `resourceType` with metadata about each
    field.

    Args:
        resource_type (str):  Default: 'Contacts'.

    Returns:
        Response[Union[ChangedentityexportjobsfieldsresourcetypeResponse400, List[ChangedentityexportjobsfieldsresourcetypeResponse200Item]]]
    """

    return (
        await asyncio_detailed(
            resource_type=resource_type,
            client=client,
        )
    ).parsed
