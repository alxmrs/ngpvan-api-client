from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.signupseventsignupid_1_response_200 import Signupseventsignupid1Response200
from ...models.signupseventsignupid_1_response_400 import Signupseventsignupid1Response400
from ...models.signupseventsignupid_1_response_404 import Signupseventsignupid1Response404
from ...types import Response


def _get_kwargs(
    event_signup_id: int = 2452,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/signups/{eventSignupId}".format(client.base_url, eventSignupId=event_signup_id)

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
    Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]
]:
    if response.status_code == 200:
        response_200 = Signupseventsignupid1Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Signupseventsignupid1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Signupseventsignupid1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_signup_id: int = 2452,
    *,
    client: Client,
) -> Response[
    Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]
]:
    """/signups/{eventSignupId}

     Use this endpoint to retrieve a specific Event Signup.

    This endpoint returns a standard [Signup](ref:signups#common-models-33) object, if found.

    If the specified Signup does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        event_signup_id (int):  Default: 2452.

    Returns:
        Response[Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]]
    """

    kwargs = _get_kwargs(
        event_signup_id=event_signup_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    event_signup_id: int = 2452,
    *,
    client: Client,
) -> Optional[
    Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]
]:
    """/signups/{eventSignupId}

     Use this endpoint to retrieve a specific Event Signup.

    This endpoint returns a standard [Signup](ref:signups#common-models-33) object, if found.

    If the specified Signup does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        event_signup_id (int):  Default: 2452.

    Returns:
        Response[Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]]
    """

    return sync_detailed(
        event_signup_id=event_signup_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_signup_id: int = 2452,
    *,
    client: Client,
) -> Response[
    Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]
]:
    """/signups/{eventSignupId}

     Use this endpoint to retrieve a specific Event Signup.

    This endpoint returns a standard [Signup](ref:signups#common-models-33) object, if found.

    If the specified Signup does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        event_signup_id (int):  Default: 2452.

    Returns:
        Response[Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]]
    """

    kwargs = _get_kwargs(
        event_signup_id=event_signup_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_signup_id: int = 2452,
    *,
    client: Client,
) -> Optional[
    Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]
]:
    """/signups/{eventSignupId}

     Use this endpoint to retrieve a specific Event Signup.

    This endpoint returns a standard [Signup](ref:signups#common-models-33) object, if found.

    If the specified Signup does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    Args:
        event_signup_id (int):  Default: 2452.

    Returns:
        Response[Union[Signupseventsignupid1Response200, Signupseventsignupid1Response400, Signupseventsignupid1Response404]]
    """

    return (
        await asyncio_detailed(
            event_signup_id=event_signup_id,
            client=client,
        )
    ).parsed
