from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangedentityexportjobsexportjobidResponse200FilesItem")


@attr.s(auto_attribs=True)
class ChangedentityexportjobsexportjobidResponse200FilesItem:
    """
    Attributes:
        download_url (Union[Unset, str]):  Example: https://www.example.com/some-unique-file-name.csv.
        date_expired (Union[Unset, str]):  Example: 2019-01-31T15:05:54.2106809-04:00.
    """

    download_url: Union[Unset, str] = UNSET
    date_expired: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        download_url = self.download_url
        date_expired = self.date_expired

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if date_expired is not UNSET:
            field_dict["dateExpired"] = date_expired

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        download_url = d.pop("downloadUrl", UNSET)

        date_expired = d.pop("dateExpired", UNSET)

        changedentityexportjobsexportjobid_response_200_files_item = cls(
            download_url=download_url,
            date_expired=date_expired,
        )

        changedentityexportjobsexportjobid_response_200_files_item.additional_properties = d
        return changedentityexportjobsexportjobid_response_200_files_item

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
