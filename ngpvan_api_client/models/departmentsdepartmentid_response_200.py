from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.departmentsdepartmentid_response_200_employer import DepartmentsdepartmentidResponse200Employer
from ..types import UNSET, Unset

T = TypeVar("T", bound="DepartmentsdepartmentidResponse200")


@attr.s(auto_attribs=True)
class DepartmentsdepartmentidResponse200:
    """
    Attributes:
        department_id (Union[Unset, int]):  Example: 123.
        name (Union[Unset, str]):  Example: Accounting.
        parent_department_id (Union[Unset, Any]):
        employer (Union[Unset, DepartmentsdepartmentidResponse200Employer]):
    """

    department_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    parent_department_id: Union[Unset, Any] = UNSET
    employer: Union[Unset, DepartmentsdepartmentidResponse200Employer] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        department_id = self.department_id
        name = self.name
        parent_department_id = self.parent_department_id
        employer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employer, Unset):
            employer = self.employer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_department_id is not UNSET:
            field_dict["parentDepartmentId"] = parent_department_id
        if employer is not UNSET:
            field_dict["employer"] = employer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        department_id = d.pop("departmentId", UNSET)

        name = d.pop("name", UNSET)

        parent_department_id = d.pop("parentDepartmentId", UNSET)

        _employer = d.pop("employer", UNSET)
        employer: Union[Unset, DepartmentsdepartmentidResponse200Employer]
        if isinstance(_employer, Unset):
            employer = UNSET
        else:
            employer = DepartmentsdepartmentidResponse200Employer.from_dict(_employer)

        departmentsdepartmentid_response_200 = cls(
            department_id=department_id,
            name=name,
            parent_department_id=parent_department_id,
            employer=employer,
        )

        departmentsdepartmentid_response_200.additional_properties = d
        return departmentsdepartmentid_response_200

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
