from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.scoreupdatesscoreupdateid_response_400 import ScoreupdatesscoreupdateidResponse400
from ...models.scoreupdatesscoreupdateid_response_404 import ScoreupdatesscoreupdateidResponse404
from ...types import Response


def _get_kwargs(
    score_update_id: int = 1888,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/scoreUpdates/{scoreUpdateId}".format(client.base_url, scoreUpdateId=score_update_id)

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
) -> Optional[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = ScoreupdatesscoreupdateidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ScoreupdatesscoreupdateidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    score_update_id: int = 1888,
    *,
    client: Client,
) -> Response[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]:
    """/scoreUpdates/{scoreUpdateId}

     Retrieve a single score update

    Args:
        score_update_id (int):  Default: 1888.

    Returns:
        Response[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]
    """

    kwargs = _get_kwargs(
        score_update_id=score_update_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    score_update_id: int = 1888,
    *,
    client: Client,
) -> Optional[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]:
    """/scoreUpdates/{scoreUpdateId}

     Retrieve a single score update

    Args:
        score_update_id (int):  Default: 1888.

    Returns:
        Response[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]
    """

    return sync_detailed(
        score_update_id=score_update_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    score_update_id: int = 1888,
    *,
    client: Client,
) -> Response[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]:
    """/scoreUpdates/{scoreUpdateId}

     Retrieve a single score update

    Args:
        score_update_id (int):  Default: 1888.

    Returns:
        Response[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]
    """

    kwargs = _get_kwargs(
        score_update_id=score_update_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    score_update_id: int = 1888,
    *,
    client: Client,
) -> Optional[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]:
    """/scoreUpdates/{scoreUpdateId}

     Retrieve a single score update

    Args:
        score_update_id (int):  Default: 1888.

    Returns:
        Response[Union[Any, ScoreupdatesscoreupdateidResponse400, ScoreupdatesscoreupdateidResponse404]]
    """

    return (
        await asyncio_detailed(
            score_update_id=score_update_id,
            client=client,
        )
    ).parsed
