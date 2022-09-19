from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.peoplevanidmergeinto_json_body import PeoplevanidmergeintoJsonBody
from ...models.peoplevanidmergeinto_response_200 import PeoplevanidmergeintoResponse200
from ...models.peoplevanidmergeinto_response_400 import PeoplevanidmergeintoResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidmergeintoJsonBody,
    what_if: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/people/{vanId}/mergeInto".format(client.base_url, vanId=van_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["whatIf"] = what_if

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]:
    if response.status_code == 200:
        response_200 = PeoplevanidmergeintoResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PeoplevanidmergeintoResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidmergeintoJsonBody,
    what_if: Union[Unset, None, bool] = UNSET,
) -> Response[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]:
    """/people/{vanId}/mergeInto

     Merges a Source contact record into a Target contact record, retaining the Target's information when
    Source and Target conflict.

    This API can be used to merge two contact records in your database.

    * The **Source** (or **Secondary**) contact is specified in the URL (`/people/{vanId}/mergeInto`);
    this record will be deleted as part of the merge
    * The **Target** (or **Primary**) contact is specified in the body of the request and survives the
    merge

    >❗️ Merges are permanent and **cannot** be undone. Use this endpoint with caution.

    Some fields may conflict between the two records and the merge process will not be able to retain
    both values (e.g., different first names). In this case, the API will retain the Target's
    information, which is the same behavior as the default selections in the Contacts Merge Wizard in
    the UI. Note that if you need to retain information from the Source, you can make a subsequent
    [/people/{vanId}](ref:peoplevanid) call to update the Target with the value(s) from the Source
    record you want to persist. All other fields where multiple values can be stored--such as emails,
    phones, and addresses--will be combined into the Target record.

    Not all records can be merged; if a record cannot be merged it will be treated as an [Input
    Validation](ref:input-validation) error with details provided in the `text` field of the error
    response. Though not exhaustive, some conditions that could prevent a merge are:

    * Both VANIDs need to exist and be accessible to you
    * Both records must have the same `contactMode`
    * If Disclosure Fields are enabled, the Source record cannot be linked to a Contribution or
    Disbursement

    To check if records can be merged without actually merging, you can specify `?whatIf=true` in the
    query string.

    Args:
        van_id (int):
        what_if (Union[Unset, None, bool]):
        json_body (PeoplevanidmergeintoJsonBody):

    Returns:
        Response[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
        json_body=json_body,
        what_if=what_if,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidmergeintoJsonBody,
    what_if: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]:
    """/people/{vanId}/mergeInto

     Merges a Source contact record into a Target contact record, retaining the Target's information when
    Source and Target conflict.

    This API can be used to merge two contact records in your database.

    * The **Source** (or **Secondary**) contact is specified in the URL (`/people/{vanId}/mergeInto`);
    this record will be deleted as part of the merge
    * The **Target** (or **Primary**) contact is specified in the body of the request and survives the
    merge

    >❗️ Merges are permanent and **cannot** be undone. Use this endpoint with caution.

    Some fields may conflict between the two records and the merge process will not be able to retain
    both values (e.g., different first names). In this case, the API will retain the Target's
    information, which is the same behavior as the default selections in the Contacts Merge Wizard in
    the UI. Note that if you need to retain information from the Source, you can make a subsequent
    [/people/{vanId}](ref:peoplevanid) call to update the Target with the value(s) from the Source
    record you want to persist. All other fields where multiple values can be stored--such as emails,
    phones, and addresses--will be combined into the Target record.

    Not all records can be merged; if a record cannot be merged it will be treated as an [Input
    Validation](ref:input-validation) error with details provided in the `text` field of the error
    response. Though not exhaustive, some conditions that could prevent a merge are:

    * Both VANIDs need to exist and be accessible to you
    * Both records must have the same `contactMode`
    * If Disclosure Fields are enabled, the Source record cannot be linked to a Contribution or
    Disbursement

    To check if records can be merged without actually merging, you can specify `?whatIf=true` in the
    query string.

    Args:
        van_id (int):
        what_if (Union[Unset, None, bool]):
        json_body (PeoplevanidmergeintoJsonBody):

    Returns:
        Response[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]
    """

    return sync_detailed(
        van_id=van_id,
        client=client,
        json_body=json_body,
        what_if=what_if,
    ).parsed


async def asyncio_detailed(
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidmergeintoJsonBody,
    what_if: Union[Unset, None, bool] = UNSET,
) -> Response[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]:
    """/people/{vanId}/mergeInto

     Merges a Source contact record into a Target contact record, retaining the Target's information when
    Source and Target conflict.

    This API can be used to merge two contact records in your database.

    * The **Source** (or **Secondary**) contact is specified in the URL (`/people/{vanId}/mergeInto`);
    this record will be deleted as part of the merge
    * The **Target** (or **Primary**) contact is specified in the body of the request and survives the
    merge

    >❗️ Merges are permanent and **cannot** be undone. Use this endpoint with caution.

    Some fields may conflict between the two records and the merge process will not be able to retain
    both values (e.g., different first names). In this case, the API will retain the Target's
    information, which is the same behavior as the default selections in the Contacts Merge Wizard in
    the UI. Note that if you need to retain information from the Source, you can make a subsequent
    [/people/{vanId}](ref:peoplevanid) call to update the Target with the value(s) from the Source
    record you want to persist. All other fields where multiple values can be stored--such as emails,
    phones, and addresses--will be combined into the Target record.

    Not all records can be merged; if a record cannot be merged it will be treated as an [Input
    Validation](ref:input-validation) error with details provided in the `text` field of the error
    response. Though not exhaustive, some conditions that could prevent a merge are:

    * Both VANIDs need to exist and be accessible to you
    * Both records must have the same `contactMode`
    * If Disclosure Fields are enabled, the Source record cannot be linked to a Contribution or
    Disbursement

    To check if records can be merged without actually merging, you can specify `?whatIf=true` in the
    query string.

    Args:
        van_id (int):
        what_if (Union[Unset, None, bool]):
        json_body (PeoplevanidmergeintoJsonBody):

    Returns:
        Response[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]
    """

    kwargs = _get_kwargs(
        van_id=van_id,
        client=client,
        json_body=json_body,
        what_if=what_if,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    van_id: int,
    *,
    client: Client,
    json_body: PeoplevanidmergeintoJsonBody,
    what_if: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]:
    """/people/{vanId}/mergeInto

     Merges a Source contact record into a Target contact record, retaining the Target's information when
    Source and Target conflict.

    This API can be used to merge two contact records in your database.

    * The **Source** (or **Secondary**) contact is specified in the URL (`/people/{vanId}/mergeInto`);
    this record will be deleted as part of the merge
    * The **Target** (or **Primary**) contact is specified in the body of the request and survives the
    merge

    >❗️ Merges are permanent and **cannot** be undone. Use this endpoint with caution.

    Some fields may conflict between the two records and the merge process will not be able to retain
    both values (e.g., different first names). In this case, the API will retain the Target's
    information, which is the same behavior as the default selections in the Contacts Merge Wizard in
    the UI. Note that if you need to retain information from the Source, you can make a subsequent
    [/people/{vanId}](ref:peoplevanid) call to update the Target with the value(s) from the Source
    record you want to persist. All other fields where multiple values can be stored--such as emails,
    phones, and addresses--will be combined into the Target record.

    Not all records can be merged; if a record cannot be merged it will be treated as an [Input
    Validation](ref:input-validation) error with details provided in the `text` field of the error
    response. Though not exhaustive, some conditions that could prevent a merge are:

    * Both VANIDs need to exist and be accessible to you
    * Both records must have the same `contactMode`
    * If Disclosure Fields are enabled, the Source record cannot be linked to a Contribution or
    Disbursement

    To check if records can be merged without actually merging, you can specify `?whatIf=true` in the
    query string.

    Args:
        van_id (int):
        what_if (Union[Unset, None, bool]):
        json_body (PeoplevanidmergeintoJsonBody):

    Returns:
        Response[Union[PeoplevanidmergeintoResponse200, PeoplevanidmergeintoResponse400]]
    """

    return (
        await asyncio_detailed(
            van_id=van_id,
            client=client,
            json_body=json_body,
            what_if=what_if,
        )
    ).parsed
