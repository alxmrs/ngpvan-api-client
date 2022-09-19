from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.canvassresponsesresultcodes_response_200_item import CanvassresponsesresultcodesResponse200Item
from ...models.canvassresponsesresultcodes_response_400 import CanvassresponsesresultcodesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    input_type_id: Union[Unset, None, int] = 11,
    contact_type_id: Union[Unset, None, int] = 82,
) -> Dict[str, Any]:
    url = "{}/canvassResponses/resultCodes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["inputTypeId"] = input_type_id

    params["contactTypeId"] = contact_type_id

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
) -> Optional[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CanvassresponsesresultcodesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = CanvassresponsesresultcodesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    input_type_id: Union[Unset, None, int] = 11,
    contact_type_id: Union[Unset, None, int] = 82,
) -> Response[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]:
    """/canvassResponses/resultCodes

     Result Codes, or contact dispositions, are the result of a contact attempt. For example, *Not Home*,
    *Wrong Number*, *Moved*, etc. A successful contact interaction yields a Result Code called
    *Canvassed* which is automatically applied when canvass responses are submitted (e.g., when a Survey
    Response is recorded).

    Unsuccessful contact attempts are what Result Codes are all about. This endpoint returns a list of
    those response codes available in the current context. Similar to Contact Types, Result Codes’
    availability can vary by Input Type and/or Contact Type. For example, *Wrong Number* only makes
    sense in the context of a *Call* Contact Type. *Moved* only makes sense in the context of a *Walk*
    Contact Type.

    Args:
        input_type_id (Union[Unset, None, int]):  Default: 11.
        contact_type_id (Union[Unset, None, int]):  Default: 82.

    Returns:
        Response[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]
    """

    kwargs = _get_kwargs(
        client=client,
        input_type_id=input_type_id,
        contact_type_id=contact_type_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    input_type_id: Union[Unset, None, int] = 11,
    contact_type_id: Union[Unset, None, int] = 82,
) -> Optional[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]:
    """/canvassResponses/resultCodes

     Result Codes, or contact dispositions, are the result of a contact attempt. For example, *Not Home*,
    *Wrong Number*, *Moved*, etc. A successful contact interaction yields a Result Code called
    *Canvassed* which is automatically applied when canvass responses are submitted (e.g., when a Survey
    Response is recorded).

    Unsuccessful contact attempts are what Result Codes are all about. This endpoint returns a list of
    those response codes available in the current context. Similar to Contact Types, Result Codes’
    availability can vary by Input Type and/or Contact Type. For example, *Wrong Number* only makes
    sense in the context of a *Call* Contact Type. *Moved* only makes sense in the context of a *Walk*
    Contact Type.

    Args:
        input_type_id (Union[Unset, None, int]):  Default: 11.
        contact_type_id (Union[Unset, None, int]):  Default: 82.

    Returns:
        Response[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]
    """

    return sync_detailed(
        client=client,
        input_type_id=input_type_id,
        contact_type_id=contact_type_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    input_type_id: Union[Unset, None, int] = 11,
    contact_type_id: Union[Unset, None, int] = 82,
) -> Response[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]:
    """/canvassResponses/resultCodes

     Result Codes, or contact dispositions, are the result of a contact attempt. For example, *Not Home*,
    *Wrong Number*, *Moved*, etc. A successful contact interaction yields a Result Code called
    *Canvassed* which is automatically applied when canvass responses are submitted (e.g., when a Survey
    Response is recorded).

    Unsuccessful contact attempts are what Result Codes are all about. This endpoint returns a list of
    those response codes available in the current context. Similar to Contact Types, Result Codes’
    availability can vary by Input Type and/or Contact Type. For example, *Wrong Number* only makes
    sense in the context of a *Call* Contact Type. *Moved* only makes sense in the context of a *Walk*
    Contact Type.

    Args:
        input_type_id (Union[Unset, None, int]):  Default: 11.
        contact_type_id (Union[Unset, None, int]):  Default: 82.

    Returns:
        Response[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]
    """

    kwargs = _get_kwargs(
        client=client,
        input_type_id=input_type_id,
        contact_type_id=contact_type_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    input_type_id: Union[Unset, None, int] = 11,
    contact_type_id: Union[Unset, None, int] = 82,
) -> Optional[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]:
    """/canvassResponses/resultCodes

     Result Codes, or contact dispositions, are the result of a contact attempt. For example, *Not Home*,
    *Wrong Number*, *Moved*, etc. A successful contact interaction yields a Result Code called
    *Canvassed* which is automatically applied when canvass responses are submitted (e.g., when a Survey
    Response is recorded).

    Unsuccessful contact attempts are what Result Codes are all about. This endpoint returns a list of
    those response codes available in the current context. Similar to Contact Types, Result Codes’
    availability can vary by Input Type and/or Contact Type. For example, *Wrong Number* only makes
    sense in the context of a *Call* Contact Type. *Moved* only makes sense in the context of a *Walk*
    Contact Type.

    Args:
        input_type_id (Union[Unset, None, int]):  Default: 11.
        contact_type_id (Union[Unset, None, int]):  Default: 82.

    Returns:
        Response[Union[CanvassresponsesresultcodesResponse400, List[CanvassresponsesresultcodesResponse200Item]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            input_type_id=input_type_id,
            contact_type_id=contact_type_id,
        )
    ).parsed
