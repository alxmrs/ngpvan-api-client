from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.employersemployeridworksites_json_body import EmployersemployeridworksitesJsonBody
from ...models.employersemployeridworksites_response_201 import EmployersemployeridworksitesResponse201
from ...models.employersemployeridworksites_response_400 import EmployersemployeridworksitesResponse400
from ...models.employersemployeridworksites_response_404 import EmployersemployeridworksitesResponse404
from ...types import Response


def _get_kwargs(
    employer_id: int = 671,
    *,
    client: Client,
    json_body: EmployersemployeridworksitesJsonBody,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/worksites".format(client.base_url, employerId=employer_id)

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
) -> Optional[
    Union[
        EmployersemployeridworksitesResponse201,
        EmployersemployeridworksitesResponse400,
        EmployersemployeridworksitesResponse404,
    ]
]:
    if response.status_code == 201:
        response_201 = EmployersemployeridworksitesResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = EmployersemployeridworksitesResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = EmployersemployeridworksitesResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        EmployersemployeridworksitesResponse201,
        EmployersemployeridworksitesResponse400,
        EmployersemployeridworksitesResponse404,
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
    *,
    client: Client,
    json_body: EmployersemployeridworksitesJsonBody,
) -> Response[
    Union[
        EmployersemployeridworksitesResponse201,
        EmployersemployeridworksitesResponse400,
        EmployersemployeridworksitesResponse404,
    ]
]:
    """/employers/{employerId}/worksites

     Use this endpoint to create a new Worksite for an Employer.

    Accepts a standard [Worksite](ref:worksites) object with no read-only values specified. If supplied,
    the `name` of the Worksite must be unique to the Employer.

    *Response*

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Worksite object with
    the integer ID of the created Worksite in the response body. It also sets the **Location** header to
    the [location](ref:worksitesworksiteid) of the Worksite.

    If the specified Employer does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        json_body (EmployersemployeridworksitesJsonBody):

    Returns:
        Response[Union[EmployersemployeridworksitesResponse201, EmployersemployeridworksitesResponse400, EmployersemployeridworksitesResponse404]]
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
    json_body: EmployersemployeridworksitesJsonBody,
) -> Optional[
    Union[
        EmployersemployeridworksitesResponse201,
        EmployersemployeridworksitesResponse400,
        EmployersemployeridworksitesResponse404,
    ]
]:
    """/employers/{employerId}/worksites

     Use this endpoint to create a new Worksite for an Employer.

    Accepts a standard [Worksite](ref:worksites) object with no read-only values specified. If supplied,
    the `name` of the Worksite must be unique to the Employer.

    *Response*

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Worksite object with
    the integer ID of the created Worksite in the response body. It also sets the **Location** header to
    the [location](ref:worksitesworksiteid) of the Worksite.

    If the specified Employer does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        json_body (EmployersemployeridworksitesJsonBody):

    Returns:
        Response[Union[EmployersemployeridworksitesResponse201, EmployersemployeridworksitesResponse400, EmployersemployeridworksitesResponse404]]
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
    json_body: EmployersemployeridworksitesJsonBody,
) -> Response[
    Union[
        EmployersemployeridworksitesResponse201,
        EmployersemployeridworksitesResponse400,
        EmployersemployeridworksitesResponse404,
    ]
]:
    """/employers/{employerId}/worksites

     Use this endpoint to create a new Worksite for an Employer.

    Accepts a standard [Worksite](ref:worksites) object with no read-only values specified. If supplied,
    the `name` of the Worksite must be unique to the Employer.

    *Response*

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Worksite object with
    the integer ID of the created Worksite in the response body. It also sets the **Location** header to
    the [location](ref:worksitesworksiteid) of the Worksite.

    If the specified Employer does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        json_body (EmployersemployeridworksitesJsonBody):

    Returns:
        Response[Union[EmployersemployeridworksitesResponse201, EmployersemployeridworksitesResponse400, EmployersemployeridworksitesResponse404]]
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
    json_body: EmployersemployeridworksitesJsonBody,
) -> Optional[
    Union[
        EmployersemployeridworksitesResponse201,
        EmployersemployeridworksitesResponse400,
        EmployersemployeridworksitesResponse404,
    ]
]:
    """/employers/{employerId}/worksites

     Use this endpoint to create a new Worksite for an Employer.

    Accepts a standard [Worksite](ref:worksites) object with no read-only values specified. If supplied,
    the `name` of the Worksite must be unique to the Employer.

    *Response*

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a Worksite object with
    the integer ID of the created Worksite in the response body. It also sets the **Location** header to
    the [location](ref:worksitesworksiteid) of the Worksite.

    If the specified Employer does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        json_body (EmployersemployeridworksitesJsonBody):

    Returns:
        Response[Union[EmployersemployeridworksitesResponse201, EmployersemployeridworksitesResponse400, EmployersemployeridworksitesResponse404]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
