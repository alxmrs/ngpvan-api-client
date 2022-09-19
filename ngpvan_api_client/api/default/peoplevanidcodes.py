from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplevanidcodes_json_body import PeoplevanidcodesJsonBody
from ...models.peoplevanidcodes_response_400 import PeoplevanidcodesResponse400
from ...models.peoplevanidcodes_response_404 import PeoplevanidcodesResponse404
from ...types import Response


def _get_kwargs(
    van_id: str = "100476252",
    *,
    client: Client,
    json_body: PeoplevanidcodesJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/codes".format(client.base_url, vanId=van_id)

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
) -> Optional[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PeoplevanidcodesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = PeoplevanidcodesResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]:
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
    json_body: PeoplevanidcodesJsonBody,
) -> Response[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]:
    """/people/{vanId}/codes

     Use this endpoint to apply a single [Code](ref:codes) to a Person.

    If the specified Person does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found.`

    If the specified Person does exist but the Code does not or cannot be applied to People, this
    endpoint will return an error with HTTP Status Code `400 Bad Request`.

    In some contexts it is possible to apply both Tags and Source Codes to People. In these contexts,
    any number of Tags and Source Codes may be accepted. However:

    * If any Source Codes are applied to a Person within 24 hours of the creation of a Person record,
    then the first such Source Code will be marked as the Origin Source Code for the Person. Otherwise,
    the Person will have no Origin Source Code.
    * If an Origin Source Code exists for a Person, it will be displayed in the user interface;
    otherwise, no Source Codes for a Person will be displayed in the user interface.
    * All Tags for a Person will be displayed in the user interface.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevanidcodesJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]
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
    json_body: PeoplevanidcodesJsonBody,
) -> Optional[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]:
    """/people/{vanId}/codes

     Use this endpoint to apply a single [Code](ref:codes) to a Person.

    If the specified Person does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found.`

    If the specified Person does exist but the Code does not or cannot be applied to People, this
    endpoint will return an error with HTTP Status Code `400 Bad Request`.

    In some contexts it is possible to apply both Tags and Source Codes to People. In these contexts,
    any number of Tags and Source Codes may be accepted. However:

    * If any Source Codes are applied to a Person within 24 hours of the creation of a Person record,
    then the first such Source Code will be marked as the Origin Source Code for the Person. Otherwise,
    the Person will have no Origin Source Code.
    * If an Origin Source Code exists for a Person, it will be displayed in the user interface;
    otherwise, no Source Codes for a Person will be displayed in the user interface.
    * All Tags for a Person will be displayed in the user interface.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevanidcodesJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]
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
    json_body: PeoplevanidcodesJsonBody,
) -> Response[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]:
    """/people/{vanId}/codes

     Use this endpoint to apply a single [Code](ref:codes) to a Person.

    If the specified Person does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found.`

    If the specified Person does exist but the Code does not or cannot be applied to People, this
    endpoint will return an error with HTTP Status Code `400 Bad Request`.

    In some contexts it is possible to apply both Tags and Source Codes to People. In these contexts,
    any number of Tags and Source Codes may be accepted. However:

    * If any Source Codes are applied to a Person within 24 hours of the creation of a Person record,
    then the first such Source Code will be marked as the Origin Source Code for the Person. Otherwise,
    the Person will have no Origin Source Code.
    * If an Origin Source Code exists for a Person, it will be displayed in the user interface;
    otherwise, no Source Codes for a Person will be displayed in the user interface.
    * All Tags for a Person will be displayed in the user interface.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevanidcodesJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]
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
    json_body: PeoplevanidcodesJsonBody,
) -> Optional[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]:
    """/people/{vanId}/codes

     Use this endpoint to apply a single [Code](ref:codes) to a Person.

    If the specified Person does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found.`

    If the specified Person does exist but the Code does not or cannot be applied to People, this
    endpoint will return an error with HTTP Status Code `400 Bad Request`.

    In some contexts it is possible to apply both Tags and Source Codes to People. In these contexts,
    any number of Tags and Source Codes may be accepted. However:

    * If any Source Codes are applied to a Person within 24 hours of the creation of a Person record,
    then the first such Source Code will be marked as the Origin Source Code for the Person. Otherwise,
    the Person will have no Origin Source Code.
    * If an Origin Source Code exists for a Person, it will be displayed in the user interface;
    otherwise, no Source Codes for a Person will be displayed in the user interface.
    * All Tags for a Person will be displayed in the user interface.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevanidcodesJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidcodesResponse400, PeoplevanidcodesResponse404]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
