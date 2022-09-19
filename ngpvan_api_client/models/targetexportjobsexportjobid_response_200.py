from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.targetexportjobsexportjobid_response_200_file import TargetexportjobsexportjobidResponse200File
from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetexportjobsexportjobidResponse200")


@attr.s(auto_attribs=True)
class TargetexportjobsexportjobidResponse200:
    """
    Attributes:
        target_id (Union[Unset, int]):  Example: 55.
        file (Union[Unset, TargetexportjobsexportjobidResponse200File]):
        webhook_url (Union[Unset, str]):  Example: https://webhook.example.org/completedExportJobs.
        export_job_id (Union[Unset, int]):  Example: 1234.
        job_status (Union[Unset, str]):  Example: Complete.
    """

    target_id: Union[Unset, int] = 0
    file: Union[Unset, TargetexportjobsexportjobidResponse200File] = UNSET
    webhook_url: Union[Unset, str] = UNSET
    export_job_id: Union[Unset, int] = 0
    job_status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_id = self.target_id
        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        webhook_url = self.webhook_url
        export_job_id = self.export_job_id
        job_status = self.job_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if file is not UNSET:
            field_dict["file"] = file
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if export_job_id is not UNSET:
            field_dict["exportJobId"] = export_job_id
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_id = d.pop("targetId", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, TargetexportjobsexportjobidResponse200File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = TargetexportjobsexportjobidResponse200File.from_dict(_file)

        webhook_url = d.pop("webhookUrl", UNSET)

        export_job_id = d.pop("exportJobId", UNSET)

        job_status = d.pop("jobStatus", UNSET)

        targetexportjobsexportjobid_response_200 = cls(
            target_id=target_id,
            file=file,
            webhook_url=webhook_url,
            export_job_id=export_job_id,
            job_status=job_status,
        )

        targetexportjobsexportjobid_response_200.additional_properties = d
        return targetexportjobsexportjobid_response_200

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
