from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplevanidnotes_response_200_items_item_category import PeoplevanidnotesResponse200ItemsItemCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidnotesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class PeoplevanidnotesResponse200ItemsItem:
    """
    Attributes:
        note_id (Union[Unset, int]):  Example: 225.
        text (Union[Unset, str]):  Example: Great chat! This person will be able to volunteer next year..
        is_view_restricted (Union[Unset, bool]):  Default: True.
        category (Union[Unset, PeoplevanidnotesResponse200ItemsItemCategory]):
        created_date (Union[Unset, str]):  Example: 2012-08-22T12:13:00Z.
    """

    note_id: Union[Unset, int] = 0
    text: Union[Unset, str] = UNSET
    is_view_restricted: Union[Unset, bool] = True
    category: Union[Unset, PeoplevanidnotesResponse200ItemsItemCategory] = UNSET
    created_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note_id = self.note_id
        text = self.text
        is_view_restricted = self.is_view_restricted
        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        created_date = self.created_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note_id is not UNSET:
            field_dict["noteId"] = note_id
        if text is not UNSET:
            field_dict["text"] = text
        if is_view_restricted is not UNSET:
            field_dict["isViewRestricted"] = is_view_restricted
        if category is not UNSET:
            field_dict["category"] = category
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        note_id = d.pop("noteId", UNSET)

        text = d.pop("text", UNSET)

        is_view_restricted = d.pop("isViewRestricted", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, PeoplevanidnotesResponse200ItemsItemCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PeoplevanidnotesResponse200ItemsItemCategory.from_dict(_category)

        created_date = d.pop("createdDate", UNSET)

        peoplevanidnotes_response_200_items_item = cls(
            note_id=note_id,
            text=text,
            is_view_restricted=is_view_restricted,
            category=category,
            created_date=created_date,
        )

        peoplevanidnotes_response_200_items_item.additional_properties = d
        return peoplevanidnotes_response_200_items_item

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
