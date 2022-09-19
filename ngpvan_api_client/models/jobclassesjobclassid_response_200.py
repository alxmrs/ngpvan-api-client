from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobclassesjobclassidResponse200")


@attr.s(auto_attribs=True)
class JobclassesjobclassidResponse200:
    """
    Attributes:
        job_class_id (Union[Unset, int]):  Example: 123.
        name (Union[Unset, str]):  Example: Registered Nurse.
        short_name (Union[Unset, str]):  Example: RN.
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

        jobclassesjobclassid_response_200 = cls(
            job_class_id=job_class_id,
            name=name,
            short_name=short_name,
        )

        jobclassesjobclassid_response_200.additional_properties = d
        return jobclassesjobclassid_response_200

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
