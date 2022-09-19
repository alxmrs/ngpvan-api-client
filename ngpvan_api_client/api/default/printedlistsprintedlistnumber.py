from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.printedlistsprintedlistnumber_response_400 import PrintedlistsprintedlistnumberResponse400
from ...models.printedlistsprintedlistnumber_response_404 import PrintedlistsprintedlistnumberResponse404
from ...types import Response


def _get_kwargs(
    printed_list_number: str = "35536742-78261",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/printedLists/{printedListNumber}".format(client.base_url, printedListNumber=printed_list_number)

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
) -> Optional[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]:
    if response.status_code == 400:
        response_400 = PrintedlistsprintedlistnumberResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = PrintedlistsprintedlistnumberResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    printed_list_number: str = "35536742-78261",
    *,
    client: Client,
) -> Response[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]:
    """/printedLists/{printedListNumber}

     Use this endpoint to get full details for a printed list.

    Args:
        printed_list_number (str):  Default: '35536742-78261'.

    Returns:
        Response[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]
    """

    kwargs = _get_kwargs(
        printed_list_number=printed_list_number,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    printed_list_number: str = "35536742-78261",
    *,
    client: Client,
) -> Optional[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]:
    """/printedLists/{printedListNumber}

     Use this endpoint to get full details for a printed list.

    Args:
        printed_list_number (str):  Default: '35536742-78261'.

    Returns:
        Response[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]
    """

    return sync_detailed(
        printed_list_number=printed_list_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    printed_list_number: str = "35536742-78261",
    *,
    client: Client,
) -> Response[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]:
    """/printedLists/{printedListNumber}

     Use this endpoint to get full details for a printed list.

    Args:
        printed_list_number (str):  Default: '35536742-78261'.

    Returns:
        Response[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]
    """

    kwargs = _get_kwargs(
        printed_list_number=printed_list_number,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    printed_list_number: str = "35536742-78261",
    *,
    client: Client,
) -> Optional[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]:
    """/printedLists/{printedListNumber}

     Use this endpoint to get full details for a printed list.

    Args:
        printed_list_number (str):  Default: '35536742-78261'.

    Returns:
        Response[Union[PrintedlistsprintedlistnumberResponse400, PrintedlistsprintedlistnumberResponse404]]
    """

    return (
        await asyncio_detailed(
            printed_list_number=printed_list_number,
            client=client,
        )
    ).parsed
