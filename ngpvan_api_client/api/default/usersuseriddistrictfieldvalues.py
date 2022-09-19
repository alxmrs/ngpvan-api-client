from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.usersuseriddistrictfieldvalues_response_200 import UsersuseriddistrictfieldvaluesResponse200
from ...models.usersuseriddistrictfieldvalues_response_400 import UsersuseriddistrictfieldvaluesResponse400
from ...types import Response


def _get_kwargs(
    user_id: int = 1234,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{userId}/districtFieldValues".format(client.base_url, userId=user_id)

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
) -> Optional[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]:
    if response.status_code == 200:
        response_200 = UsersuseriddistrictfieldvaluesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = UsersuseriddistrictfieldvaluesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: int = 1234,
    *,
    client: Client,
) -> Response[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]:
    """/users/{userId}/districtFieldValues

     Use this endpoint to retrieve all District Field Values assigned to a user.

    This endpoint returns a standard [User District Field Value Assignment](ref:users#common-models-38).

    Args:
        user_id (int):  Default: 1234.

    Returns:
        Response[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: int = 1234,
    *,
    client: Client,
) -> Optional[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]:
    """/users/{userId}/districtFieldValues

     Use this endpoint to retrieve all District Field Values assigned to a user.

    This endpoint returns a standard [User District Field Value Assignment](ref:users#common-models-38).

    Args:
        user_id (int):  Default: 1234.

    Returns:
        Response[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: int = 1234,
    *,
    client: Client,
) -> Response[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]:
    """/users/{userId}/districtFieldValues

     Use this endpoint to retrieve all District Field Values assigned to a user.

    This endpoint returns a standard [User District Field Value Assignment](ref:users#common-models-38).

    Args:
        user_id (int):  Default: 1234.

    Returns:
        Response[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: int = 1234,
    *,
    client: Client,
) -> Optional[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]:
    """/users/{userId}/districtFieldValues

     Use this endpoint to retrieve all District Field Values assigned to a user.

    This endpoint returns a standard [User District Field Value Assignment](ref:users#common-models-38).

    Args:
        user_id (int):  Default: 1234.

    Returns:
        Response[Union[UsersuseriddistrictfieldvaluesResponse200, UsersuseriddistrictfieldvaluesResponse400]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
