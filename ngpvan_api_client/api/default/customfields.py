from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.customfields_response_200_item import CustomfieldsResponse200Item
from ...models.customfields_response_400 import CustomfieldsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    custom_fields_group_type: Union[Unset, None, str] = "Contacts",
) -> Dict[str, Any]:
    url = "{}/customFields".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["customFieldsGroupType"] = custom_fields_group_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CustomfieldsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = CustomfieldsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    custom_fields_group_type: Union[Unset, None, str] = "Contacts",
) -> Response[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]:
    """/customFields

     Use this endpoint to retrieve all Custom Fields that are available in the current context.

    Args:
        custom_fields_group_type (Union[Unset, None, str]):  Default: 'Contacts'.

    Returns:
        Response[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]
    """

    kwargs = _get_kwargs(
        client=client,
        custom_fields_group_type=custom_fields_group_type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    custom_fields_group_type: Union[Unset, None, str] = "Contacts",
) -> Optional[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]:
    """/customFields

     Use this endpoint to retrieve all Custom Fields that are available in the current context.

    Args:
        custom_fields_group_type (Union[Unset, None, str]):  Default: 'Contacts'.

    Returns:
        Response[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]
    """

    return sync_detailed(
        client=client,
        custom_fields_group_type=custom_fields_group_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    custom_fields_group_type: Union[Unset, None, str] = "Contacts",
) -> Response[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]:
    """/customFields

     Use this endpoint to retrieve all Custom Fields that are available in the current context.

    Args:
        custom_fields_group_type (Union[Unset, None, str]):  Default: 'Contacts'.

    Returns:
        Response[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]
    """

    kwargs = _get_kwargs(
        client=client,
        custom_fields_group_type=custom_fields_group_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    custom_fields_group_type: Union[Unset, None, str] = "Contacts",
) -> Optional[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]:
    """/customFields

     Use this endpoint to retrieve all Custom Fields that are available in the current context.

    Args:
        custom_fields_group_type (Union[Unset, None, str]):  Default: 'Contacts'.

    Returns:
        Response[Union[CustomfieldsResponse400, List[CustomfieldsResponse200Item]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            custom_fields_group_type=custom_fields_group_type,
        )
    ).parsed
