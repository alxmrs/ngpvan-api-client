from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EventseventidshiftsJsonBodyShift")


@attr.s(auto_attribs=True)
class EventseventidshiftsJsonBodyShift:
    """The body of this request is a standard Event Shift"""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eventseventidshifts_json_body_shift = cls()

        eventseventidshifts_json_body_shift.additional_properties = d
        return eventseventidshifts_json_body_shift

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
