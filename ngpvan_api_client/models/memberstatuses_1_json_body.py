from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Memberstatuses1JsonBody")


@attr.s(auto_attribs=True)
class Memberstatuses1JsonBody:
    """
    Attributes:
        name (Union[Unset, str]):  Default: 'Non-Member'.
        is_member (Union[Unset, bool]):
    """

    name: Union[Unset, str] = "Non-Member"
    is_member: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_member = self.is_member

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if is_member is not UNSET:
            field_dict["isMember"] = is_member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        is_member = d.pop("isMember", UNSET)

        memberstatuses_1_json_body = cls(
            name=name,
            is_member=is_member,
        )

        memberstatuses_1_json_body.additional_properties = d
        return memberstatuses_1_json_body

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
