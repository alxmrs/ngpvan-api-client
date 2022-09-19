from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.signups_2_json_body import Signups2JsonBody
from ...models.signups_2_response_201 import Signups2Response201
from ...models.signups_2_response_400 import Signups2Response400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Signups2JsonBody,
) -> Dict[str, Any]:
    url = "{}/signups".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Signups2Response201, Signups2Response400]]:
    if response.status_code == 201:
        response_201 = Signups2Response201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = Signups2Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Signups2Response201, Signups2Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Signups2JsonBody,
) -> Response[Union[Signups2Response201, Signups2Response400]]:
    """/signups

     Use this endpoint to record a Person’s participation at an [Event](ref:events). Because it’s not
    easy to know whether a Person is already signed up for an Event, this endpoint will create a new
    Signup only if a Signup with the same Person, Event, Role, and Shift does not already exist. If a
    Signup does exist, it will override the existing Signup’s Status, Start Time, End Time, and (if
    specified) Location. A record of this change is displayed in the VAN UI.

    When a Signup is created or updated, a canvass response is generated to represent the signup
    interaction. The *Input Type* is *API*, the *Date Canvassed* is the current date, the *Canvasser* is
    the API user associated with the current context, and the *Result Code* corresponds to a result most
    appropriate for the given Status (e.g., *Scheduled* → *Canvassed*). Consult the VAN UI for a
    detailed mapping.

    This endpoint accepts a standard [Signup](ref:signups#common-models-33) object with simple types and
    no read-only values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created` (even if it matched and
    updated an existing Signup) and the integer ID of the created Signup in the response body. It also
    sets the **Location** header to the [location](ref:signupseventsignupid-1) of the newly created
    Signup.

    Args:
        json_body (Signups2JsonBody):

    Returns:
        Response[Union[Signups2Response201, Signups2Response400]]
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
    json_body: Signups2JsonBody,
) -> Optional[Union[Signups2Response201, Signups2Response400]]:
    """/signups

     Use this endpoint to record a Person’s participation at an [Event](ref:events). Because it’s not
    easy to know whether a Person is already signed up for an Event, this endpoint will create a new
    Signup only if a Signup with the same Person, Event, Role, and Shift does not already exist. If a
    Signup does exist, it will override the existing Signup’s Status, Start Time, End Time, and (if
    specified) Location. A record of this change is displayed in the VAN UI.

    When a Signup is created or updated, a canvass response is generated to represent the signup
    interaction. The *Input Type* is *API*, the *Date Canvassed* is the current date, the *Canvasser* is
    the API user associated with the current context, and the *Result Code* corresponds to a result most
    appropriate for the given Status (e.g., *Scheduled* → *Canvassed*). Consult the VAN UI for a
    detailed mapping.

    This endpoint accepts a standard [Signup](ref:signups#common-models-33) object with simple types and
    no read-only values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created` (even if it matched and
    updated an existing Signup) and the integer ID of the created Signup in the response body. It also
    sets the **Location** header to the [location](ref:signupseventsignupid-1) of the newly created
    Signup.

    Args:
        json_body (Signups2JsonBody):

    Returns:
        Response[Union[Signups2Response201, Signups2Response400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Signups2JsonBody,
) -> Response[Union[Signups2Response201, Signups2Response400]]:
    """/signups

     Use this endpoint to record a Person’s participation at an [Event](ref:events). Because it’s not
    easy to know whether a Person is already signed up for an Event, this endpoint will create a new
    Signup only if a Signup with the same Person, Event, Role, and Shift does not already exist. If a
    Signup does exist, it will override the existing Signup’s Status, Start Time, End Time, and (if
    specified) Location. A record of this change is displayed in the VAN UI.

    When a Signup is created or updated, a canvass response is generated to represent the signup
    interaction. The *Input Type* is *API*, the *Date Canvassed* is the current date, the *Canvasser* is
    the API user associated with the current context, and the *Result Code* corresponds to a result most
    appropriate for the given Status (e.g., *Scheduled* → *Canvassed*). Consult the VAN UI for a
    detailed mapping.

    This endpoint accepts a standard [Signup](ref:signups#common-models-33) object with simple types and
    no read-only values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created` (even if it matched and
    updated an existing Signup) and the integer ID of the created Signup in the response body. It also
    sets the **Location** header to the [location](ref:signupseventsignupid-1) of the newly created
    Signup.

    Args:
        json_body (Signups2JsonBody):

    Returns:
        Response[Union[Signups2Response201, Signups2Response400]]
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
    json_body: Signups2JsonBody,
) -> Optional[Union[Signups2Response201, Signups2Response400]]:
    """/signups

     Use this endpoint to record a Person’s participation at an [Event](ref:events). Because it’s not
    easy to know whether a Person is already signed up for an Event, this endpoint will create a new
    Signup only if a Signup with the same Person, Event, Role, and Shift does not already exist. If a
    Signup does exist, it will override the existing Signup’s Status, Start Time, End Time, and (if
    specified) Location. A record of this change is displayed in the VAN UI.

    When a Signup is created or updated, a canvass response is generated to represent the signup
    interaction. The *Input Type* is *API*, the *Date Canvassed* is the current date, the *Canvasser* is
    the API user associated with the current context, and the *Result Code* corresponds to a result most
    appropriate for the given Status (e.g., *Scheduled* → *Canvassed*). Consult the VAN UI for a
    detailed mapping.

    This endpoint accepts a standard [Signup](ref:signups#common-models-33) object with simple types and
    no read-only values specified.

    If successful, the endpoint responds with HTTP Status Code `201 Created` (even if it matched and
    updated an existing Signup) and the integer ID of the created Signup in the response body. It also
    sets the **Location** header to the [location](ref:signupseventsignupid-1) of the newly created
    Signup.

    Args:
        json_body (Signups2JsonBody):

    Returns:
        Response[Union[Signups2Response201, Signups2Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
