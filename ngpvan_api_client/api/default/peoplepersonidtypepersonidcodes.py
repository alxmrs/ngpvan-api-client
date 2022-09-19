from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplepersonidtypepersonidcodes_json_body import PeoplepersonidtypepersonidcodesJsonBody
from ...models.peoplepersonidtypepersonidcodes_response_400 import PeoplepersonidtypepersonidcodesResponse400
from ...models.peoplepersonidtypepersonidcodes_response_404 import PeoplepersonidtypepersonidcodesResponse404
from ...types import Response


def _get_kwargs(
    person_id_type: str = "GWID",
    person_id: str = "3",
    *,
    client: Client,
    json_body: PeoplepersonidtypepersonidcodesJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/{personIdType}:{personId}/codes".format(
        client.base_url, personIdType=person_id_type, personId=person_id
    )

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
) -> Optional[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PeoplepersonidtypepersonidcodesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = PeoplepersonidtypepersonidcodesResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]:
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
    json_body: PeoplepersonidtypepersonidcodesJsonBody,
) -> Response[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]:
    """/people/{personIdType}:{personId}/codes

     This endpoint is the same as [POST /people/{vanId}/codes](ref:people#peoplevanidcodes) but uses
    external IDs rather than VANIDs.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        json_body (PeoplepersonidtypepersonidcodesJsonBody):

    Returns:
        Response[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]
    """

    kwargs = _get_kwargs(
        person_id_type=person_id_type,
        person_id=person_id,
        client=client,
        json_body=json_body,
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
    json_body: PeoplepersonidtypepersonidcodesJsonBody,
) -> Optional[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]:
    """/people/{personIdType}:{personId}/codes

     This endpoint is the same as [POST /people/{vanId}/codes](ref:people#peoplevanidcodes) but uses
    external IDs rather than VANIDs.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        json_body (PeoplepersonidtypepersonidcodesJsonBody):

    Returns:
        Response[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]
    """

    return sync_detailed(
        person_id_type=person_id_type,
        person_id=person_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    person_id_type: str = "GWID",
    person_id: str = "3",
    *,
    client: Client,
    json_body: PeoplepersonidtypepersonidcodesJsonBody,
) -> Response[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]:
    """/people/{personIdType}:{personId}/codes

     This endpoint is the same as [POST /people/{vanId}/codes](ref:people#peoplevanidcodes) but uses
    external IDs rather than VANIDs.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        json_body (PeoplepersonidtypepersonidcodesJsonBody):

    Returns:
        Response[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]
    """

    kwargs = _get_kwargs(
        person_id_type=person_id_type,
        person_id=person_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    person_id_type: str = "GWID",
    person_id: str = "3",
    *,
    client: Client,
    json_body: PeoplepersonidtypepersonidcodesJsonBody,
) -> Optional[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]:
    """/people/{personIdType}:{personId}/codes

     This endpoint is the same as [POST /people/{vanId}/codes](ref:people#peoplevanidcodes) but uses
    external IDs rather than VANIDs.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        json_body (PeoplepersonidtypepersonidcodesJsonBody):

    Returns:
        Response[Union[Any, PeoplepersonidtypepersonidcodesResponse400, PeoplepersonidtypepersonidcodesResponse404]]
    """

    return (
        await asyncio_detailed(
            person_id_type=person_id_type,
            person_id=person_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
