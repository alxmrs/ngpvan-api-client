from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployersemployeriddeparmentsJsonBody")


@attr.s(auto_attribs=True)
class EmployersemployeriddeparmentsJsonBody:
    """
    Attributes:
        name (Union[Unset, str]):  Default: 'Human Resources'.
        parent_department_id (Union[Unset, str]):  Default: '135'.
    """

    name: Union[Unset, str] = "Human Resources"
    parent_department_id: Union[Unset, str] = "135"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        parent_department_id = self.parent_department_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if parent_department_id is not UNSET:
            field_dict["parentDepartmentId"] = parent_department_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        parent_department_id = d.pop("parentDepartmentId", UNSET)

        employersemployeriddeparments_json_body = cls(
            name=name,
            parent_department_id=parent_department_id,
        )

        employersemployeriddeparments_json_body.additional_properties = d
        return employersemployeriddeparments_json_body

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
