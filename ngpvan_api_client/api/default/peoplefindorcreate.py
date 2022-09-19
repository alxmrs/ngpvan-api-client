from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.peoplefindorcreate_json_body import PeoplefindorcreateJsonBody
from ...models.peoplefindorcreate_response_200 import PeoplefindorcreateResponse200
from ...models.peoplefindorcreate_response_400 import PeoplefindorcreateResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PeoplefindorcreateJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/findOrCreate".format(client.base_url)

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
) -> Optional[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]:
    if response.status_code == 200:
        response_200 = PeoplefindorcreateResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PeoplefindorcreateResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PeoplefindorcreateJsonBody,
) -> Response[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]:
    """/people/findOrCreate

     Attempts to find the given match candidate. If a person is found, it is updated with the information
    provided. If a person is not found, a new person record is created.

    See [Common Models](ref:people#common-models) for a full list of fields.

    Args:
        json_body (PeoplefindorcreateJsonBody):

    Returns:
        Response[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]
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
    json_body: PeoplefindorcreateJsonBody,
) -> Optional[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]:
    """/people/findOrCreate

     Attempts to find the given match candidate. If a person is found, it is updated with the information
    provided. If a person is not found, a new person record is created.

    See [Common Models](ref:people#common-models) for a full list of fields.

    Args:
        json_body (PeoplefindorcreateJsonBody):

    Returns:
        Response[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PeoplefindorcreateJsonBody,
) -> Response[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]:
    """/people/findOrCreate

     Attempts to find the given match candidate. If a person is found, it is updated with the information
    provided. If a person is not found, a new person record is created.

    See [Common Models](ref:people#common-models) for a full list of fields.

    Args:
        json_body (PeoplefindorcreateJsonBody):

    Returns:
        Response[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]
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
    json_body: PeoplefindorcreateJsonBody,
) -> Optional[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]:
    """/people/findOrCreate

     Attempts to find the given match candidate. If a person is found, it is updated with the information
    provided. If a person is not found, a new person record is created.

    See [Common Models](ref:people#common-models) for a full list of fields.

    Args:
        json_body (PeoplefindorcreateJsonBody):

    Returns:
        Response[Union[PeoplefindorcreateResponse200, PeoplefindorcreateResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
