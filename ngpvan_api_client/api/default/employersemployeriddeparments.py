from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.employersemployeriddeparments_json_body import EmployersemployeriddeparmentsJsonBody
from ...models.employersemployeriddeparments_response_400 import EmployersemployeriddeparmentsResponse400
from ...models.employersemployeriddeparments_response_404 import EmployersemployeriddeparmentsResponse404
from ...types import Response


def _get_kwargs(
    employer_id: int = 671,
    *,
    client: Client,
    json_body: EmployersemployeriddeparmentsJsonBody,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/departments".format(client.base_url, employerId=employer_id)

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
) -> Optional[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 400:
        response_400 = EmployersemployeriddeparmentsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = EmployersemployeriddeparmentsResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    employer_id: int = 671,
    *,
    client: Client,
    json_body: EmployersemployeriddeparmentsJsonBody,
) -> Response[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]:
    """/employers/{employerId}/departments

     Use this endpoint to create a new Department in the current context.

    Accepts a standard Department object with no read-only values specified. The `name` of the
    department must be unique to the Employer, and if supplied, the `parentDepartmentId` must already
    exist for the specified Employer.

    In the example below, we’re creating a Department called *Human Resources* which is a child of
    `parentDepartmentId 135`.


    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Department object
    with `departmentId` populated with the integer ID of the created Department in the response body. It
    also sets the **Location** header to the [location](ref:departmentsdepartmentid) of the Department.

    If the specified Employer does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        json_body (EmployersemployeriddeparmentsJsonBody):

    Returns:
        Response[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    employer_id: int = 671,
    *,
    client: Client,
    json_body: EmployersemployeriddeparmentsJsonBody,
) -> Optional[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]:
    """/employers/{employerId}/departments

     Use this endpoint to create a new Department in the current context.

    Accepts a standard Department object with no read-only values specified. The `name` of the
    department must be unique to the Employer, and if supplied, the `parentDepartmentId` must already
    exist for the specified Employer.

    In the example below, we’re creating a Department called *Human Resources* which is a child of
    `parentDepartmentId 135`.


    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Department object
    with `departmentId` populated with the integer ID of the created Department in the response body. It
    also sets the **Location** header to the [location](ref:departmentsdepartmentid) of the Department.

    If the specified Employer does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        json_body (EmployersemployeriddeparmentsJsonBody):

    Returns:
        Response[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]
    """

    return sync_detailed(
        employer_id=employer_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    employer_id: int = 671,
    *,
    client: Client,
    json_body: EmployersemployeriddeparmentsJsonBody,
) -> Response[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]:
    """/employers/{employerId}/departments

     Use this endpoint to create a new Department in the current context.

    Accepts a standard Department object with no read-only values specified. The `name` of the
    department must be unique to the Employer, and if supplied, the `parentDepartmentId` must already
    exist for the specified Employer.

    In the example below, we’re creating a Department called *Human Resources* which is a child of
    `parentDepartmentId 135`.


    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Department object
    with `departmentId` populated with the integer ID of the created Department in the response body. It
    also sets the **Location** header to the [location](ref:departmentsdepartmentid) of the Department.

    If the specified Employer does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        json_body (EmployersemployeriddeparmentsJsonBody):

    Returns:
        Response[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: int = 671,
    *,
    client: Client,
    json_body: EmployersemployeriddeparmentsJsonBody,
) -> Optional[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]:
    """/employers/{employerId}/departments

     Use this endpoint to create a new Department in the current context.

    Accepts a standard Department object with no read-only values specified. The `name` of the
    department must be unique to the Employer, and if supplied, the `parentDepartmentId` must already
    exist for the specified Employer.

    In the example below, we’re creating a Department called *Human Resources* which is a child of
    `parentDepartmentId 135`.


    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Department object
    with `departmentId` populated with the integer ID of the created Department in the response body. It
    also sets the **Location** header to the [location](ref:departmentsdepartmentid) of the Department.

    If the specified Employer does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        json_body (EmployersemployeriddeparmentsJsonBody):

    Returns:
        Response[Union[Any, EmployersemployeriddeparmentsResponse400, EmployersemployeriddeparmentsResponse404]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
