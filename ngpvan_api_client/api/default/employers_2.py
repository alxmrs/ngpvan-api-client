from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.employers_2_json_body import Employers2JsonBody
from ...models.employers_2_response_400 import Employers2Response400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Employers2JsonBody,
) -> Dict[str, Any]:
    url = "{}/employers".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Employers2Response400]:
    if response.status_code == 400:
        response_400 = Employers2Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Employers2Response400]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Employers2JsonBody,
) -> Response[Employers2Response400]:
    """/employers

     Use this endpoint to create a new Employer.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and an
    [Employer](ref:employers) object with the integer ID of the created Employer in the response body
    and any associated [Worksites](ref:worksites). If no Worksite was specified, a default Worksite will
    be created. It also sets the **Location** header to the [location](ref:employersemployerid) of the
    Employer.

    Args:
        json_body (Employers2JsonBody):

    Returns:
        Response[Employers2Response400]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: Employers2JsonBody,
) -> Optional[Employers2Response400]:
    """/employers

     Use this endpoint to create a new Employer.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and an
    [Employer](ref:employers) object with the integer ID of the created Employer in the response body
    and any associated [Worksites](ref:worksites). If no Worksite was specified, a default Worksite will
    be created. It also sets the **Location** header to the [location](ref:employersemployerid) of the
    Employer.

    Args:
        json_body (Employers2JsonBody):

    Returns:
        Response[Employers2Response400]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Employers2JsonBody,
) -> Response[Employers2Response400]:
    """/employers

     Use this endpoint to create a new Employer.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and an
    [Employer](ref:employers) object with the integer ID of the created Employer in the response body
    and any associated [Worksites](ref:worksites). If no Worksite was specified, a default Worksite will
    be created. It also sets the **Location** header to the [location](ref:employersemployerid) of the
    Employer.

    Args:
        json_body (Employers2JsonBody):

    Returns:
        Response[Employers2Response400]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Employers2JsonBody,
) -> Optional[Employers2Response400]:
    """/employers

     Use this endpoint to create a new Employer.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and an
    [Employer](ref:employers) object with the integer ID of the created Employer in the response body
    and any associated [Worksites](ref:worksites). If no Worksite was specified, a default Worksite will
    be created. It also sets the **Location** header to the [location](ref:employersemployerid) of the
    Employer.

    Args:
        json_body (Employers2JsonBody):

    Returns:
        Response[Employers2Response400]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
