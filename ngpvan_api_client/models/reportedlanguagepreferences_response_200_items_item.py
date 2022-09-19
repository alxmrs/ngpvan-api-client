from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportedlanguagepreferencesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class ReportedlanguagepreferencesResponse200ItemsItem:
    """
    Attributes:
        reported_language_preference_id (Union[Unset, int]):  Example: 2.
        reported_language_preference_name (Union[Unset, str]):  Example: Cantonese.
    """

    reported_language_preference_id: Union[Unset, int] = 0
    reported_language_preference_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reported_language_preference_id = self.reported_language_preference_id
        reported_language_preference_name = self.reported_language_preference_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reported_language_preference_id is not UNSET:
            field_dict["reportedLanguagePreferenceId"] = reported_language_preference_id
        if reported_language_preference_name is not UNSET:
            field_dict["reportedLanguagePreferenceName"] = reported_language_preference_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reported_language_preference_id = d.pop("reportedLanguagePreferenceId", UNSET)

        reported_language_preference_name = d.pop("reportedLanguagePreferenceName", UNSET)

        reportedlanguagepreferences_response_200_items_item = cls(
            reported_language_preference_id=reported_language_preference_id,
            reported_language_preference_name=reported_language_preference_name,
        )

        reportedlanguagepreferences_response_200_items_item.additional_properties = d
        return reportedlanguagepreferences_response_200_items_item

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
