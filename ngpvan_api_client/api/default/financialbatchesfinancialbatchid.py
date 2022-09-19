from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.financialbatchesfinancialbatchid_response_200 import FinancialbatchesfinancialbatchidResponse200
from ...models.financialbatchesfinancialbatchid_response_400 import FinancialbatchesfinancialbatchidResponse400
from ...models.financialbatchesfinancialbatchid_response_404 import FinancialbatchesfinancialbatchidResponse404
from ...types import Response


def _get_kwargs(
    financial_batch_id: int = 825,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/financialBatches/{financialBatchId}".format(client.base_url, financialBatchId=financial_batch_id)

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
        FinancialbatchesfinancialbatchidResponse200,
        FinancialbatchesfinancialbatchidResponse400,
        FinancialbatchesfinancialbatchidResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = FinancialbatchesfinancialbatchidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = FinancialbatchesfinancialbatchidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = FinancialbatchesfinancialbatchidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        FinancialbatchesfinancialbatchidResponse200,
        FinancialbatchesfinancialbatchidResponse400,
        FinancialbatchesfinancialbatchidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    financial_batch_id: int = 825,
    *,
    client: Client,
) -> Response[
    Union[
        FinancialbatchesfinancialbatchidResponse200,
        FinancialbatchesfinancialbatchidResponse400,
        FinancialbatchesfinancialbatchidResponse404,
    ]
]:
    """/financialBatches/{financialBatchId}

     Retrieve a Financial Batch by financialBatchId.

    Args:
        financial_batch_id (int):  Default: 825.

    Returns:
        Response[Union[FinancialbatchesfinancialbatchidResponse200, FinancialbatchesfinancialbatchidResponse400, FinancialbatchesfinancialbatchidResponse404]]
    """

    kwargs = _get_kwargs(
        financial_batch_id=financial_batch_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    financial_batch_id: int = 825,
    *,
    client: Client,
) -> Optional[
    Union[
        FinancialbatchesfinancialbatchidResponse200,
        FinancialbatchesfinancialbatchidResponse400,
        FinancialbatchesfinancialbatchidResponse404,
    ]
]:
    """/financialBatches/{financialBatchId}

     Retrieve a Financial Batch by financialBatchId.

    Args:
        financial_batch_id (int):  Default: 825.

    Returns:
        Response[Union[FinancialbatchesfinancialbatchidResponse200, FinancialbatchesfinancialbatchidResponse400, FinancialbatchesfinancialbatchidResponse404]]
    """

    return sync_detailed(
        financial_batch_id=financial_batch_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    financial_batch_id: int = 825,
    *,
    client: Client,
) -> Response[
    Union[
        FinancialbatchesfinancialbatchidResponse200,
        FinancialbatchesfinancialbatchidResponse400,
        FinancialbatchesfinancialbatchidResponse404,
    ]
]:
    """/financialBatches/{financialBatchId}

     Retrieve a Financial Batch by financialBatchId.

    Args:
        financial_batch_id (int):  Default: 825.

    Returns:
        Response[Union[FinancialbatchesfinancialbatchidResponse200, FinancialbatchesfinancialbatchidResponse400, FinancialbatchesfinancialbatchidResponse404]]
    """

    kwargs = _get_kwargs(
        financial_batch_id=financial_batch_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    financial_batch_id: int = 825,
    *,
    client: Client,
) -> Optional[
    Union[
        FinancialbatchesfinancialbatchidResponse200,
        FinancialbatchesfinancialbatchidResponse400,
        FinancialbatchesfinancialbatchidResponse404,
    ]
]:
    """/financialBatches/{financialBatchId}

     Retrieve a Financial Batch by financialBatchId.

    Args:
        financial_batch_id (int):  Default: 825.

    Returns:
        Response[Union[FinancialbatchesfinancialbatchidResponse200, FinancialbatchesfinancialbatchidResponse400, FinancialbatchesfinancialbatchidResponse404]]
    """

    return (
        await asyncio_detailed(
            financial_batch_id=financial_batch_id,
            client=client,
        )
    ).parsed
