from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201JobClass")


@attr.s(auto_attribs=True)
class EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201JobClass:
    """
    Attributes:
        job_class_id (Union[Unset, int]):  Example: 805.
        name (Union[Unset, str]):  Example: Custodian.
        short_name (Union[Unset, str]):  Example: Custodian.
    """

    job_class_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_class_id = self.job_class_id
        name = self.name
        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_class_id is not UNSET:
            field_dict["jobClassId"] = job_class_id
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_class_id = d.pop("jobClassId", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_201_job_class = cls(
            job_class_id=job_class_id,
            name=name,
            short_name=short_name,
        )

        employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_201_job_class.additional_properties = (
            d
        )
        return employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_201_job_class

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
