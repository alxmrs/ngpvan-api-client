from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.emailmessages_response_200 import EmailmessagesResponse200
from ...models.emailmessages_response_400 import EmailmessagesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    orderby: Union[Unset, None, str] = "dateModified asc",
) -> Dict[str, Any]:
    url = "{}/email/messages".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$orderby"] = orderby

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[EmailmessagesResponse200, EmailmessagesResponse400]]:
    if response.status_code == 200:
        response_200 = EmailmessagesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = EmailmessagesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[EmailmessagesResponse200, EmailmessagesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    orderby: Union[Unset, None, str] = "dateModified asc",
) -> Response[Union[EmailmessagesResponse200, EmailmessagesResponse400]]:
    """/email/messages

     Use this endpoint to retrieve all emails that are available in the current context.

    The only valid `orderby` property is: `dateModified`.

    This endpoint responds with an array of standard [Email](ref:email) objects.

    Args:
        orderby (Union[Unset, None, str]):  Default: 'dateModified asc'.

    Returns:
        Response[Union[EmailmessagesResponse200, EmailmessagesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        orderby=orderby,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    orderby: Union[Unset, None, str] = "dateModified asc",
) -> Optional[Union[EmailmessagesResponse200, EmailmessagesResponse400]]:
    """/email/messages

     Use this endpoint to retrieve all emails that are available in the current context.

    The only valid `orderby` property is: `dateModified`.

    This endpoint responds with an array of standard [Email](ref:email) objects.

    Args:
        orderby (Union[Unset, None, str]):  Default: 'dateModified asc'.

    Returns:
        Response[Union[EmailmessagesResponse200, EmailmessagesResponse400]]
    """

    return sync_detailed(
        client=client,
        orderby=orderby,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    orderby: Union[Unset, None, str] = "dateModified asc",
) -> Response[Union[EmailmessagesResponse200, EmailmessagesResponse400]]:
    """/email/messages

     Use this endpoint to retrieve all emails that are available in the current context.

    The only valid `orderby` property is: `dateModified`.

    This endpoint responds with an array of standard [Email](ref:email) objects.

    Args:
        orderby (Union[Unset, None, str]):  Default: 'dateModified asc'.

    Returns:
        Response[Union[EmailmessagesResponse200, EmailmessagesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        orderby=orderby,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    orderby: Union[Unset, None, str] = "dateModified asc",
) -> Optional[Union[EmailmessagesResponse200, EmailmessagesResponse400]]:
    """/email/messages

     Use this endpoint to retrieve all emails that are available in the current context.

    The only valid `orderby` property is: `dateModified`.

    This endpoint responds with an array of standard [Email](ref:email) objects.

    Args:
        orderby (Union[Unset, None, str]):  Default: 'dateModified asc'.

    Returns:
        Response[Union[EmailmessagesResponse200, EmailmessagesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            orderby=orderby,
        )
    ).parsed
