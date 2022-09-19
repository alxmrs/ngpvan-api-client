from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CanvassfilereqeustscanvassfileidResponse200")


@attr.s(auto_attribs=True)
class CanvassfilereqeustscanvassfileidResponse200:
    """
    Attributes:
        canvass_file_request_id (Union[Unset, int]):  Example: 123.
        canvass_file_request_guid (Union[Unset, str]):  Example: DC7309A7-19F5-4DC7-8437-33FDBBADC2DA.
        saved_list_id (Union[Unset, int]):  Example: 555888.
        webhook_url (Union[Unset, str]):  Example: https://webhook.example.org/canvassFileRequests.
        download_url (Union[Unset, str]):  Example: https://vancanvassfiles.blob.core.windows.net/canvass-
            file/DC7309A7-2012-05-05T10:18:43.6007964-04:00.csv.
        status (Union[Unset, str]):  Example: Completed.
        type (Union[Unset, int]):  Example: 102.
        date_expired (Union[Unset, str]):  Example: 2012-05-05T12:18:43.6007964-04:00.
        error_code (Union[Unset, Any]):
    """

    canvass_file_request_id: Union[Unset, int] = 0
    canvass_file_request_guid: Union[Unset, str] = UNSET
    saved_list_id: Union[Unset, int] = 0
    webhook_url: Union[Unset, str] = UNSET
    download_url: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    type: Union[Unset, int] = 0
    date_expired: Union[Unset, str] = UNSET
    error_code: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        canvass_file_request_id = self.canvass_file_request_id
        canvass_file_request_guid = self.canvass_file_request_guid
        saved_list_id = self.saved_list_id
        webhook_url = self.webhook_url
        download_url = self.download_url
        status = self.status
        type = self.type
        date_expired = self.date_expired
        error_code = self.error_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if canvass_file_request_id is not UNSET:
            field_dict["canvassFileRequestId"] = canvass_file_request_id
        if canvass_file_request_guid is not UNSET:
            field_dict["canvassFileRequestGuid"] = canvass_file_request_guid
        if saved_list_id is not UNSET:
            field_dict["savedListId"] = saved_list_id
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if status is not UNSET:
            field_dict["status"] = status
        if type is not UNSET:
            field_dict["type"] = type
        if date_expired is not UNSET:
            field_dict["dateExpired"] = date_expired
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        canvass_file_request_id = d.pop("canvassFileRequestId", UNSET)

        canvass_file_request_guid = d.pop("canvassFileRequestGuid", UNSET)

        saved_list_id = d.pop("savedListId", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        download_url = d.pop("downloadUrl", UNSET)

        status = d.pop("status", UNSET)

        type = d.pop("type", UNSET)

        date_expired = d.pop("dateExpired", UNSET)

        error_code = d.pop("errorCode", UNSET)

        canvassfilereqeustscanvassfileid_response_200 = cls(
            canvass_file_request_id=canvass_file_request_id,
            canvass_file_request_guid=canvass_file_request_guid,
            saved_list_id=saved_list_id,
            webhook_url=webhook_url,
            download_url=download_url,
            status=status,
            type=type,
            date_expired=date_expired,
            error_code=error_code,
        )

        canvassfilereqeustscanvassfileid_response_200.additional_properties = d
        return canvassfilereqeustscanvassfileid_response_200

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
