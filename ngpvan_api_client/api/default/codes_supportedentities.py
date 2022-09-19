from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.codes_supportedentities_response_400 import CodesSupportedentitiesResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/codes/supportedEntities".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CodesSupportedentitiesResponse400, List[str]]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CodesSupportedentitiesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CodesSupportedentitiesResponse400, List[str]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[CodesSupportedentitiesResponse400, List[str]]]:
    """/codes/supportedEntities

     Retrieve Code Supported Entities

    *Description*

    `ActivistCodes` — Tags can be applied to [Activist Codes](ref:activist-codes) in the VAN UI
    `Contacts` — Contacts are synonymous with [People](ref:people)
    `Events` — Tags can be applied to [Events](ref:events)
    `Locations` — Tags can be applied to [Locations](ref:locations)
    `Organizations` — Tags can be applied to Organizations
    `SurveyQuestions` — Tags can be applied to [Survey Questions](ref:survey-questions) in the VAN UI

    This endpoint does *not* have relevance for Source Codes, as Source Codes are always applicable to a
    fixed list of Entities; see the [Codes Overview](ref:codes#overview-7) for more details.

    Returns:
        Response[Union[CodesSupportedentitiesResponse400, List[str]]]
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
) -> Optional[Union[CodesSupportedentitiesResponse400, List[str]]]:
    """/codes/supportedEntities

     Retrieve Code Supported Entities

    *Description*

    `ActivistCodes` — Tags can be applied to [Activist Codes](ref:activist-codes) in the VAN UI
    `Contacts` — Contacts are synonymous with [People](ref:people)
    `Events` — Tags can be applied to [Events](ref:events)
    `Locations` — Tags can be applied to [Locations](ref:locations)
    `Organizations` — Tags can be applied to Organizations
    `SurveyQuestions` — Tags can be applied to [Survey Questions](ref:survey-questions) in the VAN UI

    This endpoint does *not* have relevance for Source Codes, as Source Codes are always applicable to a
    fixed list of Entities; see the [Codes Overview](ref:codes#overview-7) for more details.

    Returns:
        Response[Union[CodesSupportedentitiesResponse400, List[str]]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[CodesSupportedentitiesResponse400, List[str]]]:
    """/codes/supportedEntities

     Retrieve Code Supported Entities

    *Description*

    `ActivistCodes` — Tags can be applied to [Activist Codes](ref:activist-codes) in the VAN UI
    `Contacts` — Contacts are synonymous with [People](ref:people)
    `Events` — Tags can be applied to [Events](ref:events)
    `Locations` — Tags can be applied to [Locations](ref:locations)
    `Organizations` — Tags can be applied to Organizations
    `SurveyQuestions` — Tags can be applied to [Survey Questions](ref:survey-questions) in the VAN UI

    This endpoint does *not* have relevance for Source Codes, as Source Codes are always applicable to a
    fixed list of Entities; see the [Codes Overview](ref:codes#overview-7) for more details.

    Returns:
        Response[Union[CodesSupportedentitiesResponse400, List[str]]]
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
) -> Optional[Union[CodesSupportedentitiesResponse400, List[str]]]:
    """/codes/supportedEntities

     Retrieve Code Supported Entities

    *Description*

    `ActivistCodes` — Tags can be applied to [Activist Codes](ref:activist-codes) in the VAN UI
    `Contacts` — Contacts are synonymous with [People](ref:people)
    `Events` — Tags can be applied to [Events](ref:events)
    `Locations` — Tags can be applied to [Locations](ref:locations)
    `Organizations` — Tags can be applied to Organizations
    `SurveyQuestions` — Tags can be applied to [Survey Questions](ref:survey-questions) in the VAN UI

    This endpoint does *not* have relevance for Source Codes, as Source Codes are always applicable to a
    fixed list of Entities; see the [Codes Overview](ref:codes#overview-7) for more details.

    Returns:
        Response[Union[CodesSupportedentitiesResponse400, List[str]]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
