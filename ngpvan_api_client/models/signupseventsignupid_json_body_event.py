from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignupseventsignupidJsonBodyEvent")


@attr.s(auto_attribs=True)
class SignupseventsignupidJsonBodyEvent:
    """
    Attributes:
        event_id (Union[Unset, int]):  Default: 1370.
    """

    event_id: Union[Unset, int] = 1370
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_id = self.event_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["eventId"] = event_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_id = d.pop("eventId", UNSET)

        signupseventsignupid_json_body_event = cls(
            event_id=event_id,
        )

        signupseventsignupid_json_body_event.additional_properties = d
        return signupseventsignupid_json_body_event

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
