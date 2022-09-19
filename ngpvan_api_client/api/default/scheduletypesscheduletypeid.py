from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.scheduletypesscheduletypeid_response_200 import ScheduletypesscheduletypeidResponse200
from ...models.scheduletypesscheduletypeid_response_400 import ScheduletypesscheduletypeidResponse400
from ...models.scheduletypesscheduletypeid_response_404 import ScheduletypesscheduletypeidResponse404
from ...types import Response


def _get_kwargs(
    schedule_type_id: int = 1,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/scheduleTypes/{scheduleTypeId}".format(client.base_url, scheduleTypeId=schedule_type_id)

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
) -> Optional[
    Union[
        ScheduletypesscheduletypeidResponse200,
        ScheduletypesscheduletypeidResponse400,
        ScheduletypesscheduletypeidResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = ScheduletypesscheduletypeidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ScheduletypesscheduletypeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ScheduletypesscheduletypeidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        ScheduletypesscheduletypeidResponse200,
        ScheduletypesscheduletypeidResponse400,
        ScheduletypesscheduletypeidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    schedule_type_id: int = 1,
    *,
    client: Client,
) -> Response[
    Union[
        ScheduletypesscheduletypeidResponse200,
        ScheduletypesscheduletypeidResponse400,
        ScheduletypesscheduletypeidResponse404,
    ]
]:
    """/scheduleTypes/{scheduleTypeId}

     Use this endpoint to retrieve the details of a specific Schedule Type.

    Args:
        schedule_type_id (int):  Default: 1.

    Returns:
        Response[Union[ScheduletypesscheduletypeidResponse200, ScheduletypesscheduletypeidResponse400, ScheduletypesscheduletypeidResponse404]]
    """

    kwargs = _get_kwargs(
        schedule_type_id=schedule_type_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    schedule_type_id: int = 1,
    *,
    client: Client,
) -> Optional[
    Union[
        ScheduletypesscheduletypeidResponse200,
        ScheduletypesscheduletypeidResponse400,
        ScheduletypesscheduletypeidResponse404,
    ]
]:
    """/scheduleTypes/{scheduleTypeId}

     Use this endpoint to retrieve the details of a specific Schedule Type.

    Args:
        schedule_type_id (int):  Default: 1.

    Returns:
        Response[Union[ScheduletypesscheduletypeidResponse200, ScheduletypesscheduletypeidResponse400, ScheduletypesscheduletypeidResponse404]]
    """

    return sync_detailed(
        schedule_type_id=schedule_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    schedule_type_id: int = 1,
    *,
    client: Client,
) -> Response[
    Union[
        ScheduletypesscheduletypeidResponse200,
        ScheduletypesscheduletypeidResponse400,
        ScheduletypesscheduletypeidResponse404,
    ]
]:
    """/scheduleTypes/{scheduleTypeId}

     Use this endpoint to retrieve the details of a specific Schedule Type.

    Args:
        schedule_type_id (int):  Default: 1.

    Returns:
        Response[Union[ScheduletypesscheduletypeidResponse200, ScheduletypesscheduletypeidResponse400, ScheduletypesscheduletypeidResponse404]]
    """

    kwargs = _get_kwargs(
        schedule_type_id=schedule_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    schedule_type_id: int = 1,
    *,
    client: Client,
) -> Optional[
    Union[
        ScheduletypesscheduletypeidResponse200,
        ScheduletypesscheduletypeidResponse400,
        ScheduletypesscheduletypeidResponse404,
    ]
]:
    """/scheduleTypes/{scheduleTypeId}

     Use this endpoint to retrieve the details of a specific Schedule Type.

    Args:
        schedule_type_id (int):  Default: 1.

    Returns:
        Response[Union[ScheduletypesscheduletypeidResponse200, ScheduletypesscheduletypeidResponse400, ScheduletypesscheduletypeidResponse404]]
    """

    return (
        await asyncio_detailed(
            schedule_type_id=schedule_type_id,
            client=client,
        )
    ).parsed
