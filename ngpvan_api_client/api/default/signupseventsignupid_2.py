from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.signupseventsignupid_2_response_400 import Signupseventsignupid2Response400
from ...models.signupseventsignupid_2_response_404 import Signupseventsignupid2Response404
from ...types import Response


def _get_kwargs(
    event_signup_id: int = 2423,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/signups/{eventSignupId}".format(client.base_url, eventSignupId=event_signup_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = Signupseventsignupid2Response400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Signupseventsignupid2Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    event_signup_id: int = 2423,
    *,
    client: Client,
) -> Response[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]:
    """/signups/{eventSignupId}

     This endpoint deletes an existing Signup. Use with caution as this this action is irreversible and a
    record of this change is not display in the VAN UI.

    Typically it’s more appropriate to [update](ref:signups#signups-2) an existing Signup with a Status
    of Declined or No Show rather than to delete the record entirely.

    Deleting a Signup does not delete any [canvass responses](ref:people#peoplevanidcanvassresponses)
    associated with actions taken on the Signup.

    If the specified Signup does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        event_signup_id (int):  Default: 2423.

    Returns:
        Response[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]
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
    event_signup_id: int = 2423,
    *,
    client: Client,
) -> Optional[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]:
    """/signups/{eventSignupId}

     This endpoint deletes an existing Signup. Use with caution as this this action is irreversible and a
    record of this change is not display in the VAN UI.

    Typically it’s more appropriate to [update](ref:signups#signups-2) an existing Signup with a Status
    of Declined or No Show rather than to delete the record entirely.

    Deleting a Signup does not delete any [canvass responses](ref:people#peoplevanidcanvassresponses)
    associated with actions taken on the Signup.

    If the specified Signup does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        event_signup_id (int):  Default: 2423.

    Returns:
        Response[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]
    """

    return sync_detailed(
        event_signup_id=event_signup_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_signup_id: int = 2423,
    *,
    client: Client,
) -> Response[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]:
    """/signups/{eventSignupId}

     This endpoint deletes an existing Signup. Use with caution as this this action is irreversible and a
    record of this change is not display in the VAN UI.

    Typically it’s more appropriate to [update](ref:signups#signups-2) an existing Signup with a Status
    of Declined or No Show rather than to delete the record entirely.

    Deleting a Signup does not delete any [canvass responses](ref:people#peoplevanidcanvassresponses)
    associated with actions taken on the Signup.

    If the specified Signup does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        event_signup_id (int):  Default: 2423.

    Returns:
        Response[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]
    """

    kwargs = _get_kwargs(
        event_signup_id=event_signup_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    event_signup_id: int = 2423,
    *,
    client: Client,
) -> Optional[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]:
    """/signups/{eventSignupId}

     This endpoint deletes an existing Signup. Use with caution as this this action is irreversible and a
    record of this change is not display in the VAN UI.

    Typically it’s more appropriate to [update](ref:signups#signups-2) an existing Signup with a Status
    of Declined or No Show rather than to delete the record entirely.

    Deleting a Signup does not delete any [canvass responses](ref:people#peoplevanidcanvassresponses)
    associated with actions taken on the Signup.

    If the specified Signup does not exist, this endpoint will return an error with HTTP Status Code
    `404 Not Found`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        event_signup_id (int):  Default: 2423.

    Returns:
        Response[Union[Any, Signupseventsignupid2Response400, Signupseventsignupid2Response404]]
    """

    return (
        await asyncio_detailed(
            event_signup_id=event_signup_id,
            client=client,
        )
    ).parsed
