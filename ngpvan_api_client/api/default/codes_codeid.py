from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.codes_codeid_get_source_code_with_expand import CodesCodeidGetSourceCodeWithExpand
from ...models.codes_codeid_response_200_type_0 import CodesCodeidResponse200Type0
from ...models.codes_codeid_response_400 import CodesCodeidResponse400
from ...models.codes_codeid_response_404 import CodesCodeidResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    code_id: int,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/codes/{codeId}".format(client.base_url, codeId=code_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$expand"] = expand

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
) -> Optional[
    Union[
        CodesCodeidResponse400,
        CodesCodeidResponse404,
        Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0],
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = CodesCodeidResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = CodesCodeidGetSourceCodeWithExpand.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CodesCodeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = CodesCodeidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        CodesCodeidResponse400,
        CodesCodeidResponse404,
        Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0],
    ]
]:
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
    expand: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[
        CodesCodeidResponse400,
        CodesCodeidResponse404,
        Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0],
    ]
]:
    """/codes/{codeId}

     Use this endpoint to retrieve an existing Code and its metadata

    Args:
        code_id (int):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[CodesCodeidResponse400, CodesCodeidResponse404, Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0]]]
    """

    kwargs = _get_kwargs(
        code_id=code_id,
        client=client,
        expand=expand,
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
    expand: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[
        CodesCodeidResponse400,
        CodesCodeidResponse404,
        Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0],
    ]
]:
    """/codes/{codeId}

     Use this endpoint to retrieve an existing Code and its metadata

    Args:
        code_id (int):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[CodesCodeidResponse400, CodesCodeidResponse404, Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0]]]
    """

    return sync_detailed(
        code_id=code_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    code_id: int,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Response[
    Union[
        CodesCodeidResponse400,
        CodesCodeidResponse404,
        Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0],
    ]
]:
    """/codes/{codeId}

     Use this endpoint to retrieve an existing Code and its metadata

    Args:
        code_id (int):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[CodesCodeidResponse400, CodesCodeidResponse404, Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0]]]
    """

    kwargs = _get_kwargs(
        code_id=code_id,
        client=client,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    code_id: int,
    *,
    client: Client,
    expand: Union[Unset, None, str] = UNSET,
) -> Optional[
    Union[
        CodesCodeidResponse400,
        CodesCodeidResponse404,
        Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0],
    ]
]:
    """/codes/{codeId}

     Use this endpoint to retrieve an existing Code and its metadata

    Args:
        code_id (int):
        expand (Union[Unset, None, str]):

    Returns:
        Response[Union[CodesCodeidResponse400, CodesCodeidResponse404, Union[CodesCodeidGetSourceCodeWithExpand, CodesCodeidResponse200Type0]]]
    """

    return (
        await asyncio_detailed(
            code_id=code_id,
            client=client,
            expand=expand,
        )
    ).parsed
