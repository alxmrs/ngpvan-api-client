from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.changedentityexportjobschangetypesresourcetype_response_200_item import (
    ChangedentityexportjobschangetypesresourcetypeResponse200Item,
)
from ...models.changedentityexportjobschangetypesresourcetype_response_400 import (
    ChangedentityexportjobschangetypesresourcetypeResponse400,
)
from ...types import Response


def _get_kwargs(
    resource_type: str = "Contacts",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/changedEntityExportJobs/changeTypes/{resourceType}".format(client.base_url, resourceType=resource_type)

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
        ChangedentityexportjobschangetypesresourcetypeResponse400,
        List[ChangedentityexportjobschangetypesresourcetypeResponse200Item],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChangedentityexportjobschangetypesresourcetypeResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ChangedentityexportjobschangetypesresourcetypeResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        ChangedentityexportjobschangetypesresourcetypeResponse400,
        List[ChangedentityexportjobschangetypesresourcetypeResponse200Item],
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
        ChangedentityexportjobschangetypesresourcetypeResponse400,
        List[ChangedentityexportjobschangetypesresourcetypeResponse200Item],
    ]
]:
    """/changedEntityExportJobs/changeTypes/{resourceType}

     Retrieve all available `changeTypes` for a specified `resourceType`

    Some `resourceTypes` will return a `ChangeTypeID` and associated data in their export files to
    indicate the type of the last change made to an exported record. This endpoint retrieves a
    collection of available `changeTypes` for a specified `resourceType` with metadata about each
    `changeType`.

    Args:
        resource_type (str):  Default: 'Contacts'.

    Returns:
        Response[Union[ChangedentityexportjobschangetypesresourcetypeResponse400, List[ChangedentityexportjobschangetypesresourcetypeResponse200Item]]]
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
        ChangedentityexportjobschangetypesresourcetypeResponse400,
        List[ChangedentityexportjobschangetypesresourcetypeResponse200Item],
    ]
]:
    """/changedEntityExportJobs/changeTypes/{resourceType}

     Retrieve all available `changeTypes` for a specified `resourceType`

    Some `resourceTypes` will return a `ChangeTypeID` and associated data in their export files to
    indicate the type of the last change made to an exported record. This endpoint retrieves a
    collection of available `changeTypes` for a specified `resourceType` with metadata about each
    `changeType`.

    Args:
        resource_type (str):  Default: 'Contacts'.

    Returns:
        Response[Union[ChangedentityexportjobschangetypesresourcetypeResponse400, List[ChangedentityexportjobschangetypesresourcetypeResponse200Item]]]
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
        ChangedentityexportjobschangetypesresourcetypeResponse400,
        List[ChangedentityexportjobschangetypesresourcetypeResponse200Item],
    ]
]:
    """/changedEntityExportJobs/changeTypes/{resourceType}

     Retrieve all available `changeTypes` for a specified `resourceType`

    Some `resourceTypes` will return a `ChangeTypeID` and associated data in their export files to
    indicate the type of the last change made to an exported record. This endpoint retrieves a
    collection of available `changeTypes` for a specified `resourceType` with metadata about each
    `changeType`.

    Args:
        resource_type (str):  Default: 'Contacts'.

    Returns:
        Response[Union[ChangedentityexportjobschangetypesresourcetypeResponse400, List[ChangedentityexportjobschangetypesresourcetypeResponse200Item]]]
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
        ChangedentityexportjobschangetypesresourcetypeResponse400,
        List[ChangedentityexportjobschangetypesresourcetypeResponse200Item],
    ]
]:
    """/changedEntityExportJobs/changeTypes/{resourceType}

     Retrieve all available `changeTypes` for a specified `resourceType`

    Some `resourceTypes` will return a `ChangeTypeID` and associated data in their export files to
    indicate the type of the last change made to an exported record. This endpoint retrieves a
    collection of available `changeTypes` for a specified `resourceType` with metadata about each
    `changeType`.

    Args:
        resource_type (str):  Default: 'Contacts'.

    Returns:
        Response[Union[ChangedentityexportjobschangetypesresourcetypeResponse400, List[ChangedentityexportjobschangetypesresourcetypeResponse200Item]]]
    """

    return (
        await asyncio_detailed(
            resource_type=resource_type,
            client=client,
        )
    ).parsed
