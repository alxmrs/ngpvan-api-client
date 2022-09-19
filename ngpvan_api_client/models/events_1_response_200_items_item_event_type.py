from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Events1Response200ItemsItemEventType")


@attr.s(auto_attribs=True)
class Events1Response200ItemsItemEventType:
    """
    Attributes:
        event_type_id (Union[Unset, int]):  Example: 143856.
        name (Union[Unset, str]):  Example: Phone Bank.
    """

    event_type_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type_id = self.event_type_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type_id is not UNSET:
            field_dict["eventTypeId"] = event_type_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_type_id = d.pop("eventTypeId", UNSET)

        name = d.pop("name", UNSET)

        events_1_response_200_items_item_event_type = cls(
            event_type_id=event_type_id,
            name=name,
        )

        events_1_response_200_items_item_event_type.additional_properties = d
        return events_1_response_200_items_item_event_type

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
