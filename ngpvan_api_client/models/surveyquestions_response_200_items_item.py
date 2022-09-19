from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.surveyquestions_response_200_items_item_responses_item import (
    SurveyquestionsResponse200ItemsItemResponsesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SurveyquestionsResponse200ItemsItem")


@attr.s(auto_attribs=True)
class SurveyquestionsResponse200ItemsItem:
    """
    Attributes:
        survey_question_id (Union[Unset, int]):  Example: 54945.
        type (Union[Unset, str]):  Example: Candidate.
        cycle (Union[Unset, int]):  Example: 2010.
        name (Union[Unset, str]):  Example: John Kerry senate.
        medium_name (Union[Unset, str]):  Example: Kerry.
        short_name (Union[Unset, str]):  Example: Kerr.
        script_question (Union[Unset, str]):  Example: Will you vote for John Kerry in the upcoming Senate race?.
        status (Union[Unset, str]):  Example: Archived.
        responses (Union[Unset, List[SurveyquestionsResponse200ItemsItemResponsesItem]]):
    """

    survey_question_id: Union[Unset, int] = 0
    type: Union[Unset, str] = UNSET
    cycle: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    medium_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    script_question: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    responses: Union[Unset, List[SurveyquestionsResponse200ItemsItemResponsesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        survey_question_id = self.survey_question_id
        type = self.type
        cycle = self.cycle
        name = self.name
        medium_name = self.medium_name
        short_name = self.short_name
        script_question = self.script_question
        status = self.status
        responses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()

                responses.append(responses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if survey_question_id is not UNSET:
            field_dict["surveyQuestionId"] = survey_question_id
        if type is not UNSET:
            field_dict["type"] = type
        if cycle is not UNSET:
            field_dict["cycle"] = cycle
        if name is not UNSET:
            field_dict["name"] = name
        if medium_name is not UNSET:
            field_dict["mediumName"] = medium_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if script_question is not UNSET:
            field_dict["scriptQuestion"] = script_question
        if status is not UNSET:
            field_dict["status"] = status
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        survey_question_id = d.pop("surveyQuestionId", UNSET)

        type = d.pop("type", UNSET)

        cycle = d.pop("cycle", UNSET)

        name = d.pop("name", UNSET)

        medium_name = d.pop("mediumName", UNSET)

        short_name = d.pop("shortName", UNSET)

        script_question = d.pop("scriptQuestion", UNSET)

        status = d.pop("status", UNSET)

        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = SurveyquestionsResponse200ItemsItemResponsesItem.from_dict(responses_item_data)

            responses.append(responses_item)

        surveyquestions_response_200_items_item = cls(
            survey_question_id=survey_question_id,
            type=type,
            cycle=cycle,
            name=name,
            medium_name=medium_name,
            short_name=short_name,
            script_question=script_question,
            status=status,
            responses=responses,
        )

        surveyquestions_response_200_items_item.additional_properties = d
        return surveyquestions_response_200_items_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
