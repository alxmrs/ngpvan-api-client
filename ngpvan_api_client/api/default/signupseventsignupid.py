from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.signupseventsignupid_json_body import SignupseventsignupidJsonBody
from ...models.signupseventsignupid_response_400 import SignupseventsignupidResponse400
from ...models.signupseventsignupid_response_404 import SignupseventsignupidResponse404
from ...types import Response


def _get_kwargs(
    event_signup_id: int = 2452,
    *,
    client: Client,
    json_body: SignupseventsignupidJsonBody,
) -> Dict[str, Any]:
    url = "{}/signups/{eventSignupId}".format(client.base_url, eventSignupId=event_signup_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = SignupseventsignupidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = SignupseventsignupidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]:
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
    json_body: SignupseventsignupidJsonBody,
) -> Response[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]:
    """/signups/{eventSignupId}

     Use this endpoint to update a specific existing Signup. A record of this change is displayed in the
    VAN UI.

    A Signup’s Event and Person properties are immutable after creation. If you want to sign up a Person
    for a different Event, first [delete](ref:signups#signupeventsignupid-2) the existing Signup and
    [create](ref:signups#signups-2) a new one.

    If you do not know the `eventSignupId`, consider using the [create or modify](ref:signups#signups-2)
    endpoint.

    When a Signup is updated, a [canvass response](ref:people#peoplevanidcanvassresponses) is generated
    to represent the signup interaction. The *Input Type* is API, the *Date Canvassed* is the current
    date, the *Canvasser* is the API user associated with the current context, and the *Result Code*
    corresponds to a result most appropriate for the given Status (e.g., *Scheduled* → *Canvassed*).
    Consult the VAN UI for a detailed mapping.

    Args:
        event_signup_id (int):  Default: 2452.
        json_body (SignupseventsignupidJsonBody):

    Returns:
        Response[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]
    """

    kwargs = _get_kwargs(
        event_signup_id=event_signup_id,
        client=client,
        json_body=json_body,
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
    json_body: SignupseventsignupidJsonBody,
) -> Optional[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]:
    """/signups/{eventSignupId}

     Use this endpoint to update a specific existing Signup. A record of this change is displayed in the
    VAN UI.

    A Signup’s Event and Person properties are immutable after creation. If you want to sign up a Person
    for a different Event, first [delete](ref:signups#signupeventsignupid-2) the existing Signup and
    [create](ref:signups#signups-2) a new one.

    If you do not know the `eventSignupId`, consider using the [create or modify](ref:signups#signups-2)
    endpoint.

    When a Signup is updated, a [canvass response](ref:people#peoplevanidcanvassresponses) is generated
    to represent the signup interaction. The *Input Type* is API, the *Date Canvassed* is the current
    date, the *Canvasser* is the API user associated with the current context, and the *Result Code*
    corresponds to a result most appropriate for the given Status (e.g., *Scheduled* → *Canvassed*).
    Consult the VAN UI for a detailed mapping.

    Args:
        event_signup_id (int):  Default: 2452.
        json_body (SignupseventsignupidJsonBody):

    Returns:
        Response[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]
    """

    return sync_detailed(
        event_signup_id=event_signup_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    event_signup_id: int = 2452,
    *,
    client: Client,
    json_body: SignupseventsignupidJsonBody,
) -> Response[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]:
    """/signups/{eventSignupId}

     Use this endpoint to update a specific existing Signup. A record of this change is displayed in the
    VAN UI.

    A Signup’s Event and Person properties are immutable after creation. If you want to sign up a Person
    for a different Event, first [delete](ref:signups#signupeventsignupid-2) the existing Signup and
    [create](ref:signups#signups-2) a new one.

    If you do not know the `eventSignupId`, consider using the [create or modify](ref:signups#signups-2)
    endpoint.

    When a Signup is updated, a [canvass response](ref:people#peoplevanidcanvassresponses) is generated
    to represent the signup interaction. The *Input Type* is API, the *Date Canvassed* is the current
    date, the *Canvasser* is the API user associated with the current context, and the *Result Code*
    corresponds to a result most appropriate for the given Status (e.g., *Scheduled* → *Canvassed*).
    Consult the VAN UI for a detailed mapping.

    Args:
        event_signup_id (int):  Default: 2452.
        json_body (SignupseventsignupidJsonBody):

    Returns:
        Response[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]
    """

    kwargs = _get_kwargs(
        event_signup_id=event_signup_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_signup_id: int = 2452,
    *,
    client: Client,
    json_body: SignupseventsignupidJsonBody,
) -> Optional[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]:
    """/signups/{eventSignupId}

     Use this endpoint to update a specific existing Signup. A record of this change is displayed in the
    VAN UI.

    A Signup’s Event and Person properties are immutable after creation. If you want to sign up a Person
    for a different Event, first [delete](ref:signups#signupeventsignupid-2) the existing Signup and
    [create](ref:signups#signups-2) a new one.

    If you do not know the `eventSignupId`, consider using the [create or modify](ref:signups#signups-2)
    endpoint.

    When a Signup is updated, a [canvass response](ref:people#peoplevanidcanvassresponses) is generated
    to represent the signup interaction. The *Input Type* is API, the *Date Canvassed* is the current
    date, the *Canvasser* is the API user associated with the current context, and the *Result Code*
    corresponds to a result most appropriate for the given Status (e.g., *Scheduled* → *Canvassed*).
    Consult the VAN UI for a detailed mapping.

    Args:
        event_signup_id (int):  Default: 2452.
        json_body (SignupseventsignupidJsonBody):

    Returns:
        Response[Union[Any, SignupseventsignupidResponse400, SignupseventsignupidResponse404]]
    """

    return (
        await asyncio_detailed(
            event_signup_id=event_signup_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
