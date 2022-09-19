from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Events2Response201EventType")


@attr.s(auto_attribs=True)
class Events2Response201EventType:
    """
    Attributes:
        event_type_id (Union[Unset, int]):  Example: 143856.
    """

    event_type_id: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type_id = self.event_type_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type_id is not UNSET:
            field_dict["eventTypeId"] = event_type_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_type_id = d.pop("eventTypeId", UNSET)

        events_2_response_201_event_type = cls(
            event_type_id=event_type_id,
        )

        events_2_response_201_event_type.additional_properties = d
        return events_2_response_201_event_type

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
