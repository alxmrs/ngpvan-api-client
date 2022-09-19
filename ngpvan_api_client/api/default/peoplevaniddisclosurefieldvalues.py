from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplevaniddisclosurefieldvalues_json_body import PeoplevaniddisclosurefieldvaluesJsonBody
from ...models.peoplevaniddisclosurefieldvalues_response_400 import PeoplevaniddisclosurefieldvaluesResponse400
from ...types import Response


def _get_kwargs(
    van_id: str = "100476252",
    *,
    client: Client,
    json_body: PeoplevaniddisclosurefieldvaluesJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/disclosureFieldValues".format(client.base_url, vanId=van_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PeoplevaniddisclosurefieldvaluesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]:
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
    json_body: PeoplevaniddisclosurefieldvaluesJsonBody,
) -> Response[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]:
    """/people/{vanId}/disclosureFieldValues

     Sets or updates the values of [Disclosure Fields](ref:people#disclosure-field-values).

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevaniddisclosurefieldvaluesJsonBody):

    Returns:
        Response[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]
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
    json_body: PeoplevaniddisclosurefieldvaluesJsonBody,
) -> Optional[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]:
    """/people/{vanId}/disclosureFieldValues

     Sets or updates the values of [Disclosure Fields](ref:people#disclosure-field-values).

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevaniddisclosurefieldvaluesJsonBody):

    Returns:
        Response[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]
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
    json_body: PeoplevaniddisclosurefieldvaluesJsonBody,
) -> Response[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]:
    """/people/{vanId}/disclosureFieldValues

     Sets or updates the values of [Disclosure Fields](ref:people#disclosure-field-values).

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevaniddisclosurefieldvaluesJsonBody):

    Returns:
        Response[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]
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
    json_body: PeoplevaniddisclosurefieldvaluesJsonBody,
) -> Optional[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]:
    """/people/{vanId}/disclosureFieldValues

     Sets or updates the values of [Disclosure Fields](ref:people#disclosure-field-values).

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevaniddisclosurefieldvaluesJsonBody):

    Returns:
        Response[Union[Any, PeoplevaniddisclosurefieldvaluesResponse400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
