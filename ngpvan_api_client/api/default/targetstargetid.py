from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.targetstargetid_response_400 import TargetstargetidResponse400
from ...models.targetstargetid_response_404 import TargetstargetidResponse404
from ...types import Response


def _get_kwargs(
    target_id: int = 15880,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/targets/{targetId}".format(client.base_url, targetId=target_id)

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
) -> Optional[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = TargetstargetidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = TargetstargetidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    target_id: int = 15880,
    *,
    client: Client,
) -> Response[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]:
    """/targets/{targetId}

     Use this endpoint to retrieve information about a specific Target (and its Subgroups) available in
    the current context.

    A standard [Target](ref:targets#common-models-37) object, if found.

    If the specified Target does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        target_id (int):  Default: 15880.

    Returns:
        Response[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]
    """

    kwargs = _get_kwargs(
        target_id=target_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    target_id: int = 15880,
    *,
    client: Client,
) -> Optional[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]:
    """/targets/{targetId}

     Use this endpoint to retrieve information about a specific Target (and its Subgroups) available in
    the current context.

    A standard [Target](ref:targets#common-models-37) object, if found.

    If the specified Target does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        target_id (int):  Default: 15880.

    Returns:
        Response[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]
    """

    return sync_detailed(
        target_id=target_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    target_id: int = 15880,
    *,
    client: Client,
) -> Response[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]:
    """/targets/{targetId}

     Use this endpoint to retrieve information about a specific Target (and its Subgroups) available in
    the current context.

    A standard [Target](ref:targets#common-models-37) object, if found.

    If the specified Target does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        target_id (int):  Default: 15880.

    Returns:
        Response[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]
    """

    kwargs = _get_kwargs(
        target_id=target_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    target_id: int = 15880,
    *,
    client: Client,
) -> Optional[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]:
    """/targets/{targetId}

     Use this endpoint to retrieve information about a specific Target (and its Subgroups) available in
    the current context.

    A standard [Target](ref:targets#common-models-37) object, if found.

    If the specified Target does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        target_id (int):  Default: 15880.

    Returns:
        Response[Union[Any, TargetstargetidResponse400, TargetstargetidResponse404]]
    """

    return (
        await asyncio_detailed(
            target_id=target_id,
            client=client,
        )
    ).parsed
