from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.put_codes_json_body import PutCodesJsonBody
from ...models.put_codes_response_200_item import PutCodesResponse200Item
from ...models.put_codes_response_400 import PutCodesResponse400
from ...models.put_codes_response_404 import PutCodesResponse404
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PutCodesJsonBody,
) -> Dict[str, Any]:
    url = "{}/codes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PutCodesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = PutCodesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = PutCodesResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PutCodesJsonBody,
) -> Response[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]:
    """/codes

     Use this endpoint to update the editable properties of a set of existing Codes. For example, you
    could use this to change the names of Codes, to change several Codes’ parents, or to add or remove
    the Entities the Codes support.

    When constructing your request, note that all editable properties must be specified otherwise it is
    assumed they should be removed or set to null. For example, if the `supportedEntities` property is
    set to `null` or `[]` (an empty array) in JSON specifying a Code, all supported Entities are removed
    from that Code.

    Args:
        json_body (PutCodesJsonBody):

    Returns:
        Response[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]
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
    json_body: PutCodesJsonBody,
) -> Optional[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]:
    """/codes

     Use this endpoint to update the editable properties of a set of existing Codes. For example, you
    could use this to change the names of Codes, to change several Codes’ parents, or to add or remove
    the Entities the Codes support.

    When constructing your request, note that all editable properties must be specified otherwise it is
    assumed they should be removed or set to null. For example, if the `supportedEntities` property is
    set to `null` or `[]` (an empty array) in JSON specifying a Code, all supported Entities are removed
    from that Code.

    Args:
        json_body (PutCodesJsonBody):

    Returns:
        Response[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PutCodesJsonBody,
) -> Response[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]:
    """/codes

     Use this endpoint to update the editable properties of a set of existing Codes. For example, you
    could use this to change the names of Codes, to change several Codes’ parents, or to add or remove
    the Entities the Codes support.

    When constructing your request, note that all editable properties must be specified otherwise it is
    assumed they should be removed or set to null. For example, if the `supportedEntities` property is
    set to `null` or `[]` (an empty array) in JSON specifying a Code, all supported Entities are removed
    from that Code.

    Args:
        json_body (PutCodesJsonBody):

    Returns:
        Response[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]
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
    json_body: PutCodesJsonBody,
) -> Optional[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]:
    """/codes

     Use this endpoint to update the editable properties of a set of existing Codes. For example, you
    could use this to change the names of Codes, to change several Codes’ parents, or to add or remove
    the Entities the Codes support.

    When constructing your request, note that all editable properties must be specified otherwise it is
    assumed they should be removed or set to null. For example, if the `supportedEntities` property is
    set to `null` or `[]` (an empty array) in JSON specifying a Code, all supported Entities are removed
    from that Code.

    Args:
        json_body (PutCodesJsonBody):

    Returns:
        Response[Union[List[PutCodesResponse200Item], PutCodesResponse400, PutCodesResponse404]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
