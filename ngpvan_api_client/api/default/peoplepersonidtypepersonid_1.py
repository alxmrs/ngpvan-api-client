from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.peoplepersonidtypepersonid_1_response_200 import Peoplepersonidtypepersonid1Response200
from ...models.peoplepersonidtypepersonid_1_response_403 import Peoplepersonidtypepersonid1Response403
from ...models.peoplepersonidtypepersonid_1_response_404 import Peoplepersonidtypepersonid1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id_type: str = "GWID",
    person_id: str = "3",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "phones,emails",
) -> Dict[str, Any]:
    url = "{}/people/{personIdType}:{personId}".format(client.base_url, personIdType=person_id_type, personId=person_id)

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
) -> Optional[
    Union[
        Peoplepersonidtypepersonid1Response200,
        Peoplepersonidtypepersonid1Response403,
        Peoplepersonidtypepersonid1Response404,
    ]
]:
    if response.status_code == 200:
        response_200 = Peoplepersonidtypepersonid1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = Peoplepersonidtypepersonid1Response403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Peoplepersonidtypepersonid1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        Peoplepersonidtypepersonid1Response200,
        Peoplepersonidtypepersonid1Response403,
        Peoplepersonidtypepersonid1Response404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    person_id_type: str = "GWID",
    person_id: str = "3",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "phones,emails",
) -> Response[
    Union[
        Peoplepersonidtypepersonid1Response200,
        Peoplepersonidtypepersonid1Response403,
        Peoplepersonidtypepersonid1Response404,
    ]
]:
    """/people/{personIdType}:{personId}

     Retrieve a person record and associated contact information. For example `/people/DWID:12345` would
    retrieve a person whose DWID is 12345.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        expand (Union[Unset, None, str]):  Default: 'phones,emails'.

    Returns:
        Response[Union[Peoplepersonidtypepersonid1Response200, Peoplepersonidtypepersonid1Response403, Peoplepersonidtypepersonid1Response404]]
    """

    kwargs = _get_kwargs(
        person_id_type=person_id_type,
        person_id=person_id,
        client=client,
        expand=expand,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    person_id_type: str = "GWID",
    person_id: str = "3",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "phones,emails",
) -> Optional[
    Union[
        Peoplepersonidtypepersonid1Response200,
        Peoplepersonidtypepersonid1Response403,
        Peoplepersonidtypepersonid1Response404,
    ]
]:
    """/people/{personIdType}:{personId}

     Retrieve a person record and associated contact information. For example `/people/DWID:12345` would
    retrieve a person whose DWID is 12345.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        expand (Union[Unset, None, str]):  Default: 'phones,emails'.

    Returns:
        Response[Union[Peoplepersonidtypepersonid1Response200, Peoplepersonidtypepersonid1Response403, Peoplepersonidtypepersonid1Response404]]
    """

    return sync_detailed(
        person_id_type=person_id_type,
        person_id=person_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    person_id_type: str = "GWID",
    person_id: str = "3",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "phones,emails",
) -> Response[
    Union[
        Peoplepersonidtypepersonid1Response200,
        Peoplepersonidtypepersonid1Response403,
        Peoplepersonidtypepersonid1Response404,
    ]
]:
    """/people/{personIdType}:{personId}

     Retrieve a person record and associated contact information. For example `/people/DWID:12345` would
    retrieve a person whose DWID is 12345.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        expand (Union[Unset, None, str]):  Default: 'phones,emails'.

    Returns:
        Response[Union[Peoplepersonidtypepersonid1Response200, Peoplepersonidtypepersonid1Response403, Peoplepersonidtypepersonid1Response404]]
    """

    kwargs = _get_kwargs(
        person_id_type=person_id_type,
        person_id=person_id,
        client=client,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    person_id_type: str = "GWID",
    person_id: str = "3",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "phones,emails",
) -> Optional[
    Union[
        Peoplepersonidtypepersonid1Response200,
        Peoplepersonidtypepersonid1Response403,
        Peoplepersonidtypepersonid1Response404,
    ]
]:
    """/people/{personIdType}:{personId}

     Retrieve a person record and associated contact information. For example `/people/DWID:12345` would
    retrieve a person whose DWID is 12345.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        expand (Union[Unset, None, str]):  Default: 'phones,emails'.

    Returns:
        Response[Union[Peoplepersonidtypepersonid1Response200, Peoplepersonidtypepersonid1Response403, Peoplepersonidtypepersonid1Response404]]
    """

    return (
        await asyncio_detailed(
            person_id_type=person_id_type,
            person_id=person_id,
            client=client,
            expand=expand,
        )
    ).parsed
