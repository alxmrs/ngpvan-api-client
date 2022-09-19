from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplevanidmyactivistflags_1_response_400 import Peoplevanidmyactivistflags1Response400
from ...types import Response


def _get_kwargs(
    van_id: str = "100476252",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/myActivistFlags".format(client.base_url, vanId=van_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Peoplevanidmyactivistflags1Response400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = Peoplevanidmyactivistflags1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Peoplevanidmyactivistflags1Response400]]:
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
) -> Response[Union[Any, Peoplevanidmyactivistflags1Response400]]:
    """/people/{vanId}/myActivistFlags

     Remove the My Activist flag from a person. Prevents this person, who belongs to a master data
    sharing committee, from being be viewed in the current context as an activist.

    Args:
        van_id (str):  Default: '100476252'.

    Returns:
        Response[Union[Any, Peoplevanidmyactivistflags1Response400]]
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
) -> Optional[Union[Any, Peoplevanidmyactivistflags1Response400]]:
    """/people/{vanId}/myActivistFlags

     Remove the My Activist flag from a person. Prevents this person, who belongs to a master data
    sharing committee, from being be viewed in the current context as an activist.

    Args:
        van_id (str):  Default: '100476252'.

    Returns:
        Response[Union[Any, Peoplevanidmyactivistflags1Response400]]
    """

    return sync_detailed(
        van_id=van_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    van_id: str = "100476252",
    *,
    client: Client,
) -> Response[Union[Any, Peoplevanidmyactivistflags1Response400]]:
    """/people/{vanId}/myActivistFlags

     Remove the My Activist flag from a person. Prevents this person, who belongs to a master data
    sharing committee, from being be viewed in the current context as an activist.

    Args:
        van_id (str):  Default: '100476252'.

    Returns:
        Response[Union[Any, Peoplevanidmyactivistflags1Response400]]
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
) -> Optional[Union[Any, Peoplevanidmyactivistflags1Response400]]:
    """/people/{vanId}/myActivistFlags

     Remove the My Activist flag from a person. Prevents this person, who belongs to a master data
    sharing committee, from being be viewed in the current context as an activist.

    Args:
        van_id (str):  Default: '100476252'.

    Returns:
        Response[Union[Any, Peoplevanidmyactivistflags1Response400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
        )
    ).parsed
