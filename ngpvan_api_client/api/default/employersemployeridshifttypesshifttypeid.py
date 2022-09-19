from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.employersemployeridshifttypesshifttypeid_response_201 import (
    EmployersemployeridshifttypesshifttypeidResponse201,
)
from ...models.employersemployeridshifttypesshifttypeid_response_400 import (
    EmployersemployeridshifttypesshifttypeidResponse400,
)
from ...models.employersemployeridshifttypesshifttypeid_response_404 import (
    EmployersemployeridshifttypesshifttypeidResponse404,
)
from ...types import Response


def _get_kwargs(
    employer_id: int = 671,
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/shiftTypes/{shiftTypeId}".format(
        client.base_url, employerId=employer_id, shiftTypeId=shift_type_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[
        EmployersemployeridshifttypesshifttypeidResponse201,
        EmployersemployeridshifttypesshifttypeidResponse400,
        EmployersemployeridshifttypesshifttypeidResponse404,
    ]
]:
    if response.status_code == 201:
        response_201 = EmployersemployeridshifttypesshifttypeidResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = EmployersemployeridshifttypesshifttypeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = EmployersemployeridshifttypesshifttypeidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        EmployersemployeridshifttypesshifttypeidResponse201,
        EmployersemployeridshifttypesshifttypeidResponse400,
        EmployersemployeridshifttypesshifttypeidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: int = 671,
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Response[
    Union[
        EmployersemployeridshifttypesshifttypeidResponse201,
        EmployersemployeridshifttypesshifttypeidResponse400,
        EmployersemployeridshifttypesshifttypeidResponse404,
    ]
]:
    """/employers/{employerId}/shiftTypes/{shiftTypeId}

     Use this endpoint to link a Shift Type to an existing Employer.

    Accepts a `shiftTypeId` for an existing Shift Type with optional overrides for `defaultStartTime`
    and `defaultEndTime`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Shift object in the
    response body.

    If the specified Employer or Shift Type does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        shift_type_id (int):  Default: 12.

    Returns:
        Response[Union[EmployersemployeridshifttypesshifttypeidResponse201, EmployersemployeridshifttypesshifttypeidResponse400, EmployersemployeridshifttypesshifttypeidResponse404]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        shift_type_id=shift_type_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    employer_id: int = 671,
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Optional[
    Union[
        EmployersemployeridshifttypesshifttypeidResponse201,
        EmployersemployeridshifttypesshifttypeidResponse400,
        EmployersemployeridshifttypesshifttypeidResponse404,
    ]
]:
    """/employers/{employerId}/shiftTypes/{shiftTypeId}

     Use this endpoint to link a Shift Type to an existing Employer.

    Accepts a `shiftTypeId` for an existing Shift Type with optional overrides for `defaultStartTime`
    and `defaultEndTime`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Shift object in the
    response body.

    If the specified Employer or Shift Type does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        shift_type_id (int):  Default: 12.

    Returns:
        Response[Union[EmployersemployeridshifttypesshifttypeidResponse201, EmployersemployeridshifttypesshifttypeidResponse400, EmployersemployeridshifttypesshifttypeidResponse404]]
    """

    return sync_detailed(
        employer_id=employer_id,
        shift_type_id=shift_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employer_id: int = 671,
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Response[
    Union[
        EmployersemployeridshifttypesshifttypeidResponse201,
        EmployersemployeridshifttypesshifttypeidResponse400,
        EmployersemployeridshifttypesshifttypeidResponse404,
    ]
]:
    """/employers/{employerId}/shiftTypes/{shiftTypeId}

     Use this endpoint to link a Shift Type to an existing Employer.

    Accepts a `shiftTypeId` for an existing Shift Type with optional overrides for `defaultStartTime`
    and `defaultEndTime`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Shift object in the
    response body.

    If the specified Employer or Shift Type does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        shift_type_id (int):  Default: 12.

    Returns:
        Response[Union[EmployersemployeridshifttypesshifttypeidResponse201, EmployersemployeridshifttypesshifttypeidResponse400, EmployersemployeridshifttypesshifttypeidResponse404]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        shift_type_id=shift_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: int = 671,
    shift_type_id: int = 12,
    *,
    client: Client,
) -> Optional[
    Union[
        EmployersemployeridshifttypesshifttypeidResponse201,
        EmployersemployeridshifttypesshifttypeidResponse400,
        EmployersemployeridshifttypesshifttypeidResponse404,
    ]
]:
    """/employers/{employerId}/shiftTypes/{shiftTypeId}

     Use this endpoint to link a Shift Type to an existing Employer.

    Accepts a `shiftTypeId` for an existing Shift Type with optional overrides for `defaultStartTime`
    and `defaultEndTime`.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Shift object in the
    response body.

    If the specified Employer or Shift Type does not exist, this endpoint will return an error with HTTP
    Status Code `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        shift_type_id (int):  Default: 12.

    Returns:
        Response[Union[EmployersemployeridshifttypesshifttypeidResponse201, EmployersemployeridshifttypesshifttypeidResponse400, EmployersemployeridshifttypesshifttypeidResponse404]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            shift_type_id=shift_type_id,
            client=client,
        )
    ).parsed
