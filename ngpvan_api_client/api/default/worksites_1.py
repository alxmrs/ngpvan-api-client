from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.worksites_1_response_200 import Worksites1Response200
from ...models.worksites_1_response_400 import Worksites1Response400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    employer_id: Union[Unset, None, int] = 99,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "workAreas",
    top: Union[Unset, None, int] = 40,
) -> Dict[str, Any]:
    url = "{}/worksites".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["employerId"] = employer_id

    params["isMyOrganization"] = is_my_organization

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Worksites1Response200, Worksites1Response400]]:
    if response.status_code == 200:
        response_200 = Worksites1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Worksites1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Worksites1Response200, Worksites1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    employer_id: Union[Unset, None, int] = 99,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "workAreas",
    top: Union[Unset, None, int] = 40,
) -> Response[Union[Worksites1Response200, Worksites1Response400]]:
    """/worksites

     Use this endpoint to retrieve all Worksites that are available in the current context.

    Args:
        employer_id (Union[Unset, None, int]):  Default: 99.
        is_my_organization (Union[Unset, None, bool]):
        expand (Union[Unset, None, str]):  Default: 'workAreas'.
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[Worksites1Response200, Worksites1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        employer_id=employer_id,
        is_my_organization=is_my_organization,
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
    employer_id: Union[Unset, None, int] = 99,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "workAreas",
    top: Union[Unset, None, int] = 40,
) -> Optional[Union[Worksites1Response200, Worksites1Response400]]:
    """/worksites

     Use this endpoint to retrieve all Worksites that are available in the current context.

    Args:
        employer_id (Union[Unset, None, int]):  Default: 99.
        is_my_organization (Union[Unset, None, bool]):
        expand (Union[Unset, None, str]):  Default: 'workAreas'.
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[Worksites1Response200, Worksites1Response400]]
    """

    return sync_detailed(
        client=client,
        employer_id=employer_id,
        is_my_organization=is_my_organization,
        expand=expand,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    employer_id: Union[Unset, None, int] = 99,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "workAreas",
    top: Union[Unset, None, int] = 40,
) -> Response[Union[Worksites1Response200, Worksites1Response400]]:
    """/worksites

     Use this endpoint to retrieve all Worksites that are available in the current context.

    Args:
        employer_id (Union[Unset, None, int]):  Default: 99.
        is_my_organization (Union[Unset, None, bool]):
        expand (Union[Unset, None, str]):  Default: 'workAreas'.
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[Worksites1Response200, Worksites1Response400]]
    """

    kwargs = _get_kwargs(
        client=client,
        employer_id=employer_id,
        is_my_organization=is_my_organization,
        expand=expand,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    employer_id: Union[Unset, None, int] = 99,
    is_my_organization: Union[Unset, None, bool] = False,
    expand: Union[Unset, None, str] = "workAreas",
    top: Union[Unset, None, int] = 40,
) -> Optional[Union[Worksites1Response200, Worksites1Response400]]:
    """/worksites

     Use this endpoint to retrieve all Worksites that are available in the current context.

    Args:
        employer_id (Union[Unset, None, int]):  Default: 99.
        is_my_organization (Union[Unset, None, bool]):
        expand (Union[Unset, None, str]):  Default: 'workAreas'.
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[Worksites1Response200, Worksites1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            employer_id=employer_id,
            is_my_organization=is_my_organization,
            expand=expand,
            top=top,
        )
    ).parsed
