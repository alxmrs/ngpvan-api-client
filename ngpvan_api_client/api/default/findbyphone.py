from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.findbyphone_json_body import FindbyphoneJsonBody
from ...models.findbyphone_response_200 import FindbyphoneResponse200
from ...models.findbyphone_response_400 import FindbyphoneResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: FindbyphoneJsonBody,
) -> Dict[str, Any]:
    url = "{}/people/findByPhone".format(client.base_url)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]:
    if response.status_code == 200:
        response_200 = FindbyphoneResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = FindbyphoneResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: FindbyphoneJsonBody,
) -> Response[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]:
    """/people/findByPhone

     Use this endpoint to get the record of an individual if there is exactly one match to the given
    phone number.


    If no matching phone number is found, an HTTP `404 Not Found` response is returned. This same
    response is also returned if more than one matching phone number is found. A successful response is
    only generated when the phone number is found on exactly one contact record.

    Successful requests will return an HTTP `200` response with a JSON body containing information on
    the [matching record](ref:people#match-candidates).

    Args:
        json_body (FindbyphoneJsonBody):

    Returns:
        Response[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]
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
    json_body: FindbyphoneJsonBody,
) -> Optional[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]:
    """/people/findByPhone

     Use this endpoint to get the record of an individual if there is exactly one match to the given
    phone number.


    If no matching phone number is found, an HTTP `404 Not Found` response is returned. This same
    response is also returned if more than one matching phone number is found. A successful response is
    only generated when the phone number is found on exactly one contact record.

    Successful requests will return an HTTP `200` response with a JSON body containing information on
    the [matching record](ref:people#match-candidates).

    Args:
        json_body (FindbyphoneJsonBody):

    Returns:
        Response[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: FindbyphoneJsonBody,
) -> Response[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]:
    """/people/findByPhone

     Use this endpoint to get the record of an individual if there is exactly one match to the given
    phone number.


    If no matching phone number is found, an HTTP `404 Not Found` response is returned. This same
    response is also returned if more than one matching phone number is found. A successful response is
    only generated when the phone number is found on exactly one contact record.

    Successful requests will return an HTTP `200` response with a JSON body containing information on
    the [matching record](ref:people#match-candidates).

    Args:
        json_body (FindbyphoneJsonBody):

    Returns:
        Response[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]
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
    json_body: FindbyphoneJsonBody,
) -> Optional[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]:
    """/people/findByPhone

     Use this endpoint to get the record of an individual if there is exactly one match to the given
    phone number.


    If no matching phone number is found, an HTTP `404 Not Found` response is returned. This same
    response is also returned if more than one matching phone number is found. A successful response is
    only generated when the phone number is found on exactly one contact record.

    Successful requests will return an HTTP `200` response with a JSON body containing information on
    the [matching record](ref:people#match-candidates).

    Args:
        json_body (FindbyphoneJsonBody):

    Returns:
        Response[Union[Any, FindbyphoneResponse200, FindbyphoneResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
