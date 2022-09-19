from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.delete_codes_codeid_response_400 import DeleteCodesCodeidResponse400
from ...models.delete_codes_codeid_response_404 import DeleteCodesCodeidResponse404
from ...types import Response


def _get_kwargs(
    code_id: int = 20547,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/codes/{codeId}".format(client.base_url, codeId=code_id)

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
) -> Optional[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = DeleteCodesCodeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = DeleteCodesCodeidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    code_id: int = 20547,
    *,
    client: Client,
) -> Response[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]:
    """/codes/{codeId}

     Use this endpoint to delete an existing Code. Use with caution as this this action is
    *irreversible*.

    Codes can only be deleted if they are not applied to any Entity in any context in which the Code
    exists. *NB*: you may not have access to every context in which the Code exists.


    If the specified Code does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Code does exist but is not deletable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        code_id (int):  Default: 20547.

    Returns:
        Response[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]
    """

    kwargs = _get_kwargs(
        code_id=code_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    code_id: int = 20547,
    *,
    client: Client,
) -> Optional[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]:
    """/codes/{codeId}

     Use this endpoint to delete an existing Code. Use with caution as this this action is
    *irreversible*.

    Codes can only be deleted if they are not applied to any Entity in any context in which the Code
    exists. *NB*: you may not have access to every context in which the Code exists.


    If the specified Code does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Code does exist but is not deletable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        code_id (int):  Default: 20547.

    Returns:
        Response[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]
    """

    return sync_detailed(
        code_id=code_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    code_id: int = 20547,
    *,
    client: Client,
) -> Response[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]:
    """/codes/{codeId}

     Use this endpoint to delete an existing Code. Use with caution as this this action is
    *irreversible*.

    Codes can only be deleted if they are not applied to any Entity in any context in which the Code
    exists. *NB*: you may not have access to every context in which the Code exists.


    If the specified Code does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Code does exist but is not deletable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        code_id (int):  Default: 20547.

    Returns:
        Response[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]
    """

    kwargs = _get_kwargs(
        code_id=code_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    code_id: int = 20547,
    *,
    client: Client,
) -> Optional[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]:
    """/codes/{codeId}

     Use this endpoint to delete an existing Code. Use with caution as this this action is
    *irreversible*.

    Codes can only be deleted if they are not applied to any Entity in any context in which the Code
    exists. *NB*: you may not have access to every context in which the Code exists.


    If the specified Code does not exist, this endpoint will return an error with HTTP Status Code `404
    Not Found`.

    If the specified Code does exist but is not deletable, this endpoint will return an error with HTTP
    Status Code `403 Forbidden`.

    If successful, the endpoint responds with HTTP Status Code `204 No Content` and an empty response
    body.

    Args:
        code_id (int):  Default: 20547.

    Returns:
        Response[Union[Any, DeleteCodesCodeidResponse400, DeleteCodesCodeidResponse404]]
    """

    return (
        await asyncio_detailed(
            code_id=code_id,
            client=client,
        )
    ).parsed
