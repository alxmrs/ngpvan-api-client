import datetime
from typing import Any, Dict, Optional, Union, cast

import httpx
from dateutil.parser import isoparse

from ...client import Client
from ...models.scoreupdates_response_400 import ScoreupdatesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2021-12-31").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2021-01-01").date(),
    score_id: Union[Unset, None, int] = 999,
) -> Dict[str, Any]:
    url = "{}/scoreUpdates".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_created_before: Union[Unset, None, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat() if created_before else None

    params["createdBefore"] = json_created_before

    json_created_after: Union[Unset, None, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat() if created_after else None

    params["createdAfter"] = json_created_after

    params["scoreId"] = score_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ScoreupdatesResponse400]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = ScoreupdatesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ScoreupdatesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2021-12-31").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2021-01-01").date(),
    score_id: Union[Unset, None, int] = 999,
) -> Response[Union[Any, ScoreupdatesResponse400]]:
    """/scoreUpdates

     Get all available Score Updates, optionally filtered by search parameters.

    Args:
        created_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2021-12-31').date().
        created_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2021-01-01').date().
        score_id (Union[Unset, None, int]):  Default: 999.

    Returns:
        Response[Union[Any, ScoreupdatesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        created_before=created_before,
        created_after=created_after,
        score_id=score_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2021-12-31").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2021-01-01").date(),
    score_id: Union[Unset, None, int] = 999,
) -> Optional[Union[Any, ScoreupdatesResponse400]]:
    """/scoreUpdates

     Get all available Score Updates, optionally filtered by search parameters.

    Args:
        created_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2021-12-31').date().
        created_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2021-01-01').date().
        score_id (Union[Unset, None, int]):  Default: 999.

    Returns:
        Response[Union[Any, ScoreupdatesResponse400]]
    """

    return sync_detailed(
        client=client,
        created_before=created_before,
        created_after=created_after,
        score_id=score_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2021-12-31").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2021-01-01").date(),
    score_id: Union[Unset, None, int] = 999,
) -> Response[Union[Any, ScoreupdatesResponse400]]:
    """/scoreUpdates

     Get all available Score Updates, optionally filtered by search parameters.

    Args:
        created_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2021-12-31').date().
        created_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2021-01-01').date().
        score_id (Union[Unset, None, int]):  Default: 999.

    Returns:
        Response[Union[Any, ScoreupdatesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        created_before=created_before,
        created_after=created_after,
        score_id=score_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2021-12-31").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2021-01-01").date(),
    score_id: Union[Unset, None, int] = 999,
) -> Optional[Union[Any, ScoreupdatesResponse400]]:
    """/scoreUpdates

     Get all available Score Updates, optionally filtered by search parameters.

    Args:
        created_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2021-12-31').date().
        created_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2021-01-01').date().
        score_id (Union[Unset, None, int]):  Default: 999.

    Returns:
        Response[Union[Any, ScoreupdatesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_before=created_before,
            created_after=created_after,
            score_id=score_id,
        )
    ).parsed
