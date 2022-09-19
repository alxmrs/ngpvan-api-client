from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Eventseventid1JsonBody")


@attr.s(auto_attribs=True)
class Eventseventid1JsonBody:
    """
    Attributes:
        event_id (Union[Unset, int]): Required; Unique identifier of the event to be updated Default: 1631.
        is_active (Union[Unset, bool]): Required; If `true`, will restore a previously deleted Event; If `false`, the
            result will effectively be the same as if the Events Delete API method had been called. Default: True.
    """

    event_id: Union[Unset, int] = 1631
    is_active: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_id = self.event_id
        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_id = d.pop("eventId", UNSET)

        is_active = d.pop("isActive", UNSET)

        eventseventid_1_json_body = cls(
            event_id=event_id,
            is_active=is_active,
        )

        eventseventid_1_json_body.additional_properties = d
        return eventseventid_1_json_body

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
