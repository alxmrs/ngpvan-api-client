from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplevanidcanvassresponses_json_body import PeoplevanidcanvassresponsesJsonBody
from ...models.peoplevanidcanvassresponses_response_400 import PeoplevanidcanvassresponsesResponse400
from ...types import Response


def _get_kwargs(
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidcanvassresponsesJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/canvassResponses".format(client.base_url, vanId=van_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PeoplevanidcanvassresponsesResponse400]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PeoplevanidcanvassresponsesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PeoplevanidcanvassresponsesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidcanvassresponsesJsonBody,
) -> Response[Union[Any, PeoplevanidcanvassresponsesResponse400]]:
    """/people/{vanId}/canvassResponses

     A Canvass Response encapsulates a complete interaction with a person: it may have a Result Code (if
    the person was unavailable) or it may have an array of responses such as Activist Codes, Survey
    Questions, and other Script elements. Optionally, additional information about the canvass
    interaction can be specified using the `canvassContext` property such as the date of the contact
    attempt (`dateCanvassed`) or the Contact Type (`contactTypeId`). Use this endpoint to record these
    interactions.

    Args:
        van_id (int):
        json_body (PeoplevanidcanvassresponsesJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidcanvassresponsesResponse400]]
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
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidcanvassresponsesJsonBody,
) -> Optional[Union[Any, PeoplevanidcanvassresponsesResponse400]]:
    """/people/{vanId}/canvassResponses

     A Canvass Response encapsulates a complete interaction with a person: it may have a Result Code (if
    the person was unavailable) or it may have an array of responses such as Activist Codes, Survey
    Questions, and other Script elements. Optionally, additional information about the canvass
    interaction can be specified using the `canvassContext` property such as the date of the contact
    attempt (`dateCanvassed`) or the Contact Type (`contactTypeId`). Use this endpoint to record these
    interactions.

    Args:
        van_id (int):
        json_body (PeoplevanidcanvassresponsesJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidcanvassresponsesResponse400]]
    """

    return sync_detailed(
        van_id=van_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidcanvassresponsesJsonBody,
) -> Response[Union[Any, PeoplevanidcanvassresponsesResponse400]]:
    """/people/{vanId}/canvassResponses

     A Canvass Response encapsulates a complete interaction with a person: it may have a Result Code (if
    the person was unavailable) or it may have an array of responses such as Activist Codes, Survey
    Questions, and other Script elements. Optionally, additional information about the canvass
    interaction can be specified using the `canvassContext` property such as the date of the contact
    attempt (`dateCanvassed`) or the Contact Type (`contactTypeId`). Use this endpoint to record these
    interactions.

    Args:
        van_id (int):
        json_body (PeoplevanidcanvassresponsesJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidcanvassresponsesResponse400]]
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
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidcanvassresponsesJsonBody,
) -> Optional[Union[Any, PeoplevanidcanvassresponsesResponse400]]:
    """/people/{vanId}/canvassResponses

     A Canvass Response encapsulates a complete interaction with a person: it may have a Result Code (if
    the person was unavailable) or it may have an array of responses such as Activist Codes, Survey
    Questions, and other Script elements. Optionally, additional information about the canvass
    interaction can be specified using the `canvassContext` property such as the date of the contact
    attempt (`dateCanvassed`) or the Contact Type (`contactTypeId`). Use this endpoint to record these
    interactions.

    Args:
        van_id (int):
        json_body (PeoplevanidcanvassresponsesJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidcanvassresponsesResponse400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
