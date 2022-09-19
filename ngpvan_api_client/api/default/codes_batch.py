from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.codes_batch_json_body import CodesBatchJsonBody
from ...models.codes_batch_response_201_item import CodesBatchResponse201Item
from ...models.codes_batch_response_400 import CodesBatchResponse400
from ...models.codes_batch_response_404 import CodesBatchResponse404
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CodesBatchJsonBody,
) -> Dict[str, Any]:
    url = "{}/codes/batch".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = CodesBatchResponse201Item.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201
    if response.status_code == 400:
        response_400 = CodesBatchResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = CodesBatchResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CodesBatchJsonBody,
) -> Response[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]:
    """/codes/batch

     Use this endpoint to create a batch of new Codes in the current context.

    Args:
        json_body (CodesBatchJsonBody):

    Returns:
        Response[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]
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
    json_body: CodesBatchJsonBody,
) -> Optional[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]:
    """/codes/batch

     Use this endpoint to create a batch of new Codes in the current context.

    Args:
        json_body (CodesBatchJsonBody):

    Returns:
        Response[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CodesBatchJsonBody,
) -> Response[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]:
    """/codes/batch

     Use this endpoint to create a batch of new Codes in the current context.

    Args:
        json_body (CodesBatchJsonBody):

    Returns:
        Response[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]
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
    json_body: CodesBatchJsonBody,
) -> Optional[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]:
    """/codes/batch

     Use this endpoint to create a batch of new Codes in the current context.

    Args:
        json_body (CodesBatchJsonBody):

    Returns:
        Response[Union[CodesBatchResponse400, CodesBatchResponse404, List[CodesBatchResponse201Item]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
