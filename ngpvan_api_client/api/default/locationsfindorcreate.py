from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.locationsfindorcreate_json_body import LocationsfindorcreateJsonBody
from ...models.locationsfindorcreate_response_400 import LocationsfindorcreateResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: LocationsfindorcreateJsonBody,
) -> Dict[str, Any]:
    url = "{}/locations/findOrCreate".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, LocationsfindorcreateResponse400]]:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == 400:
        response_400 = LocationsfindorcreateResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, LocationsfindorcreateResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: LocationsfindorcreateJsonBody,
) -> Response[Union[Any, LocationsfindorcreateResponse400]]:
    """/locations/findOrCreate

     Similar to the [POST /people/findOrCreate](ref:people#peoplefindorcreate) endpoint, this endpoint
    searches for the given Location. If a Location is found, the existing Location is returned. If a
    Location is not found, a new Location is created.

    This endpoint is useful when synchronizing from a system that does not uniquely identify locations.

    This endpoint parses the address provided, and uses the following criteria to find existing
    locations in US contexts:

    * If a `name` is provided and a ZIP5 can be determined (either provided or discovered based on
    `city` and `stateOrProvince`), and no Street Name can be parsed, a match will be attempted based on
    `name` and ZIP5
    * Then, if a `name` is provided and a ZIP5 cannot be determined and no Street Name can be parsed, a
    match will be attempted based on `name`, `city`, and `stateOrProvince`
    * Then, if a Street Name can be parsed and a ZIP5 can be determined (either provided or discovered
    based on `city` and `stateOrProvince`), a match will be attempted based on Street Number, Street
    Name, Apartment Number, and ZIP5

    Non-US contexts match on exact name and parsed address.

    If successful, the endpoint responds with HTTP Status Code `201 Created` (even if it matched and
    updated an existing Location). It also sets the **Location** header to the
    [location](ref:locationslocationid) of the Location.

    Args:
        json_body (LocationsfindorcreateJsonBody):

    Returns:
        Response[Union[Any, LocationsfindorcreateResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: LocationsfindorcreateJsonBody,
) -> Optional[Union[Any, LocationsfindorcreateResponse400]]:
    """/locations/findOrCreate

     Similar to the [POST /people/findOrCreate](ref:people#peoplefindorcreate) endpoint, this endpoint
    searches for the given Location. If a Location is found, the existing Location is returned. If a
    Location is not found, a new Location is created.

    This endpoint is useful when synchronizing from a system that does not uniquely identify locations.

    This endpoint parses the address provided, and uses the following criteria to find existing
    locations in US contexts:

    * If a `name` is provided and a ZIP5 can be determined (either provided or discovered based on
    `city` and `stateOrProvince`), and no Street Name can be parsed, a match will be attempted based on
    `name` and ZIP5
    * Then, if a `name` is provided and a ZIP5 cannot be determined and no Street Name can be parsed, a
    match will be attempted based on `name`, `city`, and `stateOrProvince`
    * Then, if a Street Name can be parsed and a ZIP5 can be determined (either provided or discovered
    based on `city` and `stateOrProvince`), a match will be attempted based on Street Number, Street
    Name, Apartment Number, and ZIP5

    Non-US contexts match on exact name and parsed address.

    If successful, the endpoint responds with HTTP Status Code `201 Created` (even if it matched and
    updated an existing Location). It also sets the **Location** header to the
    [location](ref:locationslocationid) of the Location.

    Args:
        json_body (LocationsfindorcreateJsonBody):

    Returns:
        Response[Union[Any, LocationsfindorcreateResponse400]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: LocationsfindorcreateJsonBody,
) -> Response[Union[Any, LocationsfindorcreateResponse400]]:
    """/locations/findOrCreate

     Similar to the [POST /people/findOrCreate](ref:people#peoplefindorcreate) endpoint, this endpoint
    searches for the given Location. If a Location is found, the existing Location is returned. If a
    Location is not found, a new Location is created.

    This endpoint is useful when synchronizing from a system that does not uniquely identify locations.

    This endpoint parses the address provided, and uses the following criteria to find existing
    locations in US contexts:

    * If a `name` is provided and a ZIP5 can be determined (either provided or discovered based on
    `city` and `stateOrProvince`), and no Street Name can be parsed, a match will be attempted based on
    `name` and ZIP5
    * Then, if a `name` is provided and a ZIP5 cannot be determined and no Street Name can be parsed, a
    match will be attempted based on `name`, `city`, and `stateOrProvince`
    * Then, if a Street Name can be parsed and a ZIP5 can be determined (either provided or discovered
    based on `city` and `stateOrProvince`), a match will be attempted based on Street Number, Street
    Name, Apartment Number, and ZIP5

    Non-US contexts match on exact name and parsed address.

    If successful, the endpoint responds with HTTP Status Code `201 Created` (even if it matched and
    updated an existing Location). It also sets the **Location** header to the
    [location](ref:locationslocationid) of the Location.

    Args:
        json_body (LocationsfindorcreateJsonBody):

    Returns:
        Response[Union[Any, LocationsfindorcreateResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: LocationsfindorcreateJsonBody,
) -> Optional[Union[Any, LocationsfindorcreateResponse400]]:
    """/locations/findOrCreate

     Similar to the [POST /people/findOrCreate](ref:people#peoplefindorcreate) endpoint, this endpoint
    searches for the given Location. If a Location is found, the existing Location is returned. If a
    Location is not found, a new Location is created.

    This endpoint is useful when synchronizing from a system that does not uniquely identify locations.

    This endpoint parses the address provided, and uses the following criteria to find existing
    locations in US contexts:

    * If a `name` is provided and a ZIP5 can be determined (either provided or discovered based on
    `city` and `stateOrProvince`), and no Street Name can be parsed, a match will be attempted based on
    `name` and ZIP5
    * Then, if a `name` is provided and a ZIP5 cannot be determined and no Street Name can be parsed, a
    match will be attempted based on `name`, `city`, and `stateOrProvince`
    * Then, if a Street Name can be parsed and a ZIP5 can be determined (either provided or discovered
    based on `city` and `stateOrProvince`), a match will be attempted based on Street Number, Street
    Name, Apartment Number, and ZIP5

    Non-US contexts match on exact name and parsed address.

    If successful, the endpoint responds with HTTP Status Code `201 Created` (even if it matched and
    updated an existing Location). It also sets the **Location** header to the
    [location](ref:locationslocationid) of the Location.

    Args:
        json_body (LocationsfindorcreateJsonBody):

    Returns:
        Response[Union[Any, LocationsfindorcreateResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
