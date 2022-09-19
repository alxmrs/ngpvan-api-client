from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetexportjobsJsonBody")


@attr.s(auto_attribs=True)
class TargetexportjobsJsonBody:
    """
    Attributes:
        target_id (Union[Unset, int]): Required; unique identifier for a specific [Target](ref:targets) Default: 2.
        webhook_url (Union[Unset, str]): Optional; the URL to be notified when the Target Export Job has completed
            Default: 'https://webhook.example.org/completedExportJobs'.
    """

    target_id: Union[Unset, int] = 2
    webhook_url: Union[Unset, str] = "https://webhook.example.org/completedExportJobs"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_id = self.target_id
        webhook_url = self.webhook_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_id = d.pop("targetId", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        targetexportjobs_json_body = cls(
            target_id=target_id,
            webhook_url=webhook_url,
        )

        targetexportjobs_json_body.additional_properties = d
        return targetexportjobs_json_body

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
