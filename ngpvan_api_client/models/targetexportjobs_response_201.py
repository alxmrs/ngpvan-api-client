from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetexportjobsResponse201")


@attr.s(auto_attribs=True)
class TargetexportjobsResponse201:
    """
    Attributes:
        export_job_id (Union[Unset, int]):  Example: 123456.
    """

    export_job_id: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_job_id = self.export_job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_job_id is not UNSET:
            field_dict["exportJobId"] = export_job_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        export_job_id = d.pop("exportJobId", UNSET)

        targetexportjobs_response_201 = cls(
            export_job_id=export_job_id,
        )

        targetexportjobs_response_201.additional_properties = d
        return targetexportjobs_response_201

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
