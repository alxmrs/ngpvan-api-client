from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.peoplevanidnames_json_body import PeoplevanidnamesJsonBody
from ...models.peoplevanidnames_response_200 import PeoplevanidnamesResponse200
from ...models.peoplevanidnames_response_400 import PeoplevanidnamesResponse400
from ...models.peoplevanidnames_response_404 import PeoplevanidnamesResponse404
from ...types import Response


def _get_kwargs(
    van_id: str = "12345678",
    *,
    client: Client,
    json_body: PeoplevanidnamesJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/names".format(client.base_url, vanId=van_id)

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
) -> Optional[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]:
    if response.status_code == 200:
        response_200 = PeoplevanidnamesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PeoplevanidnamesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = PeoplevanidnamesResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    van_id: str = "12345678",
    *,
    client: Client,
    json_body: PeoplevanidnamesJsonBody,
) -> Response[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]:
    """/people/{vanId}/names

    Args:
        van_id (str):  Default: '12345678'.
        json_body (PeoplevanidnamesJsonBody):

    Returns:
        Response[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    van_id: str = "12345678",
    *,
    client: Client,
    json_body: PeoplevanidnamesJsonBody,
) -> Optional[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]:
    """/people/{vanId}/names

    Args:
        van_id (str):  Default: '12345678'.
        json_body (PeoplevanidnamesJsonBody):

    Returns:
        Response[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]
    """

    return sync_detailed(
        van_id=van_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    van_id: str = "12345678",
    *,
    client: Client,
    json_body: PeoplevanidnamesJsonBody,
) -> Response[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]:
    """/people/{vanId}/names

    Args:
        van_id (str):  Default: '12345678'.
        json_body (PeoplevanidnamesJsonBody):

    Returns:
        Response[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    van_id: str = "12345678",
    *,
    client: Client,
    json_body: PeoplevanidnamesJsonBody,
) -> Optional[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]:
    """/people/{vanId}/names

    Args:
        van_id (str):  Default: '12345678'.
        json_body (PeoplevanidnamesJsonBody):

    Returns:
        Response[Union[PeoplevanidnamesResponse200, PeoplevanidnamesResponse400, PeoplevanidnamesResponse404]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
