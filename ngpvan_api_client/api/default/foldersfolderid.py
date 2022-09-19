from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.foldersfolderid_response_400 import FoldersfolderidResponse400
from ...models.foldersfolderid_response_404 import FoldersfolderidResponse404
from ...types import Response


def _get_kwargs(
    folder_id: int = 44,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/folders/{folderId}".format(client.base_url, folderId=folder_id)

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
) -> Optional[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = FoldersfolderidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = FoldersfolderidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    folder_id: int = 44,
    *,
    client: Client,
) -> Response[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]:
    """/folders/{folderId}

     Use this endpoint to get full details for a folder.

    Args:
        folder_id (int):  Default: 44.

    Returns:
        Response[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    folder_id: int = 44,
    *,
    client: Client,
) -> Optional[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]:
    """/folders/{folderId}

     Use this endpoint to get full details for a folder.

    Args:
        folder_id (int):  Default: 44.

    Returns:
        Response[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]
    """

    return sync_detailed(
        folder_id=folder_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    folder_id: int = 44,
    *,
    client: Client,
) -> Response[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]:
    """/folders/{folderId}

     Use this endpoint to get full details for a folder.

    Args:
        folder_id (int):  Default: 44.

    Returns:
        Response[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]
    """

    kwargs = _get_kwargs(
        folder_id=folder_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    folder_id: int = 44,
    *,
    client: Client,
) -> Optional[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]:
    """/folders/{folderId}

     Use this endpoint to get full details for a folder.

    Args:
        folder_id (int):  Default: 44.

    Returns:
        Response[Union[Any, FoldersfolderidResponse400, FoldersfolderidResponse404]]
    """

    return (
        await asyncio_detailed(
            folder_id=folder_id,
            client=client,
        )
    ).parsed
