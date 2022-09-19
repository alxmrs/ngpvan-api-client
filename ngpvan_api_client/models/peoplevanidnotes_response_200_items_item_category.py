from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidnotesResponse200ItemsItemCategory")


@attr.s(auto_attribs=True)
class PeoplevanidnotesResponse200ItemsItemCategory:
    """
    Attributes:
        note_category_id (Union[Unset, int]):
        name (Union[Unset, Any]):
    """

    note_category_id: Union[Unset, int] = 0
    name: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note_category_id = self.note_category_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note_category_id is not UNSET:
            field_dict["noteCategoryId"] = note_category_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        note_category_id = d.pop("noteCategoryId", UNSET)

        name = d.pop("name", UNSET)

        peoplevanidnotes_response_200_items_item_category = cls(
            note_category_id=note_category_id,
            name=name,
        )

        peoplevanidnotes_response_200_items_item_category.additional_properties = d
        return peoplevanidnotes_response_200_items_item_category

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
