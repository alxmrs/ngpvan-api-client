from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2Response201Shift")


@attr.s(auto_attribs=True)
class Signups2Response201Shift:
    """
    Attributes:
        event_shift_id (Union[Unset, int]):  Example: 2162.
        name (Union[Unset, Any]):
    """

    event_shift_id: Union[Unset, int] = 0
    name: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_shift_id = self.event_shift_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_shift_id is not UNSET:
            field_dict["eventShiftId"] = event_shift_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_shift_id = d.pop("eventShiftId", UNSET)

        name = d.pop("name", UNSET)

        signups_2_response_201_shift = cls(
            event_shift_id=event_shift_id,
            name=name,
        )

        signups_2_response_201_shift.additional_properties = d
        return signups_2_response_201_shift

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
