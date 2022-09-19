from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Designations1Response200ItemsItem")


@attr.s(auto_attribs=True)
class Designations1Response200ItemsItem:
    """
    Attributes:
        designation_id (Union[Unset, int]):  Example: 123456789.
        name (Union[Unset, str]):  Example: Jane for Congress Committee.
    """

    designation_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        designation_id = self.designation_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if designation_id is not UNSET:
            field_dict["designationId"] = designation_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        designation_id = d.pop("designationId", UNSET)

        name = d.pop("name", UNSET)

        designations_1_response_200_items_item = cls(
            designation_id=designation_id,
            name=name,
        )

        designations_1_response_200_items_item.additional_properties = d
        return designations_1_response_200_items_item

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
