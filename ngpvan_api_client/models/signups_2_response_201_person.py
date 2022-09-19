from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2Response201Person")


@attr.s(auto_attribs=True)
class Signups2Response201Person:
    """
    Attributes:
        van_id (Union[Unset, int]):  Example: 100476252.
        first_name (Union[Unset, str]):  Example: James.
        middle_name (Union[Unset, str]):  Example: Worthington.
        last_name (Union[Unset, str]):  Example: Gordon.
    """

    van_id: Union[Unset, int] = 0
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        van_id = self.van_id
        first_name = self.first_name
        middle_name = self.middle_name
        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if van_id is not UNSET:
            field_dict["vanId"] = van_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        van_id = d.pop("vanId", UNSET)

        first_name = d.pop("firstName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        last_name = d.pop("lastName", UNSET)

        signups_2_response_201_person = cls(
            van_id=van_id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
        )

        signups_2_response_201_person.additional_properties = d
        return signups_2_response_201_person

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
