from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.surveyquestionssurveyquestionid_response_200 import SurveyquestionssurveyquestionidResponse200
from ...models.surveyquestionssurveyquestionid_response_400 import SurveyquestionssurveyquestionidResponse400
from ...models.surveyquestionssurveyquestionid_response_404 import SurveyquestionssurveyquestionidResponse404
from ...types import Response


def _get_kwargs(
    survey_question_id: str = "54949",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/surveyQuestions/{surveyQuestionId}".format(client.base_url, surveyQuestionId=survey_question_id)

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
        SurveyquestionssurveyquestionidResponse200,
        SurveyquestionssurveyquestionidResponse400,
        SurveyquestionssurveyquestionidResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = SurveyquestionssurveyquestionidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = SurveyquestionssurveyquestionidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = SurveyquestionssurveyquestionidResponse404.from_dict(response.json())

        return response_404
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[
    Union[
        SurveyquestionssurveyquestionidResponse200,
        SurveyquestionssurveyquestionidResponse400,
        SurveyquestionssurveyquestionidResponse404,
    ]
]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    survey_question_id: str = "54949",
    *,
    client: Client,
) -> Response[
    Union[
        SurveyquestionssurveyquestionidResponse200,
        SurveyquestionssurveyquestionidResponse400,
        SurveyquestionssurveyquestionidResponse404,
    ]
]:
    """/surveyQuestions/{surveyQuestionId}

     Use this endpoint to retrieve information about a specific Survey Question (and its set of Survey
    Responses) available in the current context.

    A standard [Survey Question](ref:survey-questions#common-models-36) object, if found.

    If the specified Survey Question does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        survey_question_id (str):  Default: '54949'.

    Returns:
        Response[Union[SurveyquestionssurveyquestionidResponse200, SurveyquestionssurveyquestionidResponse400, SurveyquestionssurveyquestionidResponse404]]
    """

    kwargs = _get_kwargs(
        survey_question_id=survey_question_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    survey_question_id: str = "54949",
    *,
    client: Client,
) -> Optional[
    Union[
        SurveyquestionssurveyquestionidResponse200,
        SurveyquestionssurveyquestionidResponse400,
        SurveyquestionssurveyquestionidResponse404,
    ]
]:
    """/surveyQuestions/{surveyQuestionId}

     Use this endpoint to retrieve information about a specific Survey Question (and its set of Survey
    Responses) available in the current context.

    A standard [Survey Question](ref:survey-questions#common-models-36) object, if found.

    If the specified Survey Question does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        survey_question_id (str):  Default: '54949'.

    Returns:
        Response[Union[SurveyquestionssurveyquestionidResponse200, SurveyquestionssurveyquestionidResponse400, SurveyquestionssurveyquestionidResponse404]]
    """

    return sync_detailed(
        survey_question_id=survey_question_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    survey_question_id: str = "54949",
    *,
    client: Client,
) -> Response[
    Union[
        SurveyquestionssurveyquestionidResponse200,
        SurveyquestionssurveyquestionidResponse400,
        SurveyquestionssurveyquestionidResponse404,
    ]
]:
    """/surveyQuestions/{surveyQuestionId}

     Use this endpoint to retrieve information about a specific Survey Question (and its set of Survey
    Responses) available in the current context.

    A standard [Survey Question](ref:survey-questions#common-models-36) object, if found.

    If the specified Survey Question does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        survey_question_id (str):  Default: '54949'.

    Returns:
        Response[Union[SurveyquestionssurveyquestionidResponse200, SurveyquestionssurveyquestionidResponse400, SurveyquestionssurveyquestionidResponse404]]
    """

    kwargs = _get_kwargs(
        survey_question_id=survey_question_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    survey_question_id: str = "54949",
    *,
    client: Client,
) -> Optional[
    Union[
        SurveyquestionssurveyquestionidResponse200,
        SurveyquestionssurveyquestionidResponse400,
        SurveyquestionssurveyquestionidResponse404,
    ]
]:
    """/surveyQuestions/{surveyQuestionId}

     Use this endpoint to retrieve information about a specific Survey Question (and its set of Survey
    Responses) available in the current context.

    A standard [Survey Question](ref:survey-questions#common-models-36) object, if found.

    If the specified Survey Question does not exist, this endpoint will return an error with HTTP Status
    Code `404 Not Found`.

    Args:
        survey_question_id (str):  Default: '54949'.

    Returns:
        Response[Union[SurveyquestionssurveyquestionidResponse200, SurveyquestionssurveyquestionidResponse400, SurveyquestionssurveyquestionidResponse404]]
    """

    return (
        await asyncio_detailed(
            survey_question_id=survey_question_id,
            client=client,
        )
    ).parsed
