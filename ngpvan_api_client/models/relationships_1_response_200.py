from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.relationships_1_response_200_items_item import Relationships1Response200ItemsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Relationships1Response200")


@attr.s(auto_attribs=True)
class Relationships1Response200:
    """
    Attributes:
        items (Union[Unset, List[Relationships1Response200ItemsItem]]):
        count (Union[Unset, int]):  Example: 20.
        next_page_link (Union[Unset, str]):  Example: https://api.securevan.com/v4/relationships?$top=3&$skip=4.
    """

    items: Union[Unset, List[Relationships1Response200ItemsItem]] = UNSET
    count: Union[Unset, int] = 0
    next_page_link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        count = self.count
        next_page_link = self.next_page_link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if count is not UNSET:
            field_dict["count"] = count
        if next_page_link is not UNSET:
            field_dict["nextPageLink"] = next_page_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = Relationships1Response200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        count = d.pop("count", UNSET)

        next_page_link = d.pop("nextPageLink", UNSET)

        relationships_1_response_200 = cls(
            items=items,
            count=count,
            next_page_link=next_page_link,
        )

        relationships_1_response_200.additional_properties = d
        return relationships_1_response_200

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
