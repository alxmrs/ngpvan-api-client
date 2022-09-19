from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.usersuseriddistrictfieldvalues_2_json_body import Usersuseriddistrictfieldvalues2JsonBody
from ...models.usersuseriddistrictfieldvalues_2_response_200 import Usersuseriddistrictfieldvalues2Response200
from ...models.usersuseriddistrictfieldvalues_2_response_400 import Usersuseriddistrictfieldvalues2Response400
from ...types import Response


def _get_kwargs(
    user_id: int = 1234,
    *,
    client: Client,
    json_body: Usersuseriddistrictfieldvalues2JsonBody,
) -> Dict[str, Any]:
    url = "{}/users/{userId}/districtFieldValues".format(client.base_url, userId=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]:
    if response.status_code == 200:
        response_200 = Usersuseriddistrictfieldvalues2Response200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Usersuseriddistrictfieldvalues2Response400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]:
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
    json_body: Usersuseriddistrictfieldvalues2JsonBody,
) -> Response[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]:
    """/users/{userId}/districtFieldValues

     Use this endpoint to completely overwrite the district field values assignments for a user.

    The request is a standard [User District Field Value Assignment](ref:users#common-models-38).

    *Response*

    The response is the full set of district field value assignments for this user, and thus should be
    identical to the district field values in the request.

    Args:
        user_id (int):  Default: 1234.
        json_body (Usersuseriddistrictfieldvalues2JsonBody):

    Returns:
        Response[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
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
    json_body: Usersuseriddistrictfieldvalues2JsonBody,
) -> Optional[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]:
    """/users/{userId}/districtFieldValues

     Use this endpoint to completely overwrite the district field values assignments for a user.

    The request is a standard [User District Field Value Assignment](ref:users#common-models-38).

    *Response*

    The response is the full set of district field value assignments for this user, and thus should be
    identical to the district field values in the request.

    Args:
        user_id (int):  Default: 1234.
        json_body (Usersuseriddistrictfieldvalues2JsonBody):

    Returns:
        Response[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: int = 1234,
    *,
    client: Client,
    json_body: Usersuseriddistrictfieldvalues2JsonBody,
) -> Response[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]:
    """/users/{userId}/districtFieldValues

     Use this endpoint to completely overwrite the district field values assignments for a user.

    The request is a standard [User District Field Value Assignment](ref:users#common-models-38).

    *Response*

    The response is the full set of district field value assignments for this user, and thus should be
    identical to the district field values in the request.

    Args:
        user_id (int):  Default: 1234.
        json_body (Usersuseriddistrictfieldvalues2JsonBody):

    Returns:
        Response[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: int = 1234,
    *,
    client: Client,
    json_body: Usersuseriddistrictfieldvalues2JsonBody,
) -> Optional[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]:
    """/users/{userId}/districtFieldValues

     Use this endpoint to completely overwrite the district field values assignments for a user.

    The request is a standard [User District Field Value Assignment](ref:users#common-models-38).

    *Response*

    The response is the full set of district field value assignments for this user, and thus should be
    identical to the district field values in the request.

    Args:
        user_id (int):  Default: 1234.
        json_body (Usersuseriddistrictfieldvalues2JsonBody):

    Returns:
        Response[Union[Usersuseriddistrictfieldvalues2Response200, Usersuseriddistrictfieldvalues2Response400]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
