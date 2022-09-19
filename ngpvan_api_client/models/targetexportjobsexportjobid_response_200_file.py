from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetexportjobsexportjobidResponse200File")


@attr.s(auto_attribs=True)
class TargetexportjobsexportjobidResponse200File:
    """
    Attributes:
        download_url (Union[Unset, str]):  Example: https://www.example.com/some-unique-file-name.csv.
        date_expired (Union[Unset, str]):  Example: 2020-04-07T09:45:51.4954493-04:00.
        record_count (Union[Unset, int]):  Example: 16.
    """

    download_url: Union[Unset, str] = UNSET
    date_expired: Union[Unset, str] = UNSET
    record_count: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        download_url = self.download_url
        date_expired = self.date_expired
        record_count = self.record_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if date_expired is not UNSET:
            field_dict["dateExpired"] = date_expired
        if record_count is not UNSET:
            field_dict["recordCount"] = record_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        download_url = d.pop("downloadUrl", UNSET)

        date_expired = d.pop("dateExpired", UNSET)

        record_count = d.pop("recordCount", UNSET)

        targetexportjobsexportjobid_response_200_file = cls(
            download_url=download_url,
            date_expired=date_expired,
            record_count=record_count,
        )

        targetexportjobsexportjobid_response_200_file.additional_properties = d
        return targetexportjobsexportjobid_response_200_file

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
