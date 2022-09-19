from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportedgendersResponse200ItemsItem")


@attr.s(auto_attribs=True)
class ReportedgendersResponse200ItemsItem:
    """
    Attributes:
        reported_gender_id (Union[Unset, int]):  Example: 19.
        reported_gender_name (Union[Unset, str]):  Example: Androgyne.
    """

    reported_gender_id: Union[Unset, int] = 0
    reported_gender_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reported_gender_id = self.reported_gender_id
        reported_gender_name = self.reported_gender_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reported_gender_id is not UNSET:
            field_dict["reportedGenderId"] = reported_gender_id
        if reported_gender_name is not UNSET:
            field_dict["reportedGenderName"] = reported_gender_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reported_gender_id = d.pop("reportedGenderId", UNSET)

        reported_gender_name = d.pop("reportedGenderName", UNSET)

        reportedgenders_response_200_items_item = cls(
            reported_gender_id=reported_gender_id,
            reported_gender_name=reported_gender_name,
        )

        reportedgenders_response_200_items_item.additional_properties = d
        return reportedgenders_response_200_items_item

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
