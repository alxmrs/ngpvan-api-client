from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.scoresscoreid_ok_range_score import ScoresscoreidOKRangeScore
from ...models.scoresscoreid_ok_value_score import ScoresscoreidOKValueScore
from ...models.scoresscoreid_response_400 import ScoresscoreidResponse400
from ...models.scoresscoreid_response_404 import ScoresscoreidResponse404
from ...types import Response


def _get_kwargs(
    score_id: int = 123,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/scores/{scoreId}".format(client.base_url, scoreId=score_id)

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
        ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ScoresscoreidOKRangeScore.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ScoresscoreidOKValueScore.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ScoresscoreidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ScoresscoreidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    score_id: int = 123,
    *,
    client: Client,
) -> Response[
    Union[
        ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]
    ]
]:
    """/scores/{scoreId}

     Retrieve a single range score

    Args:
        score_id (int):  Default: 123.

    Returns:
        Response[Union[ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]]]
    """

    kwargs = _get_kwargs(
        score_id=score_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    score_id: int = 123,
    *,
    client: Client,
) -> Optional[
    Union[
        ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]
    ]
]:
    """/scores/{scoreId}

     Retrieve a single range score

    Args:
        score_id (int):  Default: 123.

    Returns:
        Response[Union[ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]]]
    """

    return sync_detailed(
        score_id=score_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    score_id: int = 123,
    *,
    client: Client,
) -> Response[
    Union[
        ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]
    ]
]:
    """/scores/{scoreId}

     Retrieve a single range score

    Args:
        score_id (int):  Default: 123.

    Returns:
        Response[Union[ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]]]
    """

    kwargs = _get_kwargs(
        score_id=score_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    score_id: int = 123,
    *,
    client: Client,
) -> Optional[
    Union[
        ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]
    ]
]:
    """/scores/{scoreId}

     Retrieve a single range score

    Args:
        score_id (int):  Default: 123.

    Returns:
        Response[Union[ScoresscoreidResponse400, ScoresscoreidResponse404, Union[ScoresscoreidOKRangeScore, ScoresscoreidOKValueScore]]]
    """

    return (
        await asyncio_detailed(
            score_id=score_id,
            client=client,
        )
    ).parsed
