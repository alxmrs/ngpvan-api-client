from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.storiesstoryid_response_200 import StoriesstoryidResponse200
from ...models.storiesstoryid_response_400 import StoriesstoryidResponse400
from ...models.storiesstoryid_response_404 import StoriesstoryidResponse404
from ...types import Response


def _get_kwargs(
    story_id: int = 123,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/stories/{storyId}".format(client.base_url, storyId=story_id)

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
) -> Optional[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]:
    if response.status_code == 200:
        response_200 = StoriesstoryidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = StoriesstoryidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = StoriesstoryidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    story_id: int = 123,
    *,
    client: Client,
) -> Response[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]:
    """/stories/{storyId}

     Use this endpoint to retrieve the details of a specific Story.

    Returns a standard [Story](ref:stories#common-models-34) object, if found.

    If the specified Story does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    Args:
        story_id (int):  Default: 123.

    Returns:
        Response[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]
    """

    kwargs = _get_kwargs(
        story_id=story_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    story_id: int = 123,
    *,
    client: Client,
) -> Optional[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]:
    """/stories/{storyId}

     Use this endpoint to retrieve the details of a specific Story.

    Returns a standard [Story](ref:stories#common-models-34) object, if found.

    If the specified Story does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    Args:
        story_id (int):  Default: 123.

    Returns:
        Response[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]
    """

    return sync_detailed(
        story_id=story_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    story_id: int = 123,
    *,
    client: Client,
) -> Response[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]:
    """/stories/{storyId}

     Use this endpoint to retrieve the details of a specific Story.

    Returns a standard [Story](ref:stories#common-models-34) object, if found.

    If the specified Story does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    Args:
        story_id (int):  Default: 123.

    Returns:
        Response[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]
    """

    kwargs = _get_kwargs(
        story_id=story_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    story_id: int = 123,
    *,
    client: Client,
) -> Optional[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]:
    """/stories/{storyId}

     Use this endpoint to retrieve the details of a specific Story.

    Returns a standard [Story](ref:stories#common-models-34) object, if found.

    If the specified Story does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    Args:
        story_id (int):  Default: 123.

    Returns:
        Response[Union[StoriesstoryidResponse200, StoriesstoryidResponse400, StoriesstoryidResponse404]]
    """

    return (
        await asyncio_detailed(
            story_id=story_id,
            client=client,
        )
    ).parsed
