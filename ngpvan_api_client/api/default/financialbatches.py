from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.financialbatches_response_200 import FinancialbatchesResponse200
from ...models.financialbatches_response_400 import FinancialbatchesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    search_keyword: Union[Unset, None, str] = "Example",
    include_unassigned: Union[Unset, None, bool] = True,
    include_all_auto_generated: Union[Unset, None, bool] = True,
    include_all_statuses: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/financialBatches".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["searchKeyword"] = search_keyword

    params["includeUnassigned"] = include_unassigned

    params["includeAllAutoGenerated"] = include_all_auto_generated

    params["includeAllStatuses"] = include_all_statuses

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
) -> Optional[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]:
    if response.status_code == 200:
        response_200 = FinancialbatchesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = FinancialbatchesResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    search_keyword: Union[Unset, None, str] = "Example",
    include_unassigned: Union[Unset, None, bool] = True,
    include_all_auto_generated: Union[Unset, None, bool] = True,
    include_all_statuses: Union[Unset, None, bool] = True,
) -> Response[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]:
    """/financialBatches

     Search for Financial Batches, with optional filtering. All query-string filters are optional.

    Args:
        search_keyword (Union[Unset, None, str]):  Default: 'Example'.
        include_unassigned (Union[Unset, None, bool]):  Default: True.
        include_all_auto_generated (Union[Unset, None, bool]):  Default: True.
        include_all_statuses (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        search_keyword=search_keyword,
        include_unassigned=include_unassigned,
        include_all_auto_generated=include_all_auto_generated,
        include_all_statuses=include_all_statuses,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    search_keyword: Union[Unset, None, str] = "Example",
    include_unassigned: Union[Unset, None, bool] = True,
    include_all_auto_generated: Union[Unset, None, bool] = True,
    include_all_statuses: Union[Unset, None, bool] = True,
) -> Optional[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]:
    """/financialBatches

     Search for Financial Batches, with optional filtering. All query-string filters are optional.

    Args:
        search_keyword (Union[Unset, None, str]):  Default: 'Example'.
        include_unassigned (Union[Unset, None, bool]):  Default: True.
        include_all_auto_generated (Union[Unset, None, bool]):  Default: True.
        include_all_statuses (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]
    """

    return sync_detailed(
        client=client,
        search_keyword=search_keyword,
        include_unassigned=include_unassigned,
        include_all_auto_generated=include_all_auto_generated,
        include_all_statuses=include_all_statuses,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    search_keyword: Union[Unset, None, str] = "Example",
    include_unassigned: Union[Unset, None, bool] = True,
    include_all_auto_generated: Union[Unset, None, bool] = True,
    include_all_statuses: Union[Unset, None, bool] = True,
) -> Response[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]:
    """/financialBatches

     Search for Financial Batches, with optional filtering. All query-string filters are optional.

    Args:
        search_keyword (Union[Unset, None, str]):  Default: 'Example'.
        include_unassigned (Union[Unset, None, bool]):  Default: True.
        include_all_auto_generated (Union[Unset, None, bool]):  Default: True.
        include_all_statuses (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        search_keyword=search_keyword,
        include_unassigned=include_unassigned,
        include_all_auto_generated=include_all_auto_generated,
        include_all_statuses=include_all_statuses,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    search_keyword: Union[Unset, None, str] = "Example",
    include_unassigned: Union[Unset, None, bool] = True,
    include_all_auto_generated: Union[Unset, None, bool] = True,
    include_all_statuses: Union[Unset, None, bool] = True,
) -> Optional[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]:
    """/financialBatches

     Search for Financial Batches, with optional filtering. All query-string filters are optional.

    Args:
        search_keyword (Union[Unset, None, str]):  Default: 'Example'.
        include_unassigned (Union[Unset, None, bool]):  Default: True.
        include_all_auto_generated (Union[Unset, None, bool]):  Default: True.
        include_all_statuses (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Union[FinancialbatchesResponse200, FinancialbatchesResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            search_keyword=search_keyword,
            include_unassigned=include_unassigned,
            include_all_auto_generated=include_all_auto_generated,
            include_all_statuses=include_all_statuses,
        )
    ).parsed