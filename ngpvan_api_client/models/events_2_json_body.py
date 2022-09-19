from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.events_2_json_body_event import Events2JsonBodyEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="Events2JsonBody")


@attr.s(auto_attribs=True)
class Events2JsonBody:
    """
    Attributes:
        event (Union[Unset, Events2JsonBodyEvent]): Accepts a standard Event object with simple types and no read-only
            values specified.
    """

    event: Union[Unset, Events2JsonBodyEvent] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _event = d.pop("event", UNSET)
        event: Union[Unset, Events2JsonBodyEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = Events2JsonBodyEvent.from_dict(_event)

        events_2_json_body = cls(
            event=event,
        )

        events_2_json_body.additional_properties = d
        return events_2_json_body

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
