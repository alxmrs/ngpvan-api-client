from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.customfieldscustomfieldid_response_200_available_values_item import (
    CustomfieldscustomfieldidResponse200AvailableValuesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomfieldscustomfieldidResponse200")


@attr.s(auto_attribs=True)
class CustomfieldscustomfieldidResponse200:
    """
    Attributes:
        custom_field_id (Union[Unset, int]):  Example: 157.
        custom_field_parent_id (Union[Unset, Any]):
        custom_field_name (Union[Unset, str]):  Example: Education level.
        custom_field_group_id (Union[Unset, int]):  Example: 52.
        custom_field_group_name (Union[Unset, str]):  Example: Education.
        custom_field_group_type (Union[Unset, str]):  Example: Contacts.
        custom_field_type_id (Union[Unset, str]):  Example: S.
        is_editable (Union[Unset, bool]):  Default: True. Example: True.
        max_textbox_characters (Union[Unset, Any]):
        available_values (Union[Unset, List[CustomfieldscustomfieldidResponse200AvailableValuesItem]]):
    """

    custom_field_id: Union[Unset, int] = 0
    custom_field_parent_id: Union[Unset, Any] = UNSET
    custom_field_name: Union[Unset, str] = UNSET
    custom_field_group_id: Union[Unset, int] = 0
    custom_field_group_name: Union[Unset, str] = UNSET
    custom_field_group_type: Union[Unset, str] = UNSET
    custom_field_type_id: Union[Unset, str] = UNSET
    is_editable: Union[Unset, bool] = True
    max_textbox_characters: Union[Unset, Any] = UNSET
    available_values: Union[Unset, List[CustomfieldscustomfieldidResponse200AvailableValuesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_id = self.custom_field_id
        custom_field_parent_id = self.custom_field_parent_id
        custom_field_name = self.custom_field_name
        custom_field_group_id = self.custom_field_group_id
        custom_field_group_name = self.custom_field_group_name
        custom_field_group_type = self.custom_field_group_type
        custom_field_type_id = self.custom_field_type_id
        is_editable = self.is_editable
        max_textbox_characters = self.max_textbox_characters
        available_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.available_values, Unset):
            available_values = []
            for available_values_item_data in self.available_values:
                available_values_item = available_values_item_data.to_dict()

                available_values.append(available_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_field_id is not UNSET:
            field_dict["customFieldId"] = custom_field_id
        if custom_field_parent_id is not UNSET:
            field_dict["customFieldParentId"] = custom_field_parent_id
        if custom_field_name is not UNSET:
            field_dict["customFieldName"] = custom_field_name
        if custom_field_group_id is not UNSET:
            field_dict["customFieldGroupId"] = custom_field_group_id
        if custom_field_group_name is not UNSET:
            field_dict["customFieldGroupName"] = custom_field_group_name
        if custom_field_group_type is not UNSET:
            field_dict["customFieldGroupType"] = custom_field_group_type
        if custom_field_type_id is not UNSET:
            field_dict["customFieldTypeId"] = custom_field_type_id
        if is_editable is not UNSET:
            field_dict["isEditable"] = is_editable
        if max_textbox_characters is not UNSET:
            field_dict["maxTextboxCharacters"] = max_textbox_characters
        if available_values is not UNSET:
            field_dict["availableValues"] = available_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_field_id = d.pop("customFieldId", UNSET)

        custom_field_parent_id = d.pop("customFieldParentId", UNSET)

        custom_field_name = d.pop("customFieldName", UNSET)

        custom_field_group_id = d.pop("customFieldGroupId", UNSET)

        custom_field_group_name = d.pop("customFieldGroupName", UNSET)

        custom_field_group_type = d.pop("customFieldGroupType", UNSET)

        custom_field_type_id = d.pop("customFieldTypeId", UNSET)

        is_editable = d.pop("isEditable", UNSET)

        max_textbox_characters = d.pop("maxTextboxCharacters", UNSET)

        available_values = []
        _available_values = d.pop("availableValues", UNSET)
        for available_values_item_data in _available_values or []:
            available_values_item = CustomfieldscustomfieldidResponse200AvailableValuesItem.from_dict(
                available_values_item_data
            )

            available_values.append(available_values_item)

        customfieldscustomfieldid_response_200 = cls(
            custom_field_id=custom_field_id,
            custom_field_parent_id=custom_field_parent_id,
            custom_field_name=custom_field_name,
            custom_field_group_id=custom_field_group_id,
            custom_field_group_name=custom_field_group_name,
            custom_field_group_type=custom_field_group_type,
            custom_field_type_id=custom_field_type_id,
            is_editable=is_editable,
            max_textbox_characters=max_textbox_characters,
            available_values=available_values,
        )

        customfieldscustomfieldid_response_200.additional_properties = d
        return customfieldscustomfieldid_response_200

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
