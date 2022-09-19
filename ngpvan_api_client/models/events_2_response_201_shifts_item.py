from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Events2Response201ShiftsItem")


@attr.s(auto_attribs=True)
class Events2Response201ShiftsItem:
    """
    Attributes:
        name (Union[Unset, str]):  Example: Setup.
        start_time (Union[Unset, str]):  Example: 2015-06-01T15:00:00-04:00.
        end_time (Union[Unset, str]):  Example: 2015-06-01T16:00:00-04:00.
    """

    name: Union[Unset, str] = UNSET
    start_time: Union[Unset, str] = UNSET
    end_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        start_time = self.start_time
        end_time = self.end_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        events_2_response_201_shifts_item = cls(
            name=name,
            start_time=start_time,
            end_time=end_time,
        )

        events_2_response_201_shifts_item.additional_properties = d
        return events_2_response_201_shifts_item

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
