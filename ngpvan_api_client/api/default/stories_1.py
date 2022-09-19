from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.stories_1_json_body import Stories1JsonBody
from ...models.stories_1_response_201 import Stories1Response201
from ...models.stories_1_response_400 import Stories1Response400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Stories1JsonBody,
) -> Dict[str, Any]:
    url = "{}/stories".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Stories1Response201, Stories1Response400]]:
    if response.status_code == 201:
        response_201 = Stories1Response201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Stories1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Stories1Response201, Stories1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Stories1JsonBody,
) -> Response[Union[Stories1Response201, Stories1Response400]]:
    """/stories

     Use this endpoint to create a new Story.

    Accepts a standard [Story](ref:stories#common-models-34) object, simple types and no read-only
    values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created`. The response body will
    contain a [Story](ref:stories#common-models-34) object populated with the new Story’s integer
    StoryId.

    Args:
        json_body (Stories1JsonBody):

    Returns:
        Response[Union[Stories1Response201, Stories1Response400]]
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
    json_body: Stories1JsonBody,
) -> Optional[Union[Stories1Response201, Stories1Response400]]:
    """/stories

     Use this endpoint to create a new Story.

    Accepts a standard [Story](ref:stories#common-models-34) object, simple types and no read-only
    values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created`. The response body will
    contain a [Story](ref:stories#common-models-34) object populated with the new Story’s integer
    StoryId.

    Args:
        json_body (Stories1JsonBody):

    Returns:
        Response[Union[Stories1Response201, Stories1Response400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Stories1JsonBody,
) -> Response[Union[Stories1Response201, Stories1Response400]]:
    """/stories

     Use this endpoint to create a new Story.

    Accepts a standard [Story](ref:stories#common-models-34) object, simple types and no read-only
    values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created`. The response body will
    contain a [Story](ref:stories#common-models-34) object populated with the new Story’s integer
    StoryId.

    Args:
        json_body (Stories1JsonBody):

    Returns:
        Response[Union[Stories1Response201, Stories1Response400]]
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
    json_body: Stories1JsonBody,
) -> Optional[Union[Stories1Response201, Stories1Response400]]:
    """/stories

     Use this endpoint to create a new Story.

    Accepts a standard [Story](ref:stories#common-models-34) object, simple types and no read-only
    values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created`. The response body will
    contain a [Story](ref:stories#common-models-34) object populated with the new Story’s integer
    StoryId.

    Args:
        json_body (Stories1JsonBody):

    Returns:
        Response[Union[Stories1Response201, Stories1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
