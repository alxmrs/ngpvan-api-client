from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployersemployeridshifttypesshifttypeidResponse201")


@attr.s(auto_attribs=True)
class EmployersemployeridshifttypesshifttypeidResponse201:
    """
    Attributes:
        shift_type_id (Union[Unset, int]):  Example: 12.
        default_start_time (Union[Unset, str]):  Example: 18:00Z.
        default_end_time (Union[Unset, str]):  Example: 06:00Z.
    """

    shift_type_id: Union[Unset, int] = 0
    default_start_time: Union[Unset, str] = UNSET
    default_end_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        shift_type_id = self.shift_type_id
        default_start_time = self.default_start_time
        default_end_time = self.default_end_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shift_type_id is not UNSET:
            field_dict["shiftTypeId:"] = shift_type_id
        if default_start_time is not UNSET:
            field_dict["defaultStartTime"] = default_start_time
        if default_end_time is not UNSET:
            field_dict["defaultEndTime"] = default_end_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        shift_type_id = d.pop("shiftTypeId:", UNSET)

        default_start_time = d.pop("defaultStartTime", UNSET)

        default_end_time = d.pop("defaultEndTime", UNSET)

        employersemployeridshifttypesshifttypeid_response_201 = cls(
            shift_type_id=shift_type_id,
            default_start_time=default_start_time,
            default_end_time=default_end_time,
        )

        employersemployeridshifttypesshifttypeid_response_201.additional_properties = d
        return employersemployeridshifttypesshifttypeid_response_201

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
