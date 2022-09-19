from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.peoplevanid_1_response_200 import Peoplevanid1Response200
from ...models.peoplevanid_1_response_403 import Peoplevanid1Response403
from ...models.peoplevanid_1_response_404 import Peoplevanid1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    van_id: str = "100476252",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "phones,emails",
) -> Dict[str, Any]:
    url = "{}/people/{vanId}".format(client.base_url, vanId=van_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$expand"] = expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]:
    if response.status_code == 200:
        response_200 = Peoplevanid1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = Peoplevanid1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Peoplevanid1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]:
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
    expand: Union[Unset, None, str] = "phones,emails",
) -> Response[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]:
    """/people/{vanId}

     Retrieve a person record and associated contact information.

    Note the following with regards to `expand` parameter values:
    * The `addresses` value will provide best known Home and Mailing address, if available.
    * The `recordedAddresses` value will provide all available address history, but requires special
    permissions.
    * The `preferences` value is required to retrieve the following properties: `nickname`, `website`,
    `contactMethodPreferenceCode`, and `jobTitle`.


    If no Person with the indicated `vanId` is available, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        van_id (str):  Default: '100476252'.
        expand (Union[Unset, None, str]):  Default: 'phones,emails'.

    Returns:
        Response[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
        expand=expand,
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
    expand: Union[Unset, None, str] = "phones,emails",
) -> Optional[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]:
    """/people/{vanId}

     Retrieve a person record and associated contact information.

    Note the following with regards to `expand` parameter values:
    * The `addresses` value will provide best known Home and Mailing address, if available.
    * The `recordedAddresses` value will provide all available address history, but requires special
    permissions.
    * The `preferences` value is required to retrieve the following properties: `nickname`, `website`,
    `contactMethodPreferenceCode`, and `jobTitle`.


    If no Person with the indicated `vanId` is available, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        van_id (str):  Default: '100476252'.
        expand (Union[Unset, None, str]):  Default: 'phones,emails'.

    Returns:
        Response[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]
    """

    return sync_detailed(
        van_id=van_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    van_id: str = "100476252",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "phones,emails",
) -> Response[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]:
    """/people/{vanId}

     Retrieve a person record and associated contact information.

    Note the following with regards to `expand` parameter values:
    * The `addresses` value will provide best known Home and Mailing address, if available.
    * The `recordedAddresses` value will provide all available address history, but requires special
    permissions.
    * The `preferences` value is required to retrieve the following properties: `nickname`, `website`,
    `contactMethodPreferenceCode`, and `jobTitle`.


    If no Person with the indicated `vanId` is available, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        van_id (str):  Default: '100476252'.
        expand (Union[Unset, None, str]):  Default: 'phones,emails'.

    Returns:
        Response[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    van_id: str = "100476252",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "phones,emails",
) -> Optional[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]:
    """/people/{vanId}

     Retrieve a person record and associated contact information.

    Note the following with regards to `expand` parameter values:
    * The `addresses` value will provide best known Home and Mailing address, if available.
    * The `recordedAddresses` value will provide all available address history, but requires special
    permissions.
    * The `preferences` value is required to retrieve the following properties: `nickname`, `website`,
    `contactMethodPreferenceCode`, and `jobTitle`.


    If no Person with the indicated `vanId` is available, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        van_id (str):  Default: '100476252'.
        expand (Union[Unset, None, str]):  Default: 'phones,emails'.

    Returns:
        Response[Union[Peoplevanid1Response200, Peoplevanid1Response403, Peoplevanid1Response404]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
            expand=expand,
        )
    ).parsed
