from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.changedentityexportjobsexportjobid_response_200_files_item import (
    ChangedentityexportjobsexportjobidResponse200FilesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangedentityexportjobsexportjobidResponse200")


@attr.s(auto_attribs=True)
class ChangedentityexportjobsexportjobidResponse200:
    """
    Attributes:
        export_job_id (Union[Unset, int]):  Example: 12345.
        job_status (Union[Unset, str]):  Example: Complete.
        date_changed_from (Union[Unset, str]):  Example: 2019-01-01T01:02:03+04:00.
        date_changed_to (Union[Unset, str]):  Example: 2019-01-01T07:03:09+04:00.
        files (Union[Unset, List[ChangedentityexportjobsexportjobidResponse200FilesItem]]):
        message (Union[Unset, str]):  Example: Finished processing export job.
        code (Union[Unset, Any]):
        exported_record_count (Union[Unset, int]):  Example: 10500.
    """

    export_job_id: Union[Unset, int] = 0
    job_status: Union[Unset, str] = UNSET
    date_changed_from: Union[Unset, str] = UNSET
    date_changed_to: Union[Unset, str] = UNSET
    files: Union[Unset, List[ChangedentityexportjobsexportjobidResponse200FilesItem]] = UNSET
    message: Union[Unset, str] = UNSET
    code: Union[Unset, Any] = UNSET
    exported_record_count: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_job_id = self.export_job_id
        job_status = self.job_status
        date_changed_from = self.date_changed_from
        date_changed_to = self.date_changed_to
        files: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()

                files.append(files_item)

        message = self.message
        code = self.code
        exported_record_count = self.exported_record_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_job_id is not UNSET:
            field_dict["exportJobId"] = export_job_id
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status
        if date_changed_from is not UNSET:
            field_dict["dateChangedFrom"] = date_changed_from
        if date_changed_to is not UNSET:
            field_dict["dateChangedTo"] = date_changed_to
        if files is not UNSET:
            field_dict["files"] = files
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code
        if exported_record_count is not UNSET:
            field_dict["exportedRecordCount"] = exported_record_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        export_job_id = d.pop("exportJobId", UNSET)

        job_status = d.pop("jobStatus", UNSET)

        date_changed_from = d.pop("dateChangedFrom", UNSET)

        date_changed_to = d.pop("dateChangedTo", UNSET)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = ChangedentityexportjobsexportjobidResponse200FilesItem.from_dict(files_item_data)

            files.append(files_item)

        message = d.pop("message", UNSET)

        code = d.pop("code", UNSET)

        exported_record_count = d.pop("exportedRecordCount", UNSET)

        changedentityexportjobsexportjobid_response_200 = cls(
            export_job_id=export_job_id,
            job_status=job_status,
            date_changed_from=date_changed_from,
            date_changed_to=date_changed_to,
            files=files,
            message=message,
            code=code,
            exported_record_count=exported_record_count,
        )

        changedentityexportjobsexportjobid_response_200.additional_properties = d
        return changedentityexportjobsexportjobid_response_200

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
