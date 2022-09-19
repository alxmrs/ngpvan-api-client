import datetime
from typing import Any, Dict, Optional, Union

import httpx
from dateutil.parser import isoparse

from ...client import Client
from ...models.voterregistrationbatches_program_type import VoterregistrationbatchesProgramType
from ...models.voterregistrationbatches_response_200 import VoterregistrationbatchesResponse200
from ...models.voterregistrationbatches_response_400 import VoterregistrationbatchesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2019-08-01").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2020-08-01").date(),
    status: Union[Unset, None, str] = "Entering",
    state_code: Union[Unset, None, str] = "MA",
    only_my_batches: Union[Unset, None, bool] = False,
    program_type: Union[Unset, None, VoterregistrationbatchesProgramType] = UNSET,
    person_type: Union[Unset, None, str] = "Applicant",
    orderby: Union[Unset, None, str] = "DateCreated desc",
    top: Union[Unset, None, int] = 1,
    skip: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/voterRegistrationBatches".format(client.base_url)

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

    params["status"] = status

    params["stateCode"] = state_code

    params["onlyMyBatches"] = only_my_batches

    json_program_type: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(program_type, Unset):
        json_program_type = program_type.to_dict() if program_type else None

    if not isinstance(json_program_type, Unset) and json_program_type is not None:
        params.update(json_program_type)

    params["personType"] = person_type

    params["$orderby"] = orderby

    params["$top"] = top

    params["$skip"] = skip

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
) -> Optional[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]:
    if response.status_code == 200:
        response_200 = VoterregistrationbatchesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = VoterregistrationbatchesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2019-08-01").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2020-08-01").date(),
    status: Union[Unset, None, str] = "Entering",
    state_code: Union[Unset, None, str] = "MA",
    only_my_batches: Union[Unset, None, bool] = False,
    program_type: Union[Unset, None, VoterregistrationbatchesProgramType] = UNSET,
    person_type: Union[Unset, None, str] = "Applicant",
    orderby: Union[Unset, None, str] = "DateCreated desc",
    top: Union[Unset, None, int] = 1,
    skip: Union[Unset, None, int] = 0,
) -> Response[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]:
    """/voterRegistrationBatches

     Search for voter registration batches, with required filtering.

    Args:
        created_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-08-01').date().
        created_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2020-08-01').date().
        status (Union[Unset, None, str]):  Default: 'Entering'.
        state_code (Union[Unset, None, str]):  Default: 'MA'.
        only_my_batches (Union[Unset, None, bool]):
        program_type (Union[Unset, None, VoterregistrationbatchesProgramType]):
        person_type (Union[Unset, None, str]):  Default: 'Applicant'.
        orderby (Union[Unset, None, str]):  Default: 'DateCreated desc'.
        top (Union[Unset, None, int]):  Default: 1.
        skip (Union[Unset, None, int]):

    Returns:
        Response[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        created_before=created_before,
        created_after=created_after,
        status=status,
        state_code=state_code,
        only_my_batches=only_my_batches,
        program_type=program_type,
        person_type=person_type,
        orderby=orderby,
        top=top,
        skip=skip,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2019-08-01").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2020-08-01").date(),
    status: Union[Unset, None, str] = "Entering",
    state_code: Union[Unset, None, str] = "MA",
    only_my_batches: Union[Unset, None, bool] = False,
    program_type: Union[Unset, None, VoterregistrationbatchesProgramType] = UNSET,
    person_type: Union[Unset, None, str] = "Applicant",
    orderby: Union[Unset, None, str] = "DateCreated desc",
    top: Union[Unset, None, int] = 1,
    skip: Union[Unset, None, int] = 0,
) -> Optional[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]:
    """/voterRegistrationBatches

     Search for voter registration batches, with required filtering.

    Args:
        created_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-08-01').date().
        created_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2020-08-01').date().
        status (Union[Unset, None, str]):  Default: 'Entering'.
        state_code (Union[Unset, None, str]):  Default: 'MA'.
        only_my_batches (Union[Unset, None, bool]):
        program_type (Union[Unset, None, VoterregistrationbatchesProgramType]):
        person_type (Union[Unset, None, str]):  Default: 'Applicant'.
        orderby (Union[Unset, None, str]):  Default: 'DateCreated desc'.
        top (Union[Unset, None, int]):  Default: 1.
        skip (Union[Unset, None, int]):

    Returns:
        Response[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]
    """

    return sync_detailed(
        client=client,
        created_before=created_before,
        created_after=created_after,
        status=status,
        state_code=state_code,
        only_my_batches=only_my_batches,
        program_type=program_type,
        person_type=person_type,
        orderby=orderby,
        top=top,
        skip=skip,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2019-08-01").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2020-08-01").date(),
    status: Union[Unset, None, str] = "Entering",
    state_code: Union[Unset, None, str] = "MA",
    only_my_batches: Union[Unset, None, bool] = False,
    program_type: Union[Unset, None, VoterregistrationbatchesProgramType] = UNSET,
    person_type: Union[Unset, None, str] = "Applicant",
    orderby: Union[Unset, None, str] = "DateCreated desc",
    top: Union[Unset, None, int] = 1,
    skip: Union[Unset, None, int] = 0,
) -> Response[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]:
    """/voterRegistrationBatches

     Search for voter registration batches, with required filtering.

    Args:
        created_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-08-01').date().
        created_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2020-08-01').date().
        status (Union[Unset, None, str]):  Default: 'Entering'.
        state_code (Union[Unset, None, str]):  Default: 'MA'.
        only_my_batches (Union[Unset, None, bool]):
        program_type (Union[Unset, None, VoterregistrationbatchesProgramType]):
        person_type (Union[Unset, None, str]):  Default: 'Applicant'.
        orderby (Union[Unset, None, str]):  Default: 'DateCreated desc'.
        top (Union[Unset, None, int]):  Default: 1.
        skip (Union[Unset, None, int]):

    Returns:
        Response[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        created_before=created_before,
        created_after=created_after,
        status=status,
        state_code=state_code,
        only_my_batches=only_my_batches,
        program_type=program_type,
        person_type=person_type,
        orderby=orderby,
        top=top,
        skip=skip,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    created_before: Union[Unset, None, datetime.date] = isoparse("2019-08-01").date(),
    created_after: Union[Unset, None, datetime.date] = isoparse("2020-08-01").date(),
    status: Union[Unset, None, str] = "Entering",
    state_code: Union[Unset, None, str] = "MA",
    only_my_batches: Union[Unset, None, bool] = False,
    program_type: Union[Unset, None, VoterregistrationbatchesProgramType] = UNSET,
    person_type: Union[Unset, None, str] = "Applicant",
    orderby: Union[Unset, None, str] = "DateCreated desc",
    top: Union[Unset, None, int] = 1,
    skip: Union[Unset, None, int] = 0,
) -> Optional[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]:
    """/voterRegistrationBatches

     Search for voter registration batches, with required filtering.

    Args:
        created_before (Union[Unset, None, datetime.date]):  Default:
            isoparse('2019-08-01').date().
        created_after (Union[Unset, None, datetime.date]):  Default:
            isoparse('2020-08-01').date().
        status (Union[Unset, None, str]):  Default: 'Entering'.
        state_code (Union[Unset, None, str]):  Default: 'MA'.
        only_my_batches (Union[Unset, None, bool]):
        program_type (Union[Unset, None, VoterregistrationbatchesProgramType]):
        person_type (Union[Unset, None, str]):  Default: 'Applicant'.
        orderby (Union[Unset, None, str]):  Default: 'DateCreated desc'.
        top (Union[Unset, None, int]):  Default: 1.
        skip (Union[Unset, None, int]):

    Returns:
        Response[Union[VoterregistrationbatchesResponse200, VoterregistrationbatchesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_before=created_before,
            created_after=created_after,
            status=status,
            state_code=state_code,
            only_my_batches=only_my_batches,
            program_type=program_type,
            person_type=person_type,
            orderby=orderby,
            top=top,
            skip=skip,
        )
    ).parsed
