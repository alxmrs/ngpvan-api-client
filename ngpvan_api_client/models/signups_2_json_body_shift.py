from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2JsonBodyShift")


@attr.s(auto_attribs=True)
class Signups2JsonBodyShift:
    """
    Attributes:
        event_shift_id (Union[Unset, int]):  Default: 2162.
    """

    event_shift_id: Union[Unset, int] = 2162
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_shift_id = self.event_shift_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_shift_id is not UNSET:
            field_dict["eventShiftId"] = event_shift_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_shift_id = d.pop("eventShiftId", UNSET)

        signups_2_json_body_shift = cls(
            event_shift_id=event_shift_id,
        )

        signups_2_json_body_shift.additional_properties = d
        return signups_2_json_body_shift

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
