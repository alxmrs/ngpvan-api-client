from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contributions_1_json_body import Contributions1JsonBody
from ...models.contributions_1_response_400 import Contributions1Response400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Contributions1JsonBody,
) -> Dict[str, Any]:
    url = "{}/contributions".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Contributions1Response400]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 400:
        response_400 = Contributions1Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Contributions1Response400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Contributions1JsonBody,
) -> Response[Union[Any, Contributions1Response400]]:
    """/contributions

     Use this endpoint to create a new contribution with the properties provided in the request body.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Contribution in the response body.

    If any of the specified ids (`vanId`, `pledgeId`, `codeId`, or `extendedSourceCodeId`) are not
    accessible in the current context (e.g., the associated api user does not have access to the
    person), the response will be considered invalid.

    Args:
        json_body (Contributions1JsonBody):

    Returns:
        Response[Union[Any, Contributions1Response400]]
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
    json_body: Contributions1JsonBody,
) -> Optional[Union[Any, Contributions1Response400]]:
    """/contributions

     Use this endpoint to create a new contribution with the properties provided in the request body.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Contribution in the response body.

    If any of the specified ids (`vanId`, `pledgeId`, `codeId`, or `extendedSourceCodeId`) are not
    accessible in the current context (e.g., the associated api user does not have access to the
    person), the response will be considered invalid.

    Args:
        json_body (Contributions1JsonBody):

    Returns:
        Response[Union[Any, Contributions1Response400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Contributions1JsonBody,
) -> Response[Union[Any, Contributions1Response400]]:
    """/contributions

     Use this endpoint to create a new contribution with the properties provided in the request body.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Contribution in the response body.

    If any of the specified ids (`vanId`, `pledgeId`, `codeId`, or `extendedSourceCodeId`) are not
    accessible in the current context (e.g., the associated api user does not have access to the
    person), the response will be considered invalid.

    Args:
        json_body (Contributions1JsonBody):

    Returns:
        Response[Union[Any, Contributions1Response400]]
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
    json_body: Contributions1JsonBody,
) -> Optional[Union[Any, Contributions1Response400]]:
    """/contributions

     Use this endpoint to create a new contribution with the properties provided in the request body.

    If successful, the endpoint responds with HTTP Status Code `201 Created` and the integer ID of the
    created Contribution in the response body.

    If any of the specified ids (`vanId`, `pledgeId`, `codeId`, or `extendedSourceCodeId`) are not
    accessible in the current context (e.g., the associated api user does not have access to the
    person), the response will be considered invalid.

    Args:
        json_body (Contributions1JsonBody):

    Returns:
        Response[Union[Any, Contributions1Response400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
