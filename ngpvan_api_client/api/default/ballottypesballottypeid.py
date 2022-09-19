from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ballottypesballottypeid_response_200 import BallottypesballottypeidResponse200
from ...models.ballottypesballottypeid_response_400 import BallottypesballottypeidResponse400
from ...types import Response


def _get_kwargs(
    ballot_type_id: int = 7,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ballotTypes/{ballotTypeId}".format(client.base_url, ballotTypeId=ballot_type_id)

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
) -> Optional[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]:
    if response.status_code == 200:
        response_200 = BallottypesballottypeidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BallottypesballottypeidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    ballot_type_id: int = 7,
    *,
    client: Client,
) -> Response[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]:
    """/ballotTypes/{ballotTypeId}

     Retrieve ballot type if it is available.

    Args:
        ballot_type_id (int):  Default: 7.

    Returns:
        Response[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]
    """

    kwargs = _get_kwargs(
        ballot_type_id=ballot_type_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    ballot_type_id: int = 7,
    *,
    client: Client,
) -> Optional[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]:
    """/ballotTypes/{ballotTypeId}

     Retrieve ballot type if it is available.

    Args:
        ballot_type_id (int):  Default: 7.

    Returns:
        Response[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]
    """

    return sync_detailed(
        ballot_type_id=ballot_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ballot_type_id: int = 7,
    *,
    client: Client,
) -> Response[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]:
    """/ballotTypes/{ballotTypeId}

     Retrieve ballot type if it is available.

    Args:
        ballot_type_id (int):  Default: 7.

    Returns:
        Response[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]
    """

    kwargs = _get_kwargs(
        ballot_type_id=ballot_type_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    ballot_type_id: int = 7,
    *,
    client: Client,
) -> Optional[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]:
    """/ballotTypes/{ballotTypeId}

     Retrieve ballot type if it is available.

    Args:
        ballot_type_id (int):  Default: 7.

    Returns:
        Response[Union[Any, BallottypesballottypeidResponse200, BallottypesballottypeidResponse400]]
    """

    return (
        await asyncio_detailed(
            ballot_type_id=ballot_type_id,
            client=client,
        )
    ).parsed
