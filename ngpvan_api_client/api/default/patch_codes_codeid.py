from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.patch_codes_codeid_json_body import PatchCodesCodeidJsonBody
from ...models.patch_codes_codeid_response_204 import PatchCodesCodeidResponse204
from ...models.patch_codes_codeid_response_400 import PatchCodesCodeidResponse400
from ...types import Response


def _get_kwargs(
    code_id: int,
    *,
    client: Client,
    json_body: PatchCodesCodeidJsonBody,
) -> Dict[str, Any]:
    url = "{}/codes/{codeId}".format(client.base_url, codeId=code_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]:
    if response.status_code == 204:
        response_204 = PatchCodesCodeidResponse204.from_dict(response.json())

        return response_204
    if response.status_code == 400:
        response_400 = PatchCodesCodeidResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]:
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
    json_body: PatchCodesCodeidJsonBody,
) -> Response[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]:
    """/codes/{codeId}

     Update editable properties of a Source Code or Tag. This is a [JSON Patch](ref:json-patch) endpoint.

    Args:
        code_id (int):
        json_body (PatchCodesCodeidJsonBody):

    Returns:
        Response[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]
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
    json_body: PatchCodesCodeidJsonBody,
) -> Optional[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]:
    """/codes/{codeId}

     Update editable properties of a Source Code or Tag. This is a [JSON Patch](ref:json-patch) endpoint.

    Args:
        code_id (int):
        json_body (PatchCodesCodeidJsonBody):

    Returns:
        Response[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]
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
    json_body: PatchCodesCodeidJsonBody,
) -> Response[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]:
    """/codes/{codeId}

     Update editable properties of a Source Code or Tag. This is a [JSON Patch](ref:json-patch) endpoint.

    Args:
        code_id (int):
        json_body (PatchCodesCodeidJsonBody):

    Returns:
        Response[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]
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
    json_body: PatchCodesCodeidJsonBody,
) -> Optional[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]:
    """/codes/{codeId}

     Update editable properties of a Source Code or Tag. This is a [JSON Patch](ref:json-patch) endpoint.

    Args:
        code_id (int):
        json_body (PatchCodesCodeidJsonBody):

    Returns:
        Response[Union[PatchCodesCodeidResponse204, PatchCodesCodeidResponse400]]
    """

    return (
        await asyncio_detailed(
            code_id=code_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
