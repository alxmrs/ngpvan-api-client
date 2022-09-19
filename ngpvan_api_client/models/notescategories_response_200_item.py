from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotescategoriesResponse200Item")


@attr.s(auto_attribs=True)
class NotescategoriesResponse200Item:
    """
    Attributes:
        assignable_types (Union[Unset, List[str]]):
        note_category_id (Union[Unset, int]):  Example: 24.
        name (Union[Unset, str]):  Example: Event Details.
    """

    assignable_types: Union[Unset, List[str]] = UNSET
    note_category_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignable_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignable_types, Unset):
            assignable_types = self.assignable_types

        note_category_id = self.note_category_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignable_types is not UNSET:
            field_dict["assignableTypes"] = assignable_types
        if note_category_id is not UNSET:
            field_dict["noteCategoryId"] = note_category_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assignable_types = cast(List[str], d.pop("assignableTypes", UNSET))

        note_category_id = d.pop("noteCategoryId", UNSET)

        name = d.pop("name", UNSET)

        notescategories_response_200_item = cls(
            assignable_types=assignable_types,
            note_category_id=note_category_id,
            name=name,
        )

        notescategories_response_200_item.additional_properties = d
        return notescategories_response_200_item

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
