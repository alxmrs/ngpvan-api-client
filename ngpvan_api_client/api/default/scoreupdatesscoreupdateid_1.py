from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.scoreupdatesscoreupdateid_1_json_body import Scoreupdatesscoreupdateid1JsonBody
from ...models.scoreupdatesscoreupdateid_1_response_400 import Scoreupdatesscoreupdateid1Response400
from ...models.scoreupdatesscoreupdateid_1_response_404 import Scoreupdatesscoreupdateid1Response404
from ...types import Response


def _get_kwargs(
    score_update_id: int = 1888,
    *,
    client: Client,
    json_body: Scoreupdatesscoreupdateid1JsonBody,
) -> Dict[str, Any]:
    url = "{}/scoreUpdates/{scoreUpdateId}".format(client.base_url, scoreUpdateId=score_update_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = Scoreupdatesscoreupdateid1Response400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = Scoreupdatesscoreupdateid1Response404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]:
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
    json_body: Scoreupdatesscoreupdateid1JsonBody,
) -> Response[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]:
    """/scoreUpdates/{scoreUpdateId}

     Changes the status of a score (e.g., from `PendingApproval` to `Approved`). Score updates that are
    approved, are applied at off-peak hours.

    Args:
        score_update_id (int):  Default: 1888.
        json_body (Scoreupdatesscoreupdateid1JsonBody):

    Returns:
        Response[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]
    """

    kwargs = _get_kwargs(
        score_update_id=score_update_id,
        client=client,
        json_body=json_body,
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
    json_body: Scoreupdatesscoreupdateid1JsonBody,
) -> Optional[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]:
    """/scoreUpdates/{scoreUpdateId}

     Changes the status of a score (e.g., from `PendingApproval` to `Approved`). Score updates that are
    approved, are applied at off-peak hours.

    Args:
        score_update_id (int):  Default: 1888.
        json_body (Scoreupdatesscoreupdateid1JsonBody):

    Returns:
        Response[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]
    """

    return sync_detailed(
        score_update_id=score_update_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    score_update_id: int = 1888,
    *,
    client: Client,
    json_body: Scoreupdatesscoreupdateid1JsonBody,
) -> Response[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]:
    """/scoreUpdates/{scoreUpdateId}

     Changes the status of a score (e.g., from `PendingApproval` to `Approved`). Score updates that are
    approved, are applied at off-peak hours.

    Args:
        score_update_id (int):  Default: 1888.
        json_body (Scoreupdatesscoreupdateid1JsonBody):

    Returns:
        Response[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]
    """

    kwargs = _get_kwargs(
        score_update_id=score_update_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    score_update_id: int = 1888,
    *,
    client: Client,
    json_body: Scoreupdatesscoreupdateid1JsonBody,
) -> Optional[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]:
    """/scoreUpdates/{scoreUpdateId}

     Changes the status of a score (e.g., from `PendingApproval` to `Approved`). Score updates that are
    approved, are applied at off-peak hours.

    Args:
        score_update_id (int):  Default: 1888.
        json_body (Scoreupdatesscoreupdateid1JsonBody):

    Returns:
        Response[Union[Any, Scoreupdatesscoreupdateid1Response400, Scoreupdatesscoreupdateid1Response404]]
    """

    return (
        await asyncio_detailed(
            score_update_id=score_update_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
