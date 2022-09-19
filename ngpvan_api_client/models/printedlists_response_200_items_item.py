from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrintedlistsResponse200ItemsItem")


@attr.s(auto_attribs=True)
class PrintedlistsResponse200ItemsItem:
    """
    Attributes:
        number (Union[Unset, str]):  Example: 35536742-78261.
        name (Union[Unset, Any]):
        event_signups (Union[Unset, Any]):
        list_size (Union[Unset, int]):  Example: 3490.
    """

    number: Union[Unset, str] = UNSET
    name: Union[Unset, Any] = UNSET
    event_signups: Union[Unset, Any] = UNSET
    list_size: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number = self.number
        name = self.name
        event_signups = self.event_signups
        list_size = self.list_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if name is not UNSET:
            field_dict["name"] = name
        if event_signups is not UNSET:
            field_dict["eventSignups"] = event_signups
        if list_size is not UNSET:
            field_dict["listSize"] = list_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        name = d.pop("name", UNSET)

        event_signups = d.pop("eventSignups", UNSET)

        list_size = d.pop("listSize", UNSET)

        printedlists_response_200_items_item = cls(
            number=number,
            name=name,
            event_signups=event_signups,
            list_size=list_size,
        )

        printedlists_response_200_items_item.additional_properties = d
        return printedlists_response_200_items_item

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
