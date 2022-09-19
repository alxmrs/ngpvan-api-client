from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.employersemployerid_1_json_body import Employersemployerid1JsonBody
from ...models.employersemployerid_1_response_400 import Employersemployerid1Response400
from ...models.employersemployerid_1_response_404 import Employersemployerid1Response404
from ...types import Response


def _get_kwargs(
    employer_id: int = 671,
    *,
    client: Client,
    json_body: Employersemployerid1JsonBody,
) -> Dict[str, Any]:
    url = "{}/employers/{employerId}".format(client.base_url, employerId=employer_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]:
    if response.status_code == 400:
        response_400 = Employersemployerid1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = Employersemployerid1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]:
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
    json_body: Employersemployerid1JsonBody,
) -> Response[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]:
    """/employers/{employerId}

     Changes the `isMyOrganization` status of an Employer.

    Args:
        employer_id (int):  Default: 671.
        json_body (Employersemployerid1JsonBody):

    Returns:
        Response[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]
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
    json_body: Employersemployerid1JsonBody,
) -> Optional[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]:
    """/employers/{employerId}

     Changes the `isMyOrganization` status of an Employer.

    Args:
        employer_id (int):  Default: 671.
        json_body (Employersemployerid1JsonBody):

    Returns:
        Response[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]
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
    json_body: Employersemployerid1JsonBody,
) -> Response[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]:
    """/employers/{employerId}

     Changes the `isMyOrganization` status of an Employer.

    Args:
        employer_id (int):  Default: 671.
        json_body (Employersemployerid1JsonBody):

    Returns:
        Response[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]
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
    json_body: Employersemployerid1JsonBody,
) -> Optional[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]:
    """/employers/{employerId}

     Changes the `isMyOrganization` status of an Employer.

    Args:
        employer_id (int):  Default: 671.
        json_body (Employersemployerid1JsonBody):

    Returns:
        Response[Union[Any, Employersemployerid1Response400, Employersemployerid1Response404]]
    """

    return (
        await asyncio_detailed(
            employer_id=employer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
