from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.canvassresponsesinputtypes_response_200_item import CanvassresponsesinputtypesResponse200Item
from ...models.canvassresponsesinputtypes_response_400 import CanvassresponsesinputtypesResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/canvassResponses/inputTypes".format(client.base_url)

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
) -> Optional[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CanvassresponsesinputtypesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = CanvassresponsesinputtypesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]:
    """/canvassResponses/inputTypes

     Input Types are different ways canvass responses are entered into VAN. For example, responses
    entered via Bulk Upload will use the Input Type of *Bulk*. By default, responses entered via the API
    will use an Input Type of *API*. While most Input Types are common across VAN instances, some
    instances may have custom Input Types. Use this endpoint to retrieve all available Input Types.

    Returns:
        Response[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]:
    """/canvassResponses/inputTypes

     Input Types are different ways canvass responses are entered into VAN. For example, responses
    entered via Bulk Upload will use the Input Type of *Bulk*. By default, responses entered via the API
    will use an Input Type of *API*. While most Input Types are common across VAN instances, some
    instances may have custom Input Types. Use this endpoint to retrieve all available Input Types.

    Returns:
        Response[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]:
    """/canvassResponses/inputTypes

     Input Types are different ways canvass responses are entered into VAN. For example, responses
    entered via Bulk Upload will use the Input Type of *Bulk*. By default, responses entered via the API
    will use an Input Type of *API*. While most Input Types are common across VAN instances, some
    instances may have custom Input Types. Use this endpoint to retrieve all available Input Types.

    Returns:
        Response[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]:
    """/canvassResponses/inputTypes

     Input Types are different ways canvass responses are entered into VAN. For example, responses
    entered via Bulk Upload will use the Input Type of *Bulk*. By default, responses entered via the API
    will use an Input Type of *API*. While most Input Types are common across VAN instances, some
    instances may have custom Input Types. Use this endpoint to retrieve all available Input Types.

    Returns:
        Response[Union[CanvassresponsesinputtypesResponse400, List[CanvassresponsesinputtypesResponse200Item]]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
