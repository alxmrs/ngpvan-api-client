from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2Response201Event")


@attr.s(auto_attribs=True)
class Signups2Response201Event:
    """
    Attributes:
        event_id (Union[Unset, int]):  Example: 1370.
        name (Union[Unset, str]):  Example: Neighbors Calling Neighbors.
        short_name (Union[Unset, str]):  Example: NeighborCall.
    """

    event_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_id = self.event_id
        name = self.name
        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_id = d.pop("eventId", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        signups_2_response_201_event = cls(
            event_id=event_id,
            name=name,
            short_name=short_name,
        )

        signups_2_response_201_event.additional_properties = d
        return signups_2_response_201_event

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
