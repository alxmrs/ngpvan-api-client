from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportjobsJsonBody")


@attr.s(auto_attribs=True)
class ExportjobsJsonBody:
    """
    Attributes:
        saved_list_id (Union[Unset, int]): The list of [People](ref:people) who are to be exported Default: 500048.
        type (Union[Unset, int]): The type of export to prepare. Must be an Export Job Type available via `GET
            /exportJobTypes`. Default: 101.
        webhook_url (Union[Unset, str]): The URL to be notified when the Export Job has completed Default:
            'https://webhook.example.org/completedExportJobs'.
    """

    saved_list_id: Union[Unset, int] = 500048
    type: Union[Unset, int] = 101
    webhook_url: Union[Unset, str] = "https://webhook.example.org/completedExportJobs"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        saved_list_id = self.saved_list_id
        type = self.type
        webhook_url = self.webhook_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if saved_list_id is not UNSET:
            field_dict["savedListId"] = saved_list_id
        if type is not UNSET:
            field_dict["type"] = type
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        saved_list_id = d.pop("savedListId", UNSET)

        type = d.pop("type", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        exportjobs_json_body = cls(
            saved_list_id=saved_list_id,
            type=type,
            webhook_url=webhook_url,
        )

        exportjobs_json_body.additional_properties = d
        return exportjobs_json_body

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
