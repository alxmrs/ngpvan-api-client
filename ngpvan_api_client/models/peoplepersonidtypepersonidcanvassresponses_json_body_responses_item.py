from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplepersonidtypepersonidcanvassresponses_json_body_responses_item_action import (
    PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemAction,
)
from ..models.peoplepersonidtypepersonidcanvassresponses_json_body_responses_item_type import (
    PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItem")


@attr.s(auto_attribs=True)
class PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItem:
    """
    Attributes:
        type (PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemType): The `type` of this response dictates
            the validation requirements of other properties. One of `ActivistCode`, `SurveyResponse`, or `VolunteerActivity`
        action (Union[Unset, PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemAction]): Indicates whether
            to apply or remove this response from a person (valid for `ActivistCode` and `VolunteerActivity` only) Default:
            PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemAction.APPLY.
        activist_code_id (Union[Unset, int]): Required if `type` is `ActivistCode`; a valid [Activist Code
            ID](ref:activist-codes)
        survey_question_id (Union[Unset, int]): Required if `type` is `SurveyResponse`; a valid [Survey Question
            ID](ref:survey-questions)
        survey_response_id (Union[Unset, int]): Required if `type` is `SurveyResponse`; a valid response corresponding
            to the question specified by `surveyQuestionId`
        volunteer_activity_id (Union[Unset, int]): Required if `type` is `VolunteerActivity`; a valid Volunteer Activity
            ID
    """

    type: PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemType
    action: Union[
        Unset, PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemAction
    ] = PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemAction.APPLY
    activist_code_id: Union[Unset, int] = UNSET
    survey_question_id: Union[Unset, int] = UNSET
    survey_response_id: Union[Unset, int] = UNSET
    volunteer_activity_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        action: Union[Unset, str] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        activist_code_id = self.activist_code_id
        survey_question_id = self.survey_question_id
        survey_response_id = self.survey_response_id
        volunteer_activity_id = self.volunteer_activity_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action
        if activist_code_id is not UNSET:
            field_dict["activistCodeId"] = activist_code_id
        if survey_question_id is not UNSET:
            field_dict["surveyQuestionId"] = survey_question_id
        if survey_response_id is not UNSET:
            field_dict["surveyResponseId"] = survey_response_id
        if volunteer_activity_id is not UNSET:
            field_dict["volunteerActivityId"] = volunteer_activity_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemType(d.pop("type"))

        _action = d.pop("action", UNSET)
        action: Union[Unset, PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemAction(_action)

        activist_code_id = d.pop("activistCodeId", UNSET)

        survey_question_id = d.pop("surveyQuestionId", UNSET)

        survey_response_id = d.pop("surveyResponseId", UNSET)

        volunteer_activity_id = d.pop("volunteerActivityId", UNSET)

        peoplepersonidtypepersonidcanvassresponses_json_body_responses_item = cls(
            type=type,
            action=action,
            activist_code_id=activist_code_id,
            survey_question_id=survey_question_id,
            survey_response_id=survey_response_id,
            volunteer_activity_id=volunteer_activity_id,
        )

        peoplepersonidtypepersonidcanvassresponses_json_body_responses_item.additional_properties = d
        return peoplepersonidtypepersonidcanvassresponses_json_body_responses_item

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
