from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_people_contact_mode import GetPeopleContactMode
from ...models.get_people_invalid_phone_number import GetPeopleInvalidPhoneNumber
from ...models.get_people_not_enough_search_parameters import GetPeopleNotEnoughSearchParameters
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    first_name: Union[Unset, None, str] = UNSET,
    middle_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    street_address: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    zip_or_postal_code: Union[Unset, None, str] = UNSET,
    phone_number: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    common_name: Union[Unset, None, str] = UNSET,
    official_name: Union[Unset, None, str] = UNSET,
    contact_mode: Union[Unset, None, GetPeopleContactMode] = UNSET,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
    orderby: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/people".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["firstName"] = first_name

    params["middleName"] = middle_name

    params["lastName"] = last_name

    params["streetAddress"] = street_address

    params["city"] = city

    params["stateOrProvince"] = state_or_province

    params["zipOrPostalCode"] = zip_or_postal_code

    params["phoneNumber"] = phone_number

    params["email"] = email

    params["commonName"] = common_name

    params["officialName"] = official_name

    json_contact_mode: Union[Unset, None, str] = UNSET
    if not isinstance(contact_mode, Unset):
        json_contact_mode = contact_mode.value if contact_mode else None

    params["contactMode"] = json_contact_mode

    params["$top"] = top

    params["$skip"] = skip

    params["$expand"] = expand

    params["$orderby"] = orderby

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
) -> Optional[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]:
    if response.status_code == 400:

        def _parse_response_400(data: object) -> Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = GetPeopleInvalidPhoneNumber.from_dict(data)

                return response_400_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_1 = GetPeopleNotEnoughSearchParameters.from_dict(data)

            return response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    first_name: Union[Unset, None, str] = UNSET,
    middle_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    street_address: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    zip_or_postal_code: Union[Unset, None, str] = UNSET,
    phone_number: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    common_name: Union[Unset, None, str] = UNSET,
    official_name: Union[Unset, None, str] = UNSET,
    contact_mode: Union[Unset, None, GetPeopleContactMode] = UNSET,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
    orderby: Union[Unset, None, str] = UNSET,
) -> Response[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]:
    """/people

     Returns a [paginated](ref:pagination) list of [contacts](ref:common-models#person) who meet all of
    the specified criteria.

    Unless noted otherwise, search criteria can be partial inputs; they will match any string that
    starts with the value provided (case-insensitive).

    At least one string parameter must be specified.

    Args:
        first_name (Union[Unset, None, str]):
        middle_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        street_address (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state_or_province (Union[Unset, None, str]):
        zip_or_postal_code (Union[Unset, None, str]):
        phone_number (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        common_name (Union[Unset, None, str]):
        official_name (Union[Unset, None, str]):
        contact_mode (Union[Unset, None, GetPeopleContactMode]):
        top (Union[Unset, None, int]):
        skip (Union[Unset, None, int]):
        expand (Union[Unset, None, str]):
        orderby (Union[Unset, None, str]):

    Returns:
        Response[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]
    """

    kwargs = _get_kwargs(
        client=client,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        street_address=street_address,
        city=city,
        state_or_province=state_or_province,
        zip_or_postal_code=zip_or_postal_code,
        phone_number=phone_number,
        email=email,
        common_name=common_name,
        official_name=official_name,
        contact_mode=contact_mode,
        top=top,
        skip=skip,
        expand=expand,
        orderby=orderby,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    first_name: Union[Unset, None, str] = UNSET,
    middle_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    street_address: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    zip_or_postal_code: Union[Unset, None, str] = UNSET,
    phone_number: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    common_name: Union[Unset, None, str] = UNSET,
    official_name: Union[Unset, None, str] = UNSET,
    contact_mode: Union[Unset, None, GetPeopleContactMode] = UNSET,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
    orderby: Union[Unset, None, str] = UNSET,
) -> Optional[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]:
    """/people

     Returns a [paginated](ref:pagination) list of [contacts](ref:common-models#person) who meet all of
    the specified criteria.

    Unless noted otherwise, search criteria can be partial inputs; they will match any string that
    starts with the value provided (case-insensitive).

    At least one string parameter must be specified.

    Args:
        first_name (Union[Unset, None, str]):
        middle_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        street_address (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state_or_province (Union[Unset, None, str]):
        zip_or_postal_code (Union[Unset, None, str]):
        phone_number (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        common_name (Union[Unset, None, str]):
        official_name (Union[Unset, None, str]):
        contact_mode (Union[Unset, None, GetPeopleContactMode]):
        top (Union[Unset, None, int]):
        skip (Union[Unset, None, int]):
        expand (Union[Unset, None, str]):
        orderby (Union[Unset, None, str]):

    Returns:
        Response[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]
    """

    return sync_detailed(
        client=client,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        street_address=street_address,
        city=city,
        state_or_province=state_or_province,
        zip_or_postal_code=zip_or_postal_code,
        phone_number=phone_number,
        email=email,
        common_name=common_name,
        official_name=official_name,
        contact_mode=contact_mode,
        top=top,
        skip=skip,
        expand=expand,
        orderby=orderby,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    first_name: Union[Unset, None, str] = UNSET,
    middle_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    street_address: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    zip_or_postal_code: Union[Unset, None, str] = UNSET,
    phone_number: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    common_name: Union[Unset, None, str] = UNSET,
    official_name: Union[Unset, None, str] = UNSET,
    contact_mode: Union[Unset, None, GetPeopleContactMode] = UNSET,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
    orderby: Union[Unset, None, str] = UNSET,
) -> Response[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]:
    """/people

     Returns a [paginated](ref:pagination) list of [contacts](ref:common-models#person) who meet all of
    the specified criteria.

    Unless noted otherwise, search criteria can be partial inputs; they will match any string that
    starts with the value provided (case-insensitive).

    At least one string parameter must be specified.

    Args:
        first_name (Union[Unset, None, str]):
        middle_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        street_address (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state_or_province (Union[Unset, None, str]):
        zip_or_postal_code (Union[Unset, None, str]):
        phone_number (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        common_name (Union[Unset, None, str]):
        official_name (Union[Unset, None, str]):
        contact_mode (Union[Unset, None, GetPeopleContactMode]):
        top (Union[Unset, None, int]):
        skip (Union[Unset, None, int]):
        expand (Union[Unset, None, str]):
        orderby (Union[Unset, None, str]):

    Returns:
        Response[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]
    """

    kwargs = _get_kwargs(
        client=client,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        street_address=street_address,
        city=city,
        state_or_province=state_or_province,
        zip_or_postal_code=zip_or_postal_code,
        phone_number=phone_number,
        email=email,
        common_name=common_name,
        official_name=official_name,
        contact_mode=contact_mode,
        top=top,
        skip=skip,
        expand=expand,
        orderby=orderby,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    first_name: Union[Unset, None, str] = UNSET,
    middle_name: Union[Unset, None, str] = UNSET,
    last_name: Union[Unset, None, str] = UNSET,
    street_address: Union[Unset, None, str] = UNSET,
    city: Union[Unset, None, str] = UNSET,
    state_or_province: Union[Unset, None, str] = UNSET,
    zip_or_postal_code: Union[Unset, None, str] = UNSET,
    phone_number: Union[Unset, None, str] = UNSET,
    email: Union[Unset, None, str] = UNSET,
    common_name: Union[Unset, None, str] = UNSET,
    official_name: Union[Unset, None, str] = UNSET,
    contact_mode: Union[Unset, None, GetPeopleContactMode] = UNSET,
    top: Union[Unset, None, int] = UNSET,
    skip: Union[Unset, None, int] = UNSET,
    expand: Union[Unset, None, str] = UNSET,
    orderby: Union[Unset, None, str] = UNSET,
) -> Optional[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]:
    """/people

     Returns a [paginated](ref:pagination) list of [contacts](ref:common-models#person) who meet all of
    the specified criteria.

    Unless noted otherwise, search criteria can be partial inputs; they will match any string that
    starts with the value provided (case-insensitive).

    At least one string parameter must be specified.

    Args:
        first_name (Union[Unset, None, str]):
        middle_name (Union[Unset, None, str]):
        last_name (Union[Unset, None, str]):
        street_address (Union[Unset, None, str]):
        city (Union[Unset, None, str]):
        state_or_province (Union[Unset, None, str]):
        zip_or_postal_code (Union[Unset, None, str]):
        phone_number (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        common_name (Union[Unset, None, str]):
        official_name (Union[Unset, None, str]):
        contact_mode (Union[Unset, None, GetPeopleContactMode]):
        top (Union[Unset, None, int]):
        skip (Union[Unset, None, int]):
        expand (Union[Unset, None, str]):
        orderby (Union[Unset, None, str]):

    Returns:
        Response[Union[GetPeopleInvalidPhoneNumber, GetPeopleNotEnoughSearchParameters]]
    """

    return (
        await asyncio_detailed(
            client=client,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            street_address=street_address,
            city=city,
            state_or_province=state_or_province,
            zip_or_postal_code=zip_or_postal_code,
            phone_number=phone_number,
            email=email,
            common_name=common_name,
            official_name=official_name,
            contact_mode=contact_mode,
            top=top,
            skip=skip,
            expand=expand,
            orderby=orderby,
        )
    ).parsed
