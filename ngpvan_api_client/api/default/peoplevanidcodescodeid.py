from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplevanidcodescodeid_response_400 import PeoplevanidcodescodeidResponse400
from ...models.peoplevanidcodescodeid_response_404 import PeoplevanidcodescodeidResponse404
from ...types import Response


def _get_kwargs(
    van_id: str = "100476252",
    code_id: str = "20545",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/codes/{codeId}".format(client.base_url, vanId=van_id, codeId=code_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PeoplevanidcodescodeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = PeoplevanidcodescodeidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    van_id: str = "100476252",
    code_id: str = "20545",
    *,
    client: Client,
) -> Response[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]:
    """/people/{vanId}/codes/{codeId}

     Use this endpoint to remove a single [Code](ref:codes) from a Person.

    Args:
        van_id (str):  Default: '100476252'.
        code_id (str):  Default: '20545'.

    Returns:
        Response[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        code_id=code_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    van_id: str = "100476252",
    code_id: str = "20545",
    *,
    client: Client,
) -> Optional[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]:
    """/people/{vanId}/codes/{codeId}

     Use this endpoint to remove a single [Code](ref:codes) from a Person.

    Args:
        van_id (str):  Default: '100476252'.
        code_id (str):  Default: '20545'.

    Returns:
        Response[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]
    """

    return sync_detailed(
        van_id=van_id,
        code_id=code_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    van_id: str = "100476252",
    code_id: str = "20545",
    *,
    client: Client,
) -> Response[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]:
    """/people/{vanId}/codes/{codeId}

     Use this endpoint to remove a single [Code](ref:codes) from a Person.

    Args:
        van_id (str):  Default: '100476252'.
        code_id (str):  Default: '20545'.

    Returns:
        Response[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        code_id=code_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    van_id: str = "100476252",
    code_id: str = "20545",
    *,
    client: Client,
) -> Optional[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]:
    """/people/{vanId}/codes/{codeId}

     Use this endpoint to remove a single [Code](ref:codes) from a Person.

    Args:
        van_id (str):  Default: '100476252'.
        code_id (str):  Default: '20545'.

    Returns:
        Response[Union[Any, PeoplevanidcodescodeidResponse400, PeoplevanidcodescodeidResponse404]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            code_id=code_id,
            client=client,
        )
    ).parsed
