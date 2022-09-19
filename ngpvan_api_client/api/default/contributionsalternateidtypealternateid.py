from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contributionsalternateidtypealternateid_response_400 import (
    ContributionsalternateidtypealternateidResponse400,
)
from ...models.contributionsalternateidtypealternateid_response_404 import (
    ContributionsalternateidtypealternateidResponse404,
)
from ...types import Response


def _get_kwargs(
    alternate_id_type: str = "onlineReferenceNumber",
    alternate_id: str = "123",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/contributions/{alternateIdType}:{alternateId}".format(
        client.base_url, alternateIdType=alternate_id_type, alternateId=alternate_id
    )

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
    Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]
]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = ContributionsalternateidtypealternateidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ContributionsalternateidtypealternateidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    alternate_id_type: str = "onlineReferenceNumber",
    alternate_id: str = "123",
    *,
    client: Client,
) -> Response[
    Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]
]:
    """/contributions/{alternateIdType}:{alternateId}

     Retrieve a Contribution record by an Alternate ID. For example
    `/contributions/onlineReferenceNumber:12345` would retrieve a contribution whose Online Reference
    Number is 12345.

    If the specified Contribution does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        alternate_id_type (str):  Default: 'onlineReferenceNumber'.
        alternate_id (str):  Default: '123'.

    Returns:
        Response[Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]]
    """

    kwargs = _get_kwargs(
        alternate_id_type=alternate_id_type,
        alternate_id=alternate_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    alternate_id_type: str = "onlineReferenceNumber",
    alternate_id: str = "123",
    *,
    client: Client,
) -> Optional[
    Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]
]:
    """/contributions/{alternateIdType}:{alternateId}

     Retrieve a Contribution record by an Alternate ID. For example
    `/contributions/onlineReferenceNumber:12345` would retrieve a contribution whose Online Reference
    Number is 12345.

    If the specified Contribution does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        alternate_id_type (str):  Default: 'onlineReferenceNumber'.
        alternate_id (str):  Default: '123'.

    Returns:
        Response[Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]]
    """

    return sync_detailed(
        alternate_id_type=alternate_id_type,
        alternate_id=alternate_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alternate_id_type: str = "onlineReferenceNumber",
    alternate_id: str = "123",
    *,
    client: Client,
) -> Response[
    Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]
]:
    """/contributions/{alternateIdType}:{alternateId}

     Retrieve a Contribution record by an Alternate ID. For example
    `/contributions/onlineReferenceNumber:12345` would retrieve a contribution whose Online Reference
    Number is 12345.

    If the specified Contribution does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        alternate_id_type (str):  Default: 'onlineReferenceNumber'.
        alternate_id (str):  Default: '123'.

    Returns:
        Response[Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]]
    """

    kwargs = _get_kwargs(
        alternate_id_type=alternate_id_type,
        alternate_id=alternate_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    alternate_id_type: str = "onlineReferenceNumber",
    alternate_id: str = "123",
    *,
    client: Client,
) -> Optional[
    Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]
]:
    """/contributions/{alternateIdType}:{alternateId}

     Retrieve a Contribution record by an Alternate ID. For example
    `/contributions/onlineReferenceNumber:12345` would retrieve a contribution whose Online Reference
    Number is 12345.

    If the specified Contribution does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        alternate_id_type (str):  Default: 'onlineReferenceNumber'.
        alternate_id (str):  Default: '123'.

    Returns:
        Response[Union[Any, ContributionsalternateidtypealternateidResponse400, ContributionsalternateidtypealternateidResponse404]]
    """

    return (
        await asyncio_detailed(
            alternate_id_type=alternate_id_type,
            alternate_id=alternate_id,
            client=client,
        )
    ).parsed
