import datetime
from typing import Any, Dict, Optional, Union

import httpx
from dateutil.parser import isoparse

from ...client import Client
from ...models.minivanexports_response_200 import MinivanexportsResponse200
from ...models.minivanexports_response_400 import MinivanexportsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2018-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2018-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    name: Union[Unset, None, str] = "GOTV",
    expand: Union[Unset, None, str] = "canvassers",
) -> Dict[str, Any]:
    url = "{}/minivanExports".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_generated_after: Union[Unset, None, str] = UNSET
    if not isinstance(generated_after, Unset):
        json_generated_after = generated_after.isoformat() if generated_after else None

    params["generatedAfter"] = json_generated_after

    json_generated_before: Union[Unset, None, str] = UNSET
    if not isinstance(generated_before, Unset):
        json_generated_before = generated_before.isoformat() if generated_before else None

    params["generatedBefore"] = json_generated_before

    params["createdBy"] = created_by

    params["name"] = name

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
) -> Optional[Union[MinivanexportsResponse200, MinivanexportsResponse400]]:
    if response.status_code == 200:
        response_200 = MinivanexportsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = MinivanexportsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[MinivanexportsResponse200, MinivanexportsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2018-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2018-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    name: Union[Unset, None, str] = "GOTV",
    expand: Union[Unset, None, str] = "canvassers",
) -> Response[Union[MinivanexportsResponse200, MinivanexportsResponse400]]:
    """/minivanExports

     Use this endpoint to retrieve all available MiniVAN Exports.

    Args:
        generated_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2018-10-01').date().
        generated_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2018-11-01').date().
        created_by (Union[Unset, None, int]):  Default: 123.
        name (Union[Unset, None, str]):  Default: 'GOTV'.
        expand (Union[Unset, None, str]):  Default: 'canvassers'.

    Returns:
        Response[Union[MinivanexportsResponse200, MinivanexportsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        generated_after=generated_after,
        generated_before=generated_before,
        created_by=created_by,
        name=name,
        expand=expand,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2018-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2018-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    name: Union[Unset, None, str] = "GOTV",
    expand: Union[Unset, None, str] = "canvassers",
) -> Optional[Union[MinivanexportsResponse200, MinivanexportsResponse400]]:
    """/minivanExports

     Use this endpoint to retrieve all available MiniVAN Exports.

    Args:
        generated_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2018-10-01').date().
        generated_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2018-11-01').date().
        created_by (Union[Unset, None, int]):  Default: 123.
        name (Union[Unset, None, str]):  Default: 'GOTV'.
        expand (Union[Unset, None, str]):  Default: 'canvassers'.

    Returns:
        Response[Union[MinivanexportsResponse200, MinivanexportsResponse400]]
    """

    return sync_detailed(
        client=client,
        generated_after=generated_after,
        generated_before=generated_before,
        created_by=created_by,
        name=name,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2018-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2018-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    name: Union[Unset, None, str] = "GOTV",
    expand: Union[Unset, None, str] = "canvassers",
) -> Response[Union[MinivanexportsResponse200, MinivanexportsResponse400]]:
    """/minivanExports

     Use this endpoint to retrieve all available MiniVAN Exports.

    Args:
        generated_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2018-10-01').date().
        generated_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2018-11-01').date().
        created_by (Union[Unset, None, int]):  Default: 123.
        name (Union[Unset, None, str]):  Default: 'GOTV'.
        expand (Union[Unset, None, str]):  Default: 'canvassers'.

    Returns:
        Response[Union[MinivanexportsResponse200, MinivanexportsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        generated_after=generated_after,
        generated_before=generated_before,
        created_by=created_by,
        name=name,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2018-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2018-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    name: Union[Unset, None, str] = "GOTV",
    expand: Union[Unset, None, str] = "canvassers",
) -> Optional[Union[MinivanexportsResponse200, MinivanexportsResponse400]]:
    """/minivanExports

     Use this endpoint to retrieve all available MiniVAN Exports.

    Args:
        generated_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2018-10-01').date().
        generated_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2018-11-01').date().
        created_by (Union[Unset, None, int]):  Default: 123.
        name (Union[Unset, None, str]):  Default: 'GOTV'.
        expand (Union[Unset, None, str]):  Default: 'canvassers'.

    Returns:
        Response[Union[MinivanexportsResponse200, MinivanexportsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            generated_after=generated_after,
            generated_before=generated_before,
            created_by=created_by,
            name=name,
            expand=expand,
        )
    ).parsed
