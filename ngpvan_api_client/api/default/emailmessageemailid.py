from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.emailmessageemailid_response_200 import EmailmessageemailidResponse200
from ...models.emailmessageemailid_response_400 import EmailmessageemailidResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    email_id: str = "K3Jy8GbLEeuYiQAVXUPJkg2",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "EmailMessageContentDistributions",
) -> Dict[str, Any]:
    url = "{}/email/message/{emailId}".format(client.base_url, emailId=email_id)

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
) -> Optional[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]:
    if response.status_code == 200:
        response_200 = EmailmessageemailidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = EmailmessageemailidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    email_id: str = "K3Jy8GbLEeuYiQAVXUPJkg2",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "EmailMessageContentDistributions",
) -> Response[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]:
    """/email/message/{emailId}

     Use this endpoint to retrieve information about a specific Email available in the current context.

    Args:
        email_id (str):  Default: 'K3Jy8GbLEeuYiQAVXUPJkg2'.
        expand (Union[Unset, None, str]):  Default: 'EmailMessageContentDistributions'.

    Returns:
        Response[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]
    """

    kwargs = _get_kwargs(
        email_id=email_id,
        client=client,
        expand=expand,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    email_id: str = "K3Jy8GbLEeuYiQAVXUPJkg2",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "EmailMessageContentDistributions",
) -> Optional[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]:
    """/email/message/{emailId}

     Use this endpoint to retrieve information about a specific Email available in the current context.

    Args:
        email_id (str):  Default: 'K3Jy8GbLEeuYiQAVXUPJkg2'.
        expand (Union[Unset, None, str]):  Default: 'EmailMessageContentDistributions'.

    Returns:
        Response[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]
    """

    return sync_detailed(
        email_id=email_id,
        client=client,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    email_id: str = "K3Jy8GbLEeuYiQAVXUPJkg2",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "EmailMessageContentDistributions",
) -> Response[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]:
    """/email/message/{emailId}

     Use this endpoint to retrieve information about a specific Email available in the current context.

    Args:
        email_id (str):  Default: 'K3Jy8GbLEeuYiQAVXUPJkg2'.
        expand (Union[Unset, None, str]):  Default: 'EmailMessageContentDistributions'.

    Returns:
        Response[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]
    """

    kwargs = _get_kwargs(
        email_id=email_id,
        client=client,
        expand=expand,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    email_id: str = "K3Jy8GbLEeuYiQAVXUPJkg2",
    *,
    client: Client,
    expand: Union[Unset, None, str] = "EmailMessageContentDistributions",
) -> Optional[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]:
    """/email/message/{emailId}

     Use this endpoint to retrieve information about a specific Email available in the current context.

    Args:
        email_id (str):  Default: 'K3Jy8GbLEeuYiQAVXUPJkg2'.
        expand (Union[Unset, None, str]):  Default: 'EmailMessageContentDistributions'.

    Returns:
        Response[Union[Any, EmailmessageemailidResponse200, EmailmessageemailidResponse400]]
    """

    return (
        await asyncio_detailed(
            email_id=email_id,
            client=client,
            expand=expand,
        )
    ).parsed
