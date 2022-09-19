from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.put_codes_codeid_json_body import PutCodesCodeidJsonBody
from ...models.put_codes_codeid_response_400 import PutCodesCodeidResponse400
from ...types import Response


def _get_kwargs(
    code_id: int,
    *,
    client: Client,
    json_body: PutCodesCodeidJsonBody,
) -> Dict[str, Any]:
    url = "{}/codes/{codeId}".format(client.base_url, codeId=code_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PutCodesCodeidResponse400]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PutCodesCodeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PutCodesCodeidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    code_id: int,
    *,
    client: Client,
    json_body: PutCodesCodeidJsonBody,
) -> Response[Union[Any, PutCodesCodeidResponse400]]:
    """/codes/{codeId}

     Use this endpoint to update the editable properties of an existing Code. For example, you could use
    this to change the name of a Code, to change a Code’s parent, or to add or remove the Entities this
    Code supports.

    When constructing your request, note that all editable properties must be specified otherwise it is
    assumed they should be removed or set to null. For example, if the `supportedEntities` property is
    set to `null` or `[]` (an empty array) in the request, all supported Entities are removed from the
    Code.

    Not all properties can be updated using this endpoint. If you need to update all metadata or are
    unable to populate all existing properties as described above, consider using the [PATCH](ref:patch-
    codes-codeid) endpoint.

    Args:
        code_id (int):
        json_body (PutCodesCodeidJsonBody):

    Returns:
        Response[Union[Any, PutCodesCodeidResponse400]]
    """

    kwargs = _get_kwargs(
        code_id=code_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    code_id: int,
    *,
    client: Client,
    json_body: PutCodesCodeidJsonBody,
) -> Optional[Union[Any, PutCodesCodeidResponse400]]:
    """/codes/{codeId}

     Use this endpoint to update the editable properties of an existing Code. For example, you could use
    this to change the name of a Code, to change a Code’s parent, or to add or remove the Entities this
    Code supports.

    When constructing your request, note that all editable properties must be specified otherwise it is
    assumed they should be removed or set to null. For example, if the `supportedEntities` property is
    set to `null` or `[]` (an empty array) in the request, all supported Entities are removed from the
    Code.

    Not all properties can be updated using this endpoint. If you need to update all metadata or are
    unable to populate all existing properties as described above, consider using the [PATCH](ref:patch-
    codes-codeid) endpoint.

    Args:
        code_id (int):
        json_body (PutCodesCodeidJsonBody):

    Returns:
        Response[Union[Any, PutCodesCodeidResponse400]]
    """

    return sync_detailed(
        code_id=code_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    code_id: int,
    *,
    client: Client,
    json_body: PutCodesCodeidJsonBody,
) -> Response[Union[Any, PutCodesCodeidResponse400]]:
    """/codes/{codeId}

     Use this endpoint to update the editable properties of an existing Code. For example, you could use
    this to change the name of a Code, to change a Code’s parent, or to add or remove the Entities this
    Code supports.

    When constructing your request, note that all editable properties must be specified otherwise it is
    assumed they should be removed or set to null. For example, if the `supportedEntities` property is
    set to `null` or `[]` (an empty array) in the request, all supported Entities are removed from the
    Code.

    Not all properties can be updated using this endpoint. If you need to update all metadata or are
    unable to populate all existing properties as described above, consider using the [PATCH](ref:patch-
    codes-codeid) endpoint.

    Args:
        code_id (int):
        json_body (PutCodesCodeidJsonBody):

    Returns:
        Response[Union[Any, PutCodesCodeidResponse400]]
    """

    kwargs = _get_kwargs(
        code_id=code_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    code_id: int,
    *,
    client: Client,
    json_body: PutCodesCodeidJsonBody,
) -> Optional[Union[Any, PutCodesCodeidResponse400]]:
    """/codes/{codeId}

     Use this endpoint to update the editable properties of an existing Code. For example, you could use
    this to change the name of a Code, to change a Code’s parent, or to add or remove the Entities this
    Code supports.

    When constructing your request, note that all editable properties must be specified otherwise it is
    assumed they should be removed or set to null. For example, if the `supportedEntities` property is
    set to `null` or `[]` (an empty array) in the request, all supported Entities are removed from the
    Code.

    Not all properties can be updated using this endpoint. If you need to update all metadata or are
    unable to populate all existing properties as described above, consider using the [PATCH](ref:patch-
    codes-codeid) endpoint.

    Args:
        code_id (int):
        json_body (PutCodesCodeidJsonBody):

    Returns:
        Response[Union[Any, PutCodesCodeidResponse400]]
    """

    return (
        await asyncio_detailed(
            code_id=code_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
