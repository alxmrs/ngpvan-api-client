from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SurveyquestionssurveyquestionidResponse200ResponsesItem")


@attr.s(auto_attribs=True)
class SurveyquestionssurveyquestionidResponse200ResponsesItem:
    """
    Attributes:
        survey_response_id (Union[Unset, int]):  Example: 246016.
        name (Union[Unset, str]):  Example: 1 - Strong Maddow.
        medium_name (Union[Unset, str]):  Example: 1.
        short_name (Union[Unset, str]):  Example: 1.
    """

    survey_response_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    medium_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        survey_response_id = self.survey_response_id
        name = self.name
        medium_name = self.medium_name
        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if survey_response_id is not UNSET:
            field_dict["surveyResponseId"] = survey_response_id
        if name is not UNSET:
            field_dict["name"] = name
        if medium_name is not UNSET:
            field_dict["mediumName"] = medium_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        survey_response_id = d.pop("surveyResponseId", UNSET)

        name = d.pop("name", UNSET)

        medium_name = d.pop("mediumName", UNSET)

        short_name = d.pop("shortName", UNSET)

        surveyquestionssurveyquestionid_response_200_responses_item = cls(
            survey_response_id=survey_response_id,
            name=name,
            medium_name=medium_name,
            short_name=short_name,
        )

        surveyquestionssurveyquestionid_response_200_responses_item.additional_properties = d
        return surveyquestionssurveyquestionid_response_200_responses_item

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
