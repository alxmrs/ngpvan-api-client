from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.disbursementsdisbursementid_response_400 import DisbursementsdisbursementidResponse400
from ...models.disbursementsdisbursementid_response_404 import DisbursementsdisbursementidResponse404
from ...types import Response


def _get_kwargs(
    disbursement_id: int = 4482,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/disbursements/{disbursementId}".format(client.base_url, disbursementId=disbursement_id)

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
) -> Optional[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = DisbursementsdisbursementidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = DisbursementsdisbursementidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    disbursement_id: int = 4482,
    *,
    client: Client,
) -> Response[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]:
    """/disbursements/{disbursementId}

     Retrieve a Disbursement by `disbursementId`

    Args:
        disbursement_id (int):  Default: 4482.

    Returns:
        Response[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]
    """

    kwargs = _get_kwargs(
        disbursement_id=disbursement_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    disbursement_id: int = 4482,
    *,
    client: Client,
) -> Optional[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]:
    """/disbursements/{disbursementId}

     Retrieve a Disbursement by `disbursementId`

    Args:
        disbursement_id (int):  Default: 4482.

    Returns:
        Response[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]
    """

    return sync_detailed(
        disbursement_id=disbursement_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    disbursement_id: int = 4482,
    *,
    client: Client,
) -> Response[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]:
    """/disbursements/{disbursementId}

     Retrieve a Disbursement by `disbursementId`

    Args:
        disbursement_id (int):  Default: 4482.

    Returns:
        Response[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]
    """

    kwargs = _get_kwargs(
        disbursement_id=disbursement_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    disbursement_id: int = 4482,
    *,
    client: Client,
) -> Optional[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]:
    """/disbursements/{disbursementId}

     Retrieve a Disbursement by `disbursementId`

    Args:
        disbursement_id (int):  Default: 4482.

    Returns:
        Response[Union[Any, DisbursementsdisbursementidResponse400, DisbursementsdisbursementidResponse404]]
    """

    return (
        await asyncio_detailed(
            disbursement_id=disbursement_id,
            client=client,
        )
    ).parsed
