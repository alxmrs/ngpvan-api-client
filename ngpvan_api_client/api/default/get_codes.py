from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_codes_response_200 import GetCodesResponse200
from ...models.get_codes_response_400 import GetCodesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    supported_entities: Union[Unset, None, str] = "Organizations,Events,Locations",
    name: Union[Unset, None, str] = "Labor",
    parent_code_id: Union[Unset, None, int] = 20513,
    code_type: Union[Unset, None, str] = "Tag",
    expand: Union[Unset, None, str] = "supportedEntities",
    orderby: Union[Unset, None, str] = "dateModified desc",
) -> Dict[str, Any]:
    url = "{}/codes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["supportedEntities"] = supported_entities

    params["name"] = name

    params["parentCodeId"] = parent_code_id

    params["codeType"] = code_type

    params["$expand"] = expand

    params["$orderby"] = orderby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GetCodesResponse200, GetCodesResponse400]]:
    if response.status_code == 200:
        response_200 = GetCodesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetCodesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GetCodesResponse200, GetCodesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    supported_entities: Union[Unset, None, str] = "Organizations,Events,Locations",
    name: Union[Unset, None, str] = "Labor",
    parent_code_id: Union[Unset, None, int] = 20513,
    code_type: Union[Unset, None, str] = "Tag",
    expand: Union[Unset, None, str] = "supportedEntities",
    orderby: Union[Unset, None, str] = "dateModified desc",
) -> Response[Union[GetCodesResponse200, GetCodesResponse400]]:
    """/codes

     Use this endpoint to find Codes available in the current context using a number of filter options.

    By default, this endpoint returns 50 records per request. A maximum of 200 records per request is
    allowed via the `$top` parameter.

    The only valid expansion property is: `supportedEntities`.

    The only valid `orderby` property is: `dateModified`.

    Args:
        supported_entities (Union[Unset, None, str]):  Default: 'Organizations,Events,Locations'.
        name (Union[Unset, None, str]):  Default: 'Labor'.
        parent_code_id (Union[Unset, None, int]):  Default: 20513.
        code_type (Union[Unset, None, str]):  Default: 'Tag'.
        expand (Union[Unset, None, str]):  Default: 'supportedEntities'.
        orderby (Union[Unset, None, str]):  Default: 'dateModified desc'.

    Returns:
        Response[Union[GetCodesResponse200, GetCodesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        supported_entities=supported_entities,
        name=name,
        parent_code_id=parent_code_id,
        code_type=code_type,
        expand=expand,
        orderby=orderby,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    supported_entities: Union[Unset, None, str] = "Organizations,Events,Locations",
    name: Union[Unset, None, str] = "Labor",
    parent_code_id: Union[Unset, None, int] = 20513,
    code_type: Union[Unset, None, str] = "Tag",
    expand: Union[Unset, None, str] = "supportedEntities",
    orderby: Union[Unset, None, str] = "dateModified desc",
) -> Optional[Union[GetCodesResponse200, GetCodesResponse400]]:
    """/codes

     Use this endpoint to find Codes available in the current context using a number of filter options.

    By default, this endpoint returns 50 records per request. A maximum of 200 records per request is
    allowed via the `$top` parameter.

    The only valid expansion property is: `supportedEntities`.

    The only valid `orderby` property is: `dateModified`.

    Args:
        supported_entities (Union[Unset, None, str]):  Default: 'Organizations,Events,Locations'.
        name (Union[Unset, None, str]):  Default: 'Labor'.
        parent_code_id (Union[Unset, None, int]):  Default: 20513.
        code_type (Union[Unset, None, str]):  Default: 'Tag'.
        expand (Union[Unset, None, str]):  Default: 'supportedEntities'.
        orderby (Union[Unset, None, str]):  Default: 'dateModified desc'.

    Returns:
        Response[Union[GetCodesResponse200, GetCodesResponse400]]
    """

    return sync_detailed(
        client=client,
        supported_entities=supported_entities,
        name=name,
        parent_code_id=parent_code_id,
        code_type=code_type,
        expand=expand,
        orderby=orderby,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    supported_entities: Union[Unset, None, str] = "Organizations,Events,Locations",
    name: Union[Unset, None, str] = "Labor",
    parent_code_id: Union[Unset, None, int] = 20513,
    code_type: Union[Unset, None, str] = "Tag",
    expand: Union[Unset, None, str] = "supportedEntities",
    orderby: Union[Unset, None, str] = "dateModified desc",
) -> Response[Union[GetCodesResponse200, GetCodesResponse400]]:
    """/codes

     Use this endpoint to find Codes available in the current context using a number of filter options.

    By default, this endpoint returns 50 records per request. A maximum of 200 records per request is
    allowed via the `$top` parameter.

    The only valid expansion property is: `supportedEntities`.

    The only valid `orderby` property is: `dateModified`.

    Args:
        supported_entities (Union[Unset, None, str]):  Default: 'Organizations,Events,Locations'.
        name (Union[Unset, None, str]):  Default: 'Labor'.
        parent_code_id (Union[Unset, None, int]):  Default: 20513.
        code_type (Union[Unset, None, str]):  Default: 'Tag'.
        expand (Union[Unset, None, str]):  Default: 'supportedEntities'.
        orderby (Union[Unset, None, str]):  Default: 'dateModified desc'.

    Returns:
        Response[Union[GetCodesResponse200, GetCodesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        supported_entities=supported_entities,
        name=name,
        parent_code_id=parent_code_id,
        code_type=code_type,
        expand=expand,
        orderby=orderby,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    supported_entities: Union[Unset, None, str] = "Organizations,Events,Locations",
    name: Union[Unset, None, str] = "Labor",
    parent_code_id: Union[Unset, None, int] = 20513,
    code_type: Union[Unset, None, str] = "Tag",
    expand: Union[Unset, None, str] = "supportedEntities",
    orderby: Union[Unset, None, str] = "dateModified desc",
) -> Optional[Union[GetCodesResponse200, GetCodesResponse400]]:
    """/codes

     Use this endpoint to find Codes available in the current context using a number of filter options.

    By default, this endpoint returns 50 records per request. A maximum of 200 records per request is
    allowed via the `$top` parameter.

    The only valid expansion property is: `supportedEntities`.

    The only valid `orderby` property is: `dateModified`.

    Args:
        supported_entities (Union[Unset, None, str]):  Default: 'Organizations,Events,Locations'.
        name (Union[Unset, None, str]):  Default: 'Labor'.
        parent_code_id (Union[Unset, None, int]):  Default: 20513.
        code_type (Union[Unset, None, str]):  Default: 'Tag'.
        expand (Union[Unset, None, str]):  Default: 'supportedEntities'.
        orderby (Union[Unset, None, str]):  Default: 'dateModified desc'.

    Returns:
        Response[Union[GetCodesResponse200, GetCodesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            supported_entities=supported_entities,
            name=name,
            parent_code_id=parent_code_id,
            code_type=code_type,
            expand=expand,
            orderby=orderby,
        )
    ).parsed
