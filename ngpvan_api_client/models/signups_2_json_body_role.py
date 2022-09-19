from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2JsonBodyRole")


@attr.s(auto_attribs=True)
class Signups2JsonBodyRole:
    """
    Attributes:
        role_id (Union[Unset, int]):  Default: 111687.
    """

    role_id: Union[Unset, int] = 111687
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_id = self.role_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["roleId"] = role_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_id = d.pop("roleId", UNSET)

        signups_2_json_body_role = cls(
            role_id=role_id,
        )

        signups_2_json_body_role.additional_properties = d
        return signups_2_json_body_role

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
