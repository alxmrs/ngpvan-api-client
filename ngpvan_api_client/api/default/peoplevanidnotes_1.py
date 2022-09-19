from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplevanidnotes_1_json_body import Peoplevanidnotes1JsonBody
from ...models.peoplevanidnotes_1_response_400 import Peoplevanidnotes1Response400
from ...types import Response


def _get_kwargs(
    van_id: str = "100476252",
    *,
    client: Client,
    json_body: Peoplevanidnotes1JsonBody,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/notes".format(client.base_url, vanId=van_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Peoplevanidnotes1Response400]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = Peoplevanidnotes1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Peoplevanidnotes1Response400]]:
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
    json_body: Peoplevanidnotes1JsonBody,
) -> Response[Union[Any, Peoplevanidnotes1Response400]]:
    """/people/{vanId}/notes

     Add Notes to a Person using a free-form text description.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (Peoplevanidnotes1JsonBody):

    Returns:
        Response[Union[Any, Peoplevanidnotes1Response400]]
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
    van_id: str = "100476252",
    *,
    client: Client,
    json_body: Peoplevanidnotes1JsonBody,
) -> Optional[Union[Any, Peoplevanidnotes1Response400]]:
    """/people/{vanId}/notes

     Add Notes to a Person using a free-form text description.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (Peoplevanidnotes1JsonBody):

    Returns:
        Response[Union[Any, Peoplevanidnotes1Response400]]
    """

    return sync_detailed(
        van_id=van_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    van_id: str = "100476252",
    *,
    client: Client,
    json_body: Peoplevanidnotes1JsonBody,
) -> Response[Union[Any, Peoplevanidnotes1Response400]]:
    """/people/{vanId}/notes

     Add Notes to a Person using a free-form text description.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (Peoplevanidnotes1JsonBody):

    Returns:
        Response[Union[Any, Peoplevanidnotes1Response400]]
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
    van_id: str = "100476252",
    *,
    client: Client,
    json_body: Peoplevanidnotes1JsonBody,
) -> Optional[Union[Any, Peoplevanidnotes1Response400]]:
    """/people/{vanId}/notes

     Add Notes to a Person using a free-form text description.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (Peoplevanidnotes1JsonBody):

    Returns:
        Response[Union[Any, Peoplevanidnotes1Response400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
