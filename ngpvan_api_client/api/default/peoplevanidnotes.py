from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.peoplevanidnotes_response_200 import PeoplevanidnotesResponse200
from ...models.peoplevanidnotes_response_400 import PeoplevanidnotesResponse400
from ...types import Response


def _get_kwargs(
    van_id: str = "100476252",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/notes".format(client.base_url, vanId=van_id)

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
) -> Optional[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]:
    if response.status_code == 200:
        response_200 = PeoplevanidnotesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PeoplevanidnotesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    van_id: str = "100476252",
    *,
    client: Client,
) -> Response[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]:
    """/people/{vanId}/notes

     Retrieves a list of Notes on a Person.

    This endpoint accepts [standard pagination parameters](ref:pagination) and returns a standard
    paginated response.

    By default, this endpoint returns 25 records per request. A maximum of 50 records per request is
    allowed via the `$top` parameter.

    Args:
        van_id (str):  Default: '100476252'.

    Returns:
        Response[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    van_id: str = "100476252",
    *,
    client: Client,
) -> Optional[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]:
    """/people/{vanId}/notes

     Retrieves a list of Notes on a Person.

    This endpoint accepts [standard pagination parameters](ref:pagination) and returns a standard
    paginated response.

    By default, this endpoint returns 25 records per request. A maximum of 50 records per request is
    allowed via the `$top` parameter.

    Args:
        van_id (str):  Default: '100476252'.

    Returns:
        Response[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]
    """

    return sync_detailed(
        van_id=van_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    van_id: str = "100476252",
    *,
    client: Client,
) -> Response[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]:
    """/people/{vanId}/notes

     Retrieves a list of Notes on a Person.

    This endpoint accepts [standard pagination parameters](ref:pagination) and returns a standard
    paginated response.

    By default, this endpoint returns 25 records per request. A maximum of 50 records per request is
    allowed via the `$top` parameter.

    Args:
        van_id (str):  Default: '100476252'.

    Returns:
        Response[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    van_id: str = "100476252",
    *,
    client: Client,
) -> Optional[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]:
    """/people/{vanId}/notes

     Retrieves a list of Notes on a Person.

    This endpoint accepts [standard pagination parameters](ref:pagination) and returns a standard
    paginated response.

    By default, this endpoint returns 25 records per request. A maximum of 50 records per request is
    allowed via the `$top` parameter.

    Args:
        van_id (str):  Default: '100476252'.

    Returns:
        Response[Union[PeoplevanidnotesResponse200, PeoplevanidnotesResponse400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
        )
    ).parsed
