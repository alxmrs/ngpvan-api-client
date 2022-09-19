from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplevanidnotesnoteid_json_body import PeoplevanidnotesnoteidJsonBody
from ...models.peoplevanidnotesnoteid_response_400 import PeoplevanidnotesnoteidResponse400
from ...types import Response


def _get_kwargs(
    van_id: str = "100476252",
    note_id: str = "225",
    *,
    client: Client,
    json_body: PeoplevanidnotesnoteidJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/notes/{noteId}".format(client.base_url, vanId=van_id, noteId=note_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PeoplevanidnotesnoteidResponse400]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PeoplevanidnotesnoteidResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PeoplevanidnotesnoteidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    van_id: str = "100476252",
    note_id: str = "225",
    *,
    client: Client,
    json_body: PeoplevanidnotesnoteidJsonBody,
) -> Response[Union[Any, PeoplevanidnotesnoteidResponse400]]:
    """/people/{vanId}/notes/{noteId}

     Updates properties on an existing Note record. Only `text`, `isViewRestricted`, and `category` may
    be updated.

    Args:
        van_id (str):  Default: '100476252'.
        note_id (str):  Default: '225'.
        json_body (PeoplevanidnotesnoteidJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidnotesnoteidResponse400]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        note_id=note_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    van_id: str = "100476252",
    note_id: str = "225",
    *,
    client: Client,
    json_body: PeoplevanidnotesnoteidJsonBody,
) -> Optional[Union[Any, PeoplevanidnotesnoteidResponse400]]:
    """/people/{vanId}/notes/{noteId}

     Updates properties on an existing Note record. Only `text`, `isViewRestricted`, and `category` may
    be updated.

    Args:
        van_id (str):  Default: '100476252'.
        note_id (str):  Default: '225'.
        json_body (PeoplevanidnotesnoteidJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidnotesnoteidResponse400]]
    """

    return sync_detailed(
        van_id=van_id,
        note_id=note_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    van_id: str = "100476252",
    note_id: str = "225",
    *,
    client: Client,
    json_body: PeoplevanidnotesnoteidJsonBody,
) -> Response[Union[Any, PeoplevanidnotesnoteidResponse400]]:
    """/people/{vanId}/notes/{noteId}

     Updates properties on an existing Note record. Only `text`, `isViewRestricted`, and `category` may
    be updated.

    Args:
        van_id (str):  Default: '100476252'.
        note_id (str):  Default: '225'.
        json_body (PeoplevanidnotesnoteidJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidnotesnoteidResponse400]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        note_id=note_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    van_id: str = "100476252",
    note_id: str = "225",
    *,
    client: Client,
    json_body: PeoplevanidnotesnoteidJsonBody,
) -> Optional[Union[Any, PeoplevanidnotesnoteidResponse400]]:
    """/people/{vanId}/notes/{noteId}

     Updates properties on an existing Note record. Only `text`, `isViewRestricted`, and `category` may
    be updated.

    Args:
        van_id (str):  Default: '100476252'.
        note_id (str):  Default: '225'.
        json_body (PeoplevanidnotesnoteidJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidnotesnoteidResponse400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            note_id=note_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
