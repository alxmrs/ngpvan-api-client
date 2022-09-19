from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MinivanexportsResponse200ItemsItemCreatedBy")


@attr.s(auto_attribs=True)
class MinivanexportsResponse200ItemsItemCreatedBy:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 220.
        user_id (Union[Unset, int]):  Example: 220.
        first_name (Union[Unset, str]):  Example: Max.
        last_name (Union[Unset, str]):  Example: Kamin-Cross.
        display_name (Union[Unset, str]):  Example: Max Kamin-Cross.
    """

    id: Union[Unset, int] = 0
    user_id: Union[Unset, int] = 0
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        first_name = self.first_name
        last_name = self.last_name
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        display_name = d.pop("displayName", UNSET)

        minivanexports_response_200_items_item_created_by = cls(
            id=id,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
        )

        minivanexports_response_200_items_item_created_by.additional_properties = d
        return minivanexports_response_200_items_item_created_by

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
