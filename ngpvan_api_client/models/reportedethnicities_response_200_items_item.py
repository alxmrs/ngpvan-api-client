from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportedethnicitiesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class ReportedethnicitiesResponse200ItemsItem:
    """
    Attributes:
        reported_ethnicity_id (Union[Unset, int]):  Example: 2.
        reported_ethnicity_name (Union[Unset, str]):  Example: Arab.
    """

    reported_ethnicity_id: Union[Unset, int] = 0
    reported_ethnicity_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reported_ethnicity_id = self.reported_ethnicity_id
        reported_ethnicity_name = self.reported_ethnicity_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reported_ethnicity_id is not UNSET:
            field_dict["reportedEthnicityId"] = reported_ethnicity_id
        if reported_ethnicity_name is not UNSET:
            field_dict["reportedEthnicityName"] = reported_ethnicity_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reported_ethnicity_id = d.pop("reportedEthnicityId", UNSET)

        reported_ethnicity_name = d.pop("reportedEthnicityName", UNSET)

        reportedethnicities_response_200_items_item = cls(
            reported_ethnicity_id=reported_ethnicity_id,
            reported_ethnicity_name=reported_ethnicity_name,
        )

        reportedethnicities_response_200_items_item.additional_properties = d
        return reportedethnicities_response_200_items_item

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
