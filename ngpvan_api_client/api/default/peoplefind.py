from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.peoplefind_json_body import PeoplefindJsonBody
from ...models.peoplefind_response_200 import PeoplefindResponse200
from ...models.peoplefind_response_400 import PeoplefindResponse400
from ...models.peoplefind_response_404 import PeoplefindResponse404
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PeoplefindJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/find".format(client.base_url)

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
) -> Optional[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]:
    if response.status_code == 200:
        response_200 = PeoplefindResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PeoplefindResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = PeoplefindResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PeoplefindJsonBody,
) -> Response[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]:
    """/people/find

     Attempts to find a person using the given match candidate. See [Common Models](ref:people#common-
    models) for a full list of fields.

    Args:
        json_body (PeoplefindJsonBody):

    Returns:
        Response[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]
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
    json_body: PeoplefindJsonBody,
) -> Optional[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]:
    """/people/find

     Attempts to find a person using the given match candidate. See [Common Models](ref:people#common-
    models) for a full list of fields.

    Args:
        json_body (PeoplefindJsonBody):

    Returns:
        Response[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PeoplefindJsonBody,
) -> Response[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]:
    """/people/find

     Attempts to find a person using the given match candidate. See [Common Models](ref:people#common-
    models) for a full list of fields.

    Args:
        json_body (PeoplefindJsonBody):

    Returns:
        Response[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]
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
    json_body: PeoplefindJsonBody,
) -> Optional[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]:
    """/people/find

     Attempts to find a person using the given match candidate. See [Common Models](ref:people#common-
    models) for a full list of fields.

    Args:
        json_body (PeoplefindJsonBody):

    Returns:
        Response[Union[PeoplefindResponse200, PeoplefindResponse400, PeoplefindResponse404]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
