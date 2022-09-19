from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.eventseventidshifts_json_body_shift import EventseventidshiftsJsonBodyShift
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventseventidshiftsJsonBody")


@attr.s(auto_attribs=True)
class EventseventidshiftsJsonBody:
    """
    Attributes:
        shift (Union[Unset, EventseventidshiftsJsonBodyShift]): The body of this request is a standard Event Shift
    """

    shift: Union[Unset, EventseventidshiftsJsonBodyShift] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shift: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shift, Unset):
            shift = self.shift.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shift is not UNSET:
            field_dict["shift"] = shift

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _shift = d.pop("shift", UNSET)
        shift: Union[Unset, EventseventidshiftsJsonBodyShift]
        if isinstance(_shift, Unset):
            shift = UNSET
        else:
            shift = EventseventidshiftsJsonBodyShift.from_dict(_shift)

        eventseventidshifts_json_body = cls(
            shift=shift,
        )

        eventseventidshifts_json_body.additional_properties = d
        return eventseventidshifts_json_body

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
