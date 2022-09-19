from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.departmentsdepartmentid_response_200 import DepartmentsdepartmentidResponse200
from ...models.departmentsdepartmentid_response_400 import DepartmentsdepartmentidResponse400
from ...models.departmentsdepartmentid_response_404 import DepartmentsdepartmentidResponse404
from ...types import Response


def _get_kwargs(
    department_id: int = 123,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/departments/{departmentId}".format(client.base_url, departmentId=department_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[
    Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]
]:
    if response.status_code == 200:
        response_200 = DepartmentsdepartmentidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = DepartmentsdepartmentidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = DepartmentsdepartmentidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    department_id: int = 123,
    *,
    client: Client,
) -> Response[
    Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]
]:
    """/departments/{departmentId}

     Use this endpoint to retrieve information about a specific Department available in the current
    context.

    Args:
        department_id (int):  Default: 123.

    Returns:
        Response[Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]]
    """

    kwargs = _get_kwargs(
        department_id=department_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    department_id: int = 123,
    *,
    client: Client,
) -> Optional[
    Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]
]:
    """/departments/{departmentId}

     Use this endpoint to retrieve information about a specific Department available in the current
    context.

    Args:
        department_id (int):  Default: 123.

    Returns:
        Response[Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]]
    """

    return sync_detailed(
        department_id=department_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    department_id: int = 123,
    *,
    client: Client,
) -> Response[
    Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]
]:
    """/departments/{departmentId}

     Use this endpoint to retrieve information about a specific Department available in the current
    context.

    Args:
        department_id (int):  Default: 123.

    Returns:
        Response[Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]]
    """

    kwargs = _get_kwargs(
        department_id=department_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    department_id: int = 123,
    *,
    client: Client,
) -> Optional[
    Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]
]:
    """/departments/{departmentId}

     Use this endpoint to retrieve information about a specific Department available in the current
    context.

    Args:
        department_id (int):  Default: 123.

    Returns:
        Response[Union[DepartmentsdepartmentidResponse200, DepartmentsdepartmentidResponse400, DepartmentsdepartmentidResponse404]]
    """

    return (
        await asyncio_detailed(
            department_id=department_id,
            client=client,
        )
    ).parsed
