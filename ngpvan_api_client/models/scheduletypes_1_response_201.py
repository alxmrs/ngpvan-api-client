from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Scheduletypes1Response201")


@attr.s(auto_attribs=True)
class Scheduletypes1Response201:
    """
    Attributes:
        schedule_type_id (Union[Unset, int]):  Example: 2.
        name (Union[Unset, str]):  Example: Part-Time.
    """

    schedule_type_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schedule_type_id = self.schedule_type_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedule_type_id is not UNSET:
            field_dict["scheduleTypeId"] = schedule_type_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schedule_type_id = d.pop("scheduleTypeId", UNSET)

        name = d.pop("name", UNSET)

        scheduletypes_1_response_201 = cls(
            schedule_type_id=schedule_type_id,
            name=name,
        )

        scheduletypes_1_response_201.additional_properties = d
        return scheduletypes_1_response_201

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
