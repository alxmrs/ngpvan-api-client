import datetime
from typing import Any, Dict, Optional, Union

import httpx
from dateutil.parser import isoparse

from ...client import Client
from ...models.printedlists_response_200 import PrintedlistsResponse200
from ...models.printedlists_response_400 import PrintedlistsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2019-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2019-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    folder_name: Union[Unset, None, str] = "GOTV",
    turf_name: Union[Unset, None, str] = "Precinct+1",
    top: Union[Unset, None, int] = 15,
) -> Dict[str, Any]:
    url = "{}/printedLists".format(client.base_url)

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

    params["folderName"] = folder_name

    params["turfName"] = turf_name

    params["$top"] = top

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[PrintedlistsResponse200, PrintedlistsResponse400]]:
    if response.status_code == 200:
        response_200 = PrintedlistsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PrintedlistsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[PrintedlistsResponse200, PrintedlistsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2019-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2019-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    folder_name: Union[Unset, None, str] = "GOTV",
    turf_name: Union[Unset, None, str] = "Precinct+1",
    top: Union[Unset, None, int] = 15,
) -> Response[Union[PrintedlistsResponse200, PrintedlistsResponse400]]:
    """/printedLists

     Use this endpoint to retrieve all available Printed Lists

    Args:
        generated_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-10-01').date().
        generated_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-11-01').date().
        created_by (Union[Unset, None, int]):  Default: 123.
        folder_name (Union[Unset, None, str]):  Default: 'GOTV'.
        turf_name (Union[Unset, None, str]):  Default: 'Precinct+1'.
        top (Union[Unset, None, int]):  Default: 15.

    Returns:
        Response[Union[PrintedlistsResponse200, PrintedlistsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        generated_after=generated_after,
        generated_before=generated_before,
        created_by=created_by,
        folder_name=folder_name,
        turf_name=turf_name,
        top=top,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2019-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2019-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    folder_name: Union[Unset, None, str] = "GOTV",
    turf_name: Union[Unset, None, str] = "Precinct+1",
    top: Union[Unset, None, int] = 15,
) -> Optional[Union[PrintedlistsResponse200, PrintedlistsResponse400]]:
    """/printedLists

     Use this endpoint to retrieve all available Printed Lists

    Args:
        generated_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-10-01').date().
        generated_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-11-01').date().
        created_by (Union[Unset, None, int]):  Default: 123.
        folder_name (Union[Unset, None, str]):  Default: 'GOTV'.
        turf_name (Union[Unset, None, str]):  Default: 'Precinct+1'.
        top (Union[Unset, None, int]):  Default: 15.

    Returns:
        Response[Union[PrintedlistsResponse200, PrintedlistsResponse400]]
    """

    return sync_detailed(
        client=client,
        generated_after=generated_after,
        generated_before=generated_before,
        created_by=created_by,
        folder_name=folder_name,
        turf_name=turf_name,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2019-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2019-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    folder_name: Union[Unset, None, str] = "GOTV",
    turf_name: Union[Unset, None, str] = "Precinct+1",
    top: Union[Unset, None, int] = 15,
) -> Response[Union[PrintedlistsResponse200, PrintedlistsResponse400]]:
    """/printedLists

     Use this endpoint to retrieve all available Printed Lists

    Args:
        generated_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-10-01').date().
        generated_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-11-01').date().
        created_by (Union[Unset, None, int]):  Default: 123.
        folder_name (Union[Unset, None, str]):  Default: 'GOTV'.
        turf_name (Union[Unset, None, str]):  Default: 'Precinct+1'.
        top (Union[Unset, None, int]):  Default: 15.

    Returns:
        Response[Union[PrintedlistsResponse200, PrintedlistsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        generated_after=generated_after,
        generated_before=generated_before,
        created_by=created_by,
        folder_name=folder_name,
        turf_name=turf_name,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    generated_after: Union[Unset, None, datetime.date] = isoparse("2019-10-01").date(),
    generated_before: Union[Unset, None, datetime.date] = isoparse("2019-11-01").date(),
    created_by: Union[Unset, None, int] = 123,
    folder_name: Union[Unset, None, str] = "GOTV",
    turf_name: Union[Unset, None, str] = "Precinct+1",
    top: Union[Unset, None, int] = 15,
) -> Optional[Union[PrintedlistsResponse200, PrintedlistsResponse400]]:
    """/printedLists

     Use this endpoint to retrieve all available Printed Lists

    Args:
        generated_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-10-01').date().
        generated_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-11-01').date().
        created_by (Union[Unset, None, int]):  Default: 123.
        folder_name (Union[Unset, None, str]):  Default: 'GOTV'.
        turf_name (Union[Unset, None, str]):  Default: 'Precinct+1'.
        top (Union[Unset, None, int]):  Default: 15.

    Returns:
        Response[Union[PrintedlistsResponse200, PrintedlistsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            generated_after=generated_after,
            generated_before=generated_before,
            created_by=created_by,
            folder_name=folder_name,
            turf_name=turf_name,
            top=top,
        )
    ).parsed
