from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplevanidrelationships_json_body import PeoplevanidrelationshipsJsonBody
from ...models.peoplevanidrelationships_response_400 import PeoplevanidrelationshipsResponse400
from ...types import Response


def _get_kwargs(
    van_id: str = "100476252",
    *,
    client: Client,
    json_body: PeoplevanidrelationshipsJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/relationships".format(client.base_url, vanId=van_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PeoplevanidrelationshipsResponse400]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PeoplevanidrelationshipsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PeoplevanidrelationshipsResponse400]]:
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
    json_body: PeoplevanidrelationshipsJsonBody,
) -> Response[Union[Any, PeoplevanidrelationshipsResponse400]]:
    """/people/{vanId}/relationships

     Use this endpoint to create a single [Relationship](ref:relationships) between two People.


    The Person indicated in the body of the request is the “source” of the relationship, and the Person
    indicated in the URL route is the “destination” of the relationship. In this case, Person 7890123 is
    the mother of Person 123123.

    If the Person specified in the URL route does not exist, this endpoint will return an error with
    HTTP Status Code `404 Not Found`.

    If the Relationship or Person specified in the request body are not available, this endpoint will
    return an error or errors with HTTP Status Code `400 Bad Request`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevanidrelationshipsJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidrelationshipsResponse400]]
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
    json_body: PeoplevanidrelationshipsJsonBody,
) -> Optional[Union[Any, PeoplevanidrelationshipsResponse400]]:
    """/people/{vanId}/relationships

     Use this endpoint to create a single [Relationship](ref:relationships) between two People.


    The Person indicated in the body of the request is the “source” of the relationship, and the Person
    indicated in the URL route is the “destination” of the relationship. In this case, Person 7890123 is
    the mother of Person 123123.

    If the Person specified in the URL route does not exist, this endpoint will return an error with
    HTTP Status Code `404 Not Found`.

    If the Relationship or Person specified in the request body are not available, this endpoint will
    return an error or errors with HTTP Status Code `400 Bad Request`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevanidrelationshipsJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidrelationshipsResponse400]]
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
    json_body: PeoplevanidrelationshipsJsonBody,
) -> Response[Union[Any, PeoplevanidrelationshipsResponse400]]:
    """/people/{vanId}/relationships

     Use this endpoint to create a single [Relationship](ref:relationships) between two People.


    The Person indicated in the body of the request is the “source” of the relationship, and the Person
    indicated in the URL route is the “destination” of the relationship. In this case, Person 7890123 is
    the mother of Person 123123.

    If the Person specified in the URL route does not exist, this endpoint will return an error with
    HTTP Status Code `404 Not Found`.

    If the Relationship or Person specified in the request body are not available, this endpoint will
    return an error or errors with HTTP Status Code `400 Bad Request`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevanidrelationshipsJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidrelationshipsResponse400]]
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
    json_body: PeoplevanidrelationshipsJsonBody,
) -> Optional[Union[Any, PeoplevanidrelationshipsResponse400]]:
    """/people/{vanId}/relationships

     Use this endpoint to create a single [Relationship](ref:relationships) between two People.


    The Person indicated in the body of the request is the “source” of the relationship, and the Person
    indicated in the URL route is the “destination” of the relationship. In this case, Person 7890123 is
    the mother of Person 123123.

    If the Person specified in the URL route does not exist, this endpoint will return an error with
    HTTP Status Code `404 Not Found`.

    If the Relationship or Person specified in the request body are not available, this endpoint will
    return an error or errors with HTTP Status Code `400 Bad Request`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        van_id (str):  Default: '100476252'.
        json_body (PeoplevanidrelationshipsJsonBody):

    Returns:
        Response[Union[Any, PeoplevanidrelationshipsResponse400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
