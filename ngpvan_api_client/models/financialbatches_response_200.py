from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.financialbatches_response_200_items_item import FinancialbatchesResponse200ItemsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="FinancialbatchesResponse200")


@attr.s(auto_attribs=True)
class FinancialbatchesResponse200:
    """
    Attributes:
        items (Union[Unset, List[FinancialbatchesResponse200ItemsItem]]):
    """

    items: Union[Unset, List[FinancialbatchesResponse200ItemsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = FinancialbatchesResponse200ItemsItem.from_dict(items_item_data)

            items.append(items_item)

        financialbatches_response_200 = cls(
            items=items,
        )

        financialbatches_response_200.additional_properties = d
        return financialbatches_response_200

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