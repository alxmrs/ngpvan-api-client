import datetime
from typing import Any, Dict, Optional, Union

import httpx
from dateutil.parser import isoparse

from ...client import Client
from ...models.events_1_response_200 import Events1Response200
from ...models.events_1_response_400 import Events1Response400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    code_ids: Union[Unset, None, str] = "20513,20515",
    event_type_ids: Union[Unset, None, str] = "20036,81987",
    in_repetition_with_event_id: Union[Unset, None, int] = 1374,
    starting_after: Union[Unset, None, datetime.date] = isoparse("2019-06-23").date(),
    starting_before: Union[Unset, None, datetime.date] = isoparse("2019-06-26").date(),
    district_field_value: Union[Unset, None, str] = "003",
    created_by_committee_id: Union[Unset, None, int] = 123,
    expand: Union[Unset, None, str] = "locations,codes",
    top: Union[Unset, None, int] = 10,
) -> Dict[str, Any]:
    url = "{}/events".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["codeIds"] = code_ids

    params["eventTypeIds"] = event_type_ids

    params["inRepetitionWithEventId"] = in_repetition_with_event_id

    json_starting_after: Union[Unset, None, str] = UNSET
    if not isinstance(starting_after, Unset):
        json_starting_after = starting_after.isoformat() if starting_after else None

    params["startingAfter"] = json_starting_after

    json_starting_before: Union[Unset, None, str] = UNSET
    if not isinstance(starting_before, Unset):
        json_starting_before = starting_before.isoformat() if starting_before else None

    params["startingBefore"] = json_starting_before

    params["districtFieldValue"] = district_field_value

    params["createdByCommitteeId"] = created_by_committee_id

    params["$expand"] = expand

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Events1Response200, Events1Response400]]:
    if response.status_code == 200:
        response_200 = Events1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Events1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Events1Response200, Events1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    code_ids: Union[Unset, None, str] = "20513,20515",
    event_type_ids: Union[Unset, None, str] = "20036,81987",
    in_repetition_with_event_id: Union[Unset, None, int] = 1374,
    starting_after: Union[Unset, None, datetime.date] = isoparse("2019-06-23").date(),
    starting_before: Union[Unset, None, datetime.date] = isoparse("2019-06-26").date(),
    district_field_value: Union[Unset, None, str] = "003",
    created_by_committee_id: Union[Unset, None, int] = 123,
    expand: Union[Unset, None, str] = "locations,codes",
    top: Union[Unset, None, int] = 10,
) -> Response[Union[Events1Response200, Events1Response400]]:
    """/events

     Find Events

    *Description*

    Use this endpoint to find Events available in the current context using a number of filter options.

    *Request*

    This endpoint accepts [standard pagination
    parameters](https://everyaction.readme.io/reference#pagination) and returns a standard paginated
    response.

    By default, this endpoint returns 10 records per request. A maximum of 50 records per request is
    allowed via the `$top` parameter.

    Valid [expansion](https://everyaction.readme.io/reference#expansion) properties are: `locations`,
    `codes`, `shifts`, `roles`, `notes`. Note that the number of `$expand` sections requested may impact
    the speed with which this endpoint will respond.

    The endpoint takes the optional filter parameters as described below

    Args:
        code_ids (Union[Unset, None, str]):  Default: '20513,20515'.
        event_type_ids (Union[Unset, None, str]):  Default: '20036,81987'.
        in_repetition_with_event_id (Union[Unset, None, int]):  Default: 1374.
        starting_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-06-23').date().
        starting_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-06-26').date().
        district_field_value (Union[Unset, None, str]):  Default: '003'.
        created_by_committee_id (Union[Unset, None, int]):  Default: 123.
        expand (Union[Unset, None, str]):  Default: 'locations,codes'.
        top (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[Events1Response200, Events1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        code_ids=code_ids,
        event_type_ids=event_type_ids,
        in_repetition_with_event_id=in_repetition_with_event_id,
        starting_after=starting_after,
        starting_before=starting_before,
        district_field_value=district_field_value,
        created_by_committee_id=created_by_committee_id,
        expand=expand,
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
    code_ids: Union[Unset, None, str] = "20513,20515",
    event_type_ids: Union[Unset, None, str] = "20036,81987",
    in_repetition_with_event_id: Union[Unset, None, int] = 1374,
    starting_after: Union[Unset, None, datetime.date] = isoparse("2019-06-23").date(),
    starting_before: Union[Unset, None, datetime.date] = isoparse("2019-06-26").date(),
    district_field_value: Union[Unset, None, str] = "003",
    created_by_committee_id: Union[Unset, None, int] = 123,
    expand: Union[Unset, None, str] = "locations,codes",
    top: Union[Unset, None, int] = 10,
) -> Optional[Union[Events1Response200, Events1Response400]]:
    """/events

     Find Events

    *Description*

    Use this endpoint to find Events available in the current context using a number of filter options.

    *Request*

    This endpoint accepts [standard pagination
    parameters](https://everyaction.readme.io/reference#pagination) and returns a standard paginated
    response.

    By default, this endpoint returns 10 records per request. A maximum of 50 records per request is
    allowed via the `$top` parameter.

    Valid [expansion](https://everyaction.readme.io/reference#expansion) properties are: `locations`,
    `codes`, `shifts`, `roles`, `notes`. Note that the number of `$expand` sections requested may impact
    the speed with which this endpoint will respond.

    The endpoint takes the optional filter parameters as described below

    Args:
        code_ids (Union[Unset, None, str]):  Default: '20513,20515'.
        event_type_ids (Union[Unset, None, str]):  Default: '20036,81987'.
        in_repetition_with_event_id (Union[Unset, None, int]):  Default: 1374.
        starting_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-06-23').date().
        starting_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-06-26').date().
        district_field_value (Union[Unset, None, str]):  Default: '003'.
        created_by_committee_id (Union[Unset, None, int]):  Default: 123.
        expand (Union[Unset, None, str]):  Default: 'locations,codes'.
        top (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[Events1Response200, Events1Response400]]
    """

    return sync_detailed(
        client=client,
        code_ids=code_ids,
        event_type_ids=event_type_ids,
        in_repetition_with_event_id=in_repetition_with_event_id,
        starting_after=starting_after,
        starting_before=starting_before,
        district_field_value=district_field_value,
        created_by_committee_id=created_by_committee_id,
        expand=expand,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    code_ids: Union[Unset, None, str] = "20513,20515",
    event_type_ids: Union[Unset, None, str] = "20036,81987",
    in_repetition_with_event_id: Union[Unset, None, int] = 1374,
    starting_after: Union[Unset, None, datetime.date] = isoparse("2019-06-23").date(),
    starting_before: Union[Unset, None, datetime.date] = isoparse("2019-06-26").date(),
    district_field_value: Union[Unset, None, str] = "003",
    created_by_committee_id: Union[Unset, None, int] = 123,
    expand: Union[Unset, None, str] = "locations,codes",
    top: Union[Unset, None, int] = 10,
) -> Response[Union[Events1Response200, Events1Response400]]:
    """/events

     Find Events

    *Description*

    Use this endpoint to find Events available in the current context using a number of filter options.

    *Request*

    This endpoint accepts [standard pagination
    parameters](https://everyaction.readme.io/reference#pagination) and returns a standard paginated
    response.

    By default, this endpoint returns 10 records per request. A maximum of 50 records per request is
    allowed via the `$top` parameter.

    Valid [expansion](https://everyaction.readme.io/reference#expansion) properties are: `locations`,
    `codes`, `shifts`, `roles`, `notes`. Note that the number of `$expand` sections requested may impact
    the speed with which this endpoint will respond.

    The endpoint takes the optional filter parameters as described below

    Args:
        code_ids (Union[Unset, None, str]):  Default: '20513,20515'.
        event_type_ids (Union[Unset, None, str]):  Default: '20036,81987'.
        in_repetition_with_event_id (Union[Unset, None, int]):  Default: 1374.
        starting_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-06-23').date().
        starting_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-06-26').date().
        district_field_value (Union[Unset, None, str]):  Default: '003'.
        created_by_committee_id (Union[Unset, None, int]):  Default: 123.
        expand (Union[Unset, None, str]):  Default: 'locations,codes'.
        top (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[Events1Response200, Events1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        code_ids=code_ids,
        event_type_ids=event_type_ids,
        in_repetition_with_event_id=in_repetition_with_event_id,
        starting_after=starting_after,
        starting_before=starting_before,
        district_field_value=district_field_value,
        created_by_committee_id=created_by_committee_id,
        expand=expand,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    code_ids: Union[Unset, None, str] = "20513,20515",
    event_type_ids: Union[Unset, None, str] = "20036,81987",
    in_repetition_with_event_id: Union[Unset, None, int] = 1374,
    starting_after: Union[Unset, None, datetime.date] = isoparse("2019-06-23").date(),
    starting_before: Union[Unset, None, datetime.date] = isoparse("2019-06-26").date(),
    district_field_value: Union[Unset, None, str] = "003",
    created_by_committee_id: Union[Unset, None, int] = 123,
    expand: Union[Unset, None, str] = "locations,codes",
    top: Union[Unset, None, int] = 10,
) -> Optional[Union[Events1Response200, Events1Response400]]:
    """/events

     Find Events

    *Description*

    Use this endpoint to find Events available in the current context using a number of filter options.

    *Request*

    This endpoint accepts [standard pagination
    parameters](https://everyaction.readme.io/reference#pagination) and returns a standard paginated
    response.

    By default, this endpoint returns 10 records per request. A maximum of 50 records per request is
    allowed via the `$top` parameter.

    Valid [expansion](https://everyaction.readme.io/reference#expansion) properties are: `locations`,
    `codes`, `shifts`, `roles`, `notes`. Note that the number of `$expand` sections requested may impact
    the speed with which this endpoint will respond.

    The endpoint takes the optional filter parameters as described below

    Args:
        code_ids (Union[Unset, None, str]):  Default: '20513,20515'.
        event_type_ids (Union[Unset, None, str]):  Default: '20036,81987'.
        in_repetition_with_event_id (Union[Unset, None, int]):  Default: 1374.
        starting_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-06-23').date().
        starting_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-06-26').date().
        district_field_value (Union[Unset, None, str]):  Default: '003'.
        created_by_committee_id (Union[Unset, None, int]):  Default: 123.
        expand (Union[Unset, None, str]):  Default: 'locations,codes'.
        top (Union[Unset, None, int]):  Default: 10.

    Returns:
        Response[Union[Events1Response200, Events1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            code_ids=code_ids,
            event_type_ids=event_type_ids,
            in_repetition_with_event_id=in_repetition_with_event_id,
            starting_after=starting_after,
            starting_before=starting_before,
            district_field_value=district_field_value,
            created_by_committee_id=created_by_committee_id,
            expand=expand,
            top=top,
        )
    ).parsed
