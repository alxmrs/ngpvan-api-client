from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_201 import (
    EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201,
)
from ...models.employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_400 import (
    EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400,
)
from ...models.employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_404 import (
    EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404,
)
from ...types import Response


def _get_kwargs(
    employer_id: int = 671,
    bargaining_unit_id: int = 35,
    job_class_id: int = 805,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}/bargainingUnits/{bargainingUnitId}/jobClasses/{jobClassId}".format(
        client.base_url, employerId=employer_id, bargainingUnitId=bargaining_unit_id, jobClassId=job_class_id
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
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404,
    ]
]:
    if response.status_code == 201:
        response_201 = EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201.from_dict(
            response.json()
        )

        return response_201
    if response.status_code == 400:
        response_400 = EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400.from_dict(
            response.json()
        )

        return response_400
    if response.status_code == 404:
        response_404 = EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404.from_dict(
            response.json()
        )

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404,
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
    bargaining_unit_id: int = 35,
    job_class_id: int = 805,
    *,
    client: Client,
) -> Response[
    Union[
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404,
    ]
]:
    """/employers/{employerId}/bargainingUnits/{bargainingUnitId}/jobClasses/{jobClassId}

     Use this endpoint to link a master Job Class to an existing Employer and Bargaining Unit.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a composite Employer
    Bargaining Unit Job Class object in the response body.

    If the specified Employer, Bargaining Unit, or Job Class does not exist, this endpoint will return
    an error with HTTP Status Code `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        bargaining_unit_id (int):  Default: 35.
        job_class_id (int):  Default: 805.

    Returns:
        Response[Union[EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201, EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400, EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        bargaining_unit_id=bargaining_unit_id,
        job_class_id=job_class_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    employer_id: int = 671,
    bargaining_unit_id: int = 35,
    job_class_id: int = 805,
    *,
    client: Client,
) -> Optional[
    Union[
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404,
    ]
]:
    """/employers/{employerId}/bargainingUnits/{bargainingUnitId}/jobClasses/{jobClassId}

     Use this endpoint to link a master Job Class to an existing Employer and Bargaining Unit.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a composite Employer
    Bargaining Unit Job Class object in the response body.

    If the specified Employer, Bargaining Unit, or Job Class does not exist, this endpoint will return
    an error with HTTP Status Code `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        bargaining_unit_id (int):  Default: 35.
        job_class_id (int):  Default: 805.

    Returns:
        Response[Union[EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201, EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400, EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404]]
    """

    return sync_detailed(
        employer_id=employer_id,
        bargaining_unit_id=bargaining_unit_id,
        job_class_id=job_class_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employer_id: int = 671,
    bargaining_unit_id: int = 35,
    job_class_id: int = 805,
    *,
    client: Client,
) -> Response[
    Union[
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404,
    ]
]:
    """/employers/{employerId}/bargainingUnits/{bargainingUnitId}/jobClasses/{jobClassId}

     Use this endpoint to link a master Job Class to an existing Employer and Bargaining Unit.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a composite Employer
    Bargaining Unit Job Class object in the response body.

    If the specified Employer, Bargaining Unit, or Job Class does not exist, this endpoint will return
    an error with HTTP Status Code `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        bargaining_unit_id (int):  Default: 35.
        job_class_id (int):  Default: 805.

    Returns:
        Response[Union[EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201, EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400, EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        bargaining_unit_id=bargaining_unit_id,
        job_class_id=job_class_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: int = 671,
    bargaining_unit_id: int = 35,
    job_class_id: int = 805,
    *,
    client: Client,
) -> Optional[
    Union[
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400,
        EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404,
    ]
]:
    """/employers/{employerId}/bargainingUnits/{bargainingUnitId}/jobClasses/{jobClassId}

     Use this endpoint to link a master Job Class to an existing Employer and Bargaining Unit.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and a composite Employer
    Bargaining Unit Job Class object in the response body.

    If the specified Employer, Bargaining Unit, or Job Class does not exist, this endpoint will return
    an error with HTTP Status Code `404 Not Found`.

    Args:
        employer_id (int):  Default: 671.
        bargaining_unit_id (int):  Default: 35.
        job_class_id (int):  Default: 805.

    Returns:
        Response[Union[EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201, EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse400, EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse404]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            bargaining_unit_id=bargaining_unit_id,
            job_class_id=job_class_id,
            client=client,
        )
    ).parsed
