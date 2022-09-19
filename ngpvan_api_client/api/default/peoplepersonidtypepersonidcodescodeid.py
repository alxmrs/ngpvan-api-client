from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.peoplepersonidtypepersonidcodescodeid_response_400 import (
    PeoplepersonidtypepersonidcodescodeidResponse400,
)
from ...models.peoplepersonidtypepersonidcodescodeid_response_404 import (
    PeoplepersonidtypepersonidcodescodeidResponse404,
)
from ...types import Response


def _get_kwargs(
    person_id_type: str = "GWID",
    person_id: str = "3",
    code_id: str = "20545",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/people/{personIdType}:{personId}/codes/{codeId}".format(
        client.base_url, personIdType=person_id_type, personId=person_id, codeId=code_id
    )

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
) -> Optional[
    Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]
]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = PeoplepersonidtypepersonidcodescodeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = PeoplepersonidtypepersonidcodescodeidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]
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
    code_id: str = "20545",
    *,
    client: Client,
) -> Response[
    Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]
]:
    """/people/{personIdType}:{personId}/codes/{codeId}

     Use this endpoint to remove a single [Code](ref:codes) from a Person identified by a case-
    insensitive external ID.

    This endpoint is the same as
    [DELETE/people/{vanId}/codes/{codeId}](ref:people#peoplevanidcodescodeid) but uses external IDs
    rather than VANIDs.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        code_id (str):  Default: '20545'.

    Returns:
        Response[Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]]
    """

    kwargs = _get_kwargs(
        person_id_type=person_id_type,
        person_id=person_id,
        code_id=code_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    person_id_type: str = "GWID",
    person_id: str = "3",
    code_id: str = "20545",
    *,
    client: Client,
) -> Optional[
    Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]
]:
    """/people/{personIdType}:{personId}/codes/{codeId}

     Use this endpoint to remove a single [Code](ref:codes) from a Person identified by a case-
    insensitive external ID.

    This endpoint is the same as
    [DELETE/people/{vanId}/codes/{codeId}](ref:people#peoplevanidcodescodeid) but uses external IDs
    rather than VANIDs.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        code_id (str):  Default: '20545'.

    Returns:
        Response[Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]]
    """

    return sync_detailed(
        person_id_type=person_id_type,
        person_id=person_id,
        code_id=code_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id_type: str = "GWID",
    person_id: str = "3",
    code_id: str = "20545",
    *,
    client: Client,
) -> Response[
    Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]
]:
    """/people/{personIdType}:{personId}/codes/{codeId}

     Use this endpoint to remove a single [Code](ref:codes) from a Person identified by a case-
    insensitive external ID.

    This endpoint is the same as
    [DELETE/people/{vanId}/codes/{codeId}](ref:people#peoplevanidcodescodeid) but uses external IDs
    rather than VANIDs.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        code_id (str):  Default: '20545'.

    Returns:
        Response[Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]]
    """

    kwargs = _get_kwargs(
        person_id_type=person_id_type,
        person_id=person_id,
        code_id=code_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    person_id_type: str = "GWID",
    person_id: str = "3",
    code_id: str = "20545",
    *,
    client: Client,
) -> Optional[
    Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]
]:
    """/people/{personIdType}:{personId}/codes/{codeId}

     Use this endpoint to remove a single [Code](ref:codes) from a Person identified by a case-
    insensitive external ID.

    This endpoint is the same as
    [DELETE/people/{vanId}/codes/{codeId}](ref:people#peoplevanidcodescodeid) but uses external IDs
    rather than VANIDs.

    Args:
        person_id_type (str):  Default: 'GWID'.
        person_id (str):  Default: '3'.
        code_id (str):  Default: '20545'.

    Returns:
        Response[Union[Any, PeoplepersonidtypepersonidcodescodeidResponse400, PeoplepersonidtypepersonidcodescodeidResponse404]]
    """

    return (
        await asyncio_detailed(
            person_id_type=person_id_type,
            person_id=person_id,
            code_id=code_id,
            client=client,
        )
    ).parsed
