from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.surveyquestions_response_200 import SurveyquestionsResponse200
from ...models.surveyquestions_response_400 import SurveyquestionsResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active,Archived",
    name: Union[Unset, None, str] = "John",
    type: Union[Unset, None, str] = "Candidate",
    question: Union[Unset, None, str] = "Will you vote for John Kerry in the upcoming Senate race?",
    cycle: Union[Unset, None, int] = 2020,
    top: Union[Unset, None, int] = 40,
) -> Dict[str, Any]:
    url = "{}/surveyQuestions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["statuses"] = statuses

    params["name"] = name

    params["type"] = type

    params["question"] = question

    params["cycle"] = cycle

    params["$top"] = top

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
) -> Optional[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]:
    if response.status_code == 200:
        response_200 = SurveyquestionsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = SurveyquestionsResponse400.from_dict(response.json())

        return response_400
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active,Archived",
    name: Union[Unset, None, str] = "John",
    type: Union[Unset, None, str] = "Candidate",
    question: Union[Unset, None, str] = "Will you vote for John Kerry in the upcoming Senate race?",
    cycle: Union[Unset, None, int] = 2020,
    top: Union[Unset, None, int] = 40,
) -> Response[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]:
    """/surveyQuestions

     Use this endpoint to retrieve all Survey Questions that are available in the current context.

    Args:
        statuses (Union[Unset, None, str]):  Default: 'Active,Archived'.
        name (Union[Unset, None, str]):  Default: 'John'.
        type (Union[Unset, None, str]):  Default: 'Candidate'.
        question (Union[Unset, None, str]):  Default: 'Will you vote for John Kerry in the
            upcoming Senate race?'.
        cycle (Union[Unset, None, int]):  Default: 2020.
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        statuses=statuses,
        name=name,
        type=type,
        question=question,
        cycle=cycle,
        top=top,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active,Archived",
    name: Union[Unset, None, str] = "John",
    type: Union[Unset, None, str] = "Candidate",
    question: Union[Unset, None, str] = "Will you vote for John Kerry in the upcoming Senate race?",
    cycle: Union[Unset, None, int] = 2020,
    top: Union[Unset, None, int] = 40,
) -> Optional[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]:
    """/surveyQuestions

     Use this endpoint to retrieve all Survey Questions that are available in the current context.

    Args:
        statuses (Union[Unset, None, str]):  Default: 'Active,Archived'.
        name (Union[Unset, None, str]):  Default: 'John'.
        type (Union[Unset, None, str]):  Default: 'Candidate'.
        question (Union[Unset, None, str]):  Default: 'Will you vote for John Kerry in the
            upcoming Senate race?'.
        cycle (Union[Unset, None, int]):  Default: 2020.
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]
    """

    return sync_detailed(
        client=client,
        statuses=statuses,
        name=name,
        type=type,
        question=question,
        cycle=cycle,
        top=top,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active,Archived",
    name: Union[Unset, None, str] = "John",
    type: Union[Unset, None, str] = "Candidate",
    question: Union[Unset, None, str] = "Will you vote for John Kerry in the upcoming Senate race?",
    cycle: Union[Unset, None, int] = 2020,
    top: Union[Unset, None, int] = 40,
) -> Response[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]:
    """/surveyQuestions

     Use this endpoint to retrieve all Survey Questions that are available in the current context.

    Args:
        statuses (Union[Unset, None, str]):  Default: 'Active,Archived'.
        name (Union[Unset, None, str]):  Default: 'John'.
        type (Union[Unset, None, str]):  Default: 'Candidate'.
        question (Union[Unset, None, str]):  Default: 'Will you vote for John Kerry in the
            upcoming Senate race?'.
        cycle (Union[Unset, None, int]):  Default: 2020.
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        statuses=statuses,
        name=name,
        type=type,
        question=question,
        cycle=cycle,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    statuses: Union[Unset, None, str] = "Active,Archived",
    name: Union[Unset, None, str] = "John",
    type: Union[Unset, None, str] = "Candidate",
    question: Union[Unset, None, str] = "Will you vote for John Kerry in the upcoming Senate race?",
    cycle: Union[Unset, None, int] = 2020,
    top: Union[Unset, None, int] = 40,
) -> Optional[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]:
    """/surveyQuestions

     Use this endpoint to retrieve all Survey Questions that are available in the current context.

    Args:
        statuses (Union[Unset, None, str]):  Default: 'Active,Archived'.
        name (Union[Unset, None, str]):  Default: 'John'.
        type (Union[Unset, None, str]):  Default: 'Candidate'.
        question (Union[Unset, None, str]):  Default: 'Will you vote for John Kerry in the
            upcoming Senate race?'.
        cycle (Union[Unset, None, int]):  Default: 2020.
        top (Union[Unset, None, int]):  Default: 40.

    Returns:
        Response[Union[SurveyquestionsResponse200, SurveyquestionsResponse400]]
    """

    return (
        await asyncio_detailed(
            client=client,
            statuses=statuses,
            name=name,
            type=type,
            question=question,
            cycle=cycle,
            top=top,
        )
    ).parsed
