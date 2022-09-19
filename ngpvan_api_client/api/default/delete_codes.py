from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.delete_codes_json_body import DeleteCodesJsonBody
from ...models.delete_codes_response_200_item import DeleteCodesResponse200Item
from ...models.delete_codes_response_400 import DeleteCodesResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: DeleteCodesJsonBody,
) -> Dict[str, Any]:
    url = "{}/codes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DeleteCodesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = DeleteCodesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: DeleteCodesJsonBody,
) -> Response[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]:
    """/codes

     Use this endpoint to delete a list of existing Codes. Use with caution as this this action is
    *irreversible*.

    Codes can only be deleted if they are not applied to any Entity in any context in which the Code
    exists. *NB*: you may not have access to every context in which the Code exists.


    The endpoint responds with HTTP Status Code `200 OK` and an array of results, one for each code
    deleted or attempted. Each object will contain the ID of the Code, if successfully updated, and any
    warning or error messages for that Code.

    Args:
        json_body (DeleteCodesJsonBody):

    Returns:
        Response[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]
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
    json_body: DeleteCodesJsonBody,
) -> Optional[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]:
    """/codes

     Use this endpoint to delete a list of existing Codes. Use with caution as this this action is
    *irreversible*.

    Codes can only be deleted if they are not applied to any Entity in any context in which the Code
    exists. *NB*: you may not have access to every context in which the Code exists.


    The endpoint responds with HTTP Status Code `200 OK` and an array of results, one for each code
    deleted or attempted. Each object will contain the ID of the Code, if successfully updated, and any
    warning or error messages for that Code.

    Args:
        json_body (DeleteCodesJsonBody):

    Returns:
        Response[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: DeleteCodesJsonBody,
) -> Response[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]:
    """/codes

     Use this endpoint to delete a list of existing Codes. Use with caution as this this action is
    *irreversible*.

    Codes can only be deleted if they are not applied to any Entity in any context in which the Code
    exists. *NB*: you may not have access to every context in which the Code exists.


    The endpoint responds with HTTP Status Code `200 OK` and an array of results, one for each code
    deleted or attempted. Each object will contain the ID of the Code, if successfully updated, and any
    warning or error messages for that Code.

    Args:
        json_body (DeleteCodesJsonBody):

    Returns:
        Response[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]
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
    json_body: DeleteCodesJsonBody,
) -> Optional[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]:
    """/codes

     Use this endpoint to delete a list of existing Codes. Use with caution as this this action is
    *irreversible*.

    Codes can only be deleted if they are not applied to any Entity in any context in which the Code
    exists. *NB*: you may not have access to every context in which the Code exists.


    The endpoint responds with HTTP Status Code `200 OK` and an array of results, one for each code
    deleted or attempted. Each object will contain the ID of the Code, if successfully updated, and any
    warning or error messages for that Code.

    Args:
        json_body (DeleteCodesJsonBody):

    Returns:
        Response[Union[DeleteCodesResponse400, List[DeleteCodesResponse200Item]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
