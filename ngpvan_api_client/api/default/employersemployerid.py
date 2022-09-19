from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.employersemployerid_response_400 import EmployersemployeridResponse400
from ...models.employersemployerid_response_404 import EmployersemployeridResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    employer_id: int = 671,
    *,
    client: Client,
    expand: Union[Unset, None, str] = "parent,phones",
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}".format(client.base_url, employerId=employer_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$expand"] = expand

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
) -> Optional[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]:
    if response.status_code == 400:
        response_400 = EmployersemployeridResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = EmployersemployeridResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]:
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
    expand: Union[Unset, None, str] = "parent,phones",
) -> Response[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]:
    """/employers/{employerId}

     Use this endpoint to retrieve the details of a specific Employer.

    Args:
        employer_id (int):  Default: 671.
        expand (Union[Unset, None, str]):  Default: 'parent,phones'.

    Returns:
        Response[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        client=client,
        expand=expand,
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
    expand: Union[Unset, None, str] = "parent,phones",
) -> Optional[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]:
    """/employers/{employerId}

     Use this endpoint to retrieve the details of a specific Employer.

    Args:
        employer_id (int):  Default: 671.
        expand (Union[Unset, None, str]):  Default: 'parent,phones'.

    Returns:
        Response[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]
    """

    return sync_detailed(
        employer_id=employer_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    employer_id: int = 671,
    *,
    client: Client,
    expand: Union[Unset, None, str] = "parent,phones",
) -> Response[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]:
    """/employers/{employerId}

     Use this endpoint to retrieve the details of a specific Employer.

    Args:
        employer_id (int):  Default: 671.
        expand (Union[Unset, None, str]):  Default: 'parent,phones'.

    Returns:
        Response[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]
    """

    kwargs = _get_kwargs(
        employer_id=employer_id,
        client=client,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    employer_id: int = 671,
    *,
    client: Client,
    expand: Union[Unset, None, str] = "parent,phones",
) -> Optional[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]:
    """/employers/{employerId}

     Use this endpoint to retrieve the details of a specific Employer.

    Args:
        employer_id (int):  Default: 671.
        expand (Union[Unset, None, str]):  Default: 'parent,phones'.

    Returns:
        Response[Union[EmployersemployeridResponse400, EmployersemployeridResponse404]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            client=client,
            expand=expand,
        )
    ).parsed
