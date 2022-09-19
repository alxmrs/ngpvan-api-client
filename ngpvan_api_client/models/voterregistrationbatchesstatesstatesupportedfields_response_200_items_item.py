from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.voterregistrationbatchesstatesstatesupportedfields_response_200_items_item_possible_values_item import (
    VoterregistrationbatchesstatesstatesupportedfieldsResponse200ItemsItemPossibleValuesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoterregistrationbatchesstatesstatesupportedfieldsResponse200ItemsItem")


@attr.s(auto_attribs=True)
class VoterregistrationbatchesstatesstatesupportedfieldsResponse200ItemsItem:
    """
    Attributes:
        custom_property_key (Union[Unset, str]):  Example: VR:CatBreed.
        display_name (Union[Unset, str]):  Example: Cat Breed.
        field_type (Union[Unset, str]):  Example: Dropdown.
        max_field_length (Union[Unset, Any]):
        possible_values (Union[Unset,
            List[VoterregistrationbatchesstatesstatesupportedfieldsResponse200ItemsItemPossibleValuesItem]]):
    """

    custom_property_key: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    field_type: Union[Unset, str] = UNSET
    max_field_length: Union[Unset, Any] = UNSET
    possible_values: Union[
        Unset, List[VoterregistrationbatchesstatesstatesupportedfieldsResponse200ItemsItemPossibleValuesItem]
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_property_key = self.custom_property_key
        display_name = self.display_name
        field_type = self.field_type
        max_field_length = self.max_field_length
        possible_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.possible_values, Unset):
            possible_values = []
            for possible_values_item_data in self.possible_values:
                possible_values_item = possible_values_item_data.to_dict()

                possible_values.append(possible_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_property_key is not UNSET:
            field_dict["customPropertyKey"] = custom_property_key
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if field_type is not UNSET:
            field_dict["fieldType"] = field_type
        if max_field_length is not UNSET:
            field_dict["maxFieldLength"] = max_field_length
        if possible_values is not UNSET:
            field_dict["possibleValues"] = possible_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_property_key = d.pop("customPropertyKey", UNSET)

        display_name = d.pop("displayName", UNSET)

        field_type = d.pop("fieldType", UNSET)

        max_field_length = d.pop("maxFieldLength", UNSET)

        possible_values = []
        _possible_values = d.pop("possibleValues", UNSET)
        for possible_values_item_data in _possible_values or []:
            possible_values_item = (
                VoterregistrationbatchesstatesstatesupportedfieldsResponse200ItemsItemPossibleValuesItem.from_dict(
                    possible_values_item_data
                )
            )

            possible_values.append(possible_values_item)

        voterregistrationbatchesstatesstatesupportedfields_response_200_items_item = cls(
            custom_property_key=custom_property_key,
            display_name=display_name,
            field_type=field_type,
            max_field_length=max_field_length,
            possible_values=possible_values,
        )

        voterregistrationbatchesstatesstatesupportedfields_response_200_items_item.additional_properties = d
        return voterregistrationbatchesstatesstatesupportedfields_response_200_items_item

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
