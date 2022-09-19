from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CanvassfilerequestsJsonBody")


@attr.s(auto_attribs=True)
class CanvassfilerequestsJsonBody:
    """
    Attributes:
        saved_list_id (Union[Unset, int]): Integer ID of the saved list containing people to be included in the canvass
            file. The API key requesting the canvass file must have access to the saved list. Default: 555888.
        webhook_url (Union[Unset, str]): Valid HTTPS URL to receive a message POST request when canvass file generation
            is complete. The message will be a JSON object identical to the body of the `GET
            /canvassFileRequests/{canvassFileId}` response for this canvass file request. Default:
            'https://webhook.example.org/canvassFileRequests'.
        type (Union[Unset, int]): Integer ID of the type of canvass file to generate. The API key requesting the canvass
            file must be authorized to request the specified canvass file type. For SMS synchronization always use the value
            102. Default: 102.
    """

    saved_list_id: Union[Unset, int] = 555888
    webhook_url: Union[Unset, str] = "https://webhook.example.org/canvassFileRequests"
    type: Union[Unset, int] = 102
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        saved_list_id = self.saved_list_id
        webhook_url = self.webhook_url
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if saved_list_id is not UNSET:
            field_dict["savedListId"] = saved_list_id
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        saved_list_id = d.pop("savedListId", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        type = d.pop("type", UNSET)

        canvassfilerequests_json_body = cls(
            saved_list_id=saved_list_id,
            webhook_url=webhook_url,
            type=type,
        )

        canvassfilerequests_json_body.additional_properties = d
        return canvassfilerequests_json_body

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
