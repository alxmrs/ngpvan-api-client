from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangedentityexportjobsfieldsresourcetypeResponse200Item")


@attr.s(auto_attribs=True)
class ChangedentityexportjobsfieldsresourcetypeResponse200Item:
    """
    Attributes:
        field_name (Union[Unset, str]):  Example: Address.
        field_type (Union[Unset, str]):  Example: T.
        max_textbox_characters (Union[Unset, int]):  Example: 200.
        is_core_field (Union[Unset, bool]):  Default: True. Example: True.
        available_values (Union[Unset, Any]):
    """

    field_name: Union[Unset, str] = UNSET
    field_type: Union[Unset, str] = UNSET
    max_textbox_characters: Union[Unset, int] = 0
    is_core_field: Union[Unset, bool] = True
    available_values: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_name = self.field_name
        field_type = self.field_type
        max_textbox_characters = self.max_textbox_characters
        is_core_field = self.is_core_field
        available_values = self.available_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if max_textbox_characters is not UNSET:
            field_dict["maxTextboxCharacters"] = max_textbox_characters
        if is_core_field is not UNSET:
            field_dict["isCoreField"] = is_core_field
        if available_values is not UNSET:
            field_dict["availableValues"] = available_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_name = d.pop("fieldName", UNSET)

        field_type = d.pop("fieldType", UNSET)

        max_textbox_characters = d.pop("maxTextboxCharacters", UNSET)

        is_core_field = d.pop("isCoreField", UNSET)

        available_values = d.pop("availableValues", UNSET)

        changedentityexportjobsfieldsresourcetype_response_200_item = cls(
            field_name=field_name,
            field_type=field_type,
            max_textbox_characters=max_textbox_characters,
            is_core_field=is_core_field,
            available_values=available_values,
        )

        changedentityexportjobsfieldsresourcetype_response_200_item.additional_properties = d
        return changedentityexportjobsfieldsresourcetype_response_200_item

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
