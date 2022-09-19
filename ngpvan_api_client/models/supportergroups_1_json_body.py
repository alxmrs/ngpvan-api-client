from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Supportergroups1JsonBody")


@attr.s(auto_attribs=True)
class Supportergroups1JsonBody:
    """
    Attributes:
        name (Union[Unset, str]):  Default: 'North End Volunteers'.
        description (Union[Unset, str]):  Default: 'Volunteers from the North End that help out frequently'.
    """

    name: Union[Unset, str] = "North End Volunteers"
    description: Union[Unset, str] = "Volunteers from the North End that help out frequently"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        supportergroups_1_json_body = cls(
            name=name,
            description=description,
        )

        supportergroups_1_json_body.additional_properties = d
        return supportergroups_1_json_body

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
