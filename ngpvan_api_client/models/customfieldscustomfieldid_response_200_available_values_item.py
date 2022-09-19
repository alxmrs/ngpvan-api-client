from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomfieldscustomfieldidResponse200AvailableValuesItem")


@attr.s(auto_attribs=True)
class CustomfieldscustomfieldidResponse200AvailableValuesItem:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 1.
        name (Union[Unset, str]):  Example: High School diploma.
        parent_value_id (Union[Unset, Any]):
    """

    id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    parent_value_id: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        parent_value_id = self.parent_value_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_value_id is not UNSET:
            field_dict["parentValueId"] = parent_value_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parent_value_id = d.pop("parentValueId", UNSET)

        customfieldscustomfieldid_response_200_available_values_item = cls(
            id=id,
            name=name,
            parent_value_id=parent_value_id,
        )

        customfieldscustomfieldid_response_200_available_values_item.additional_properties = d
        return customfieldscustomfieldid_response_200_available_values_item

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
