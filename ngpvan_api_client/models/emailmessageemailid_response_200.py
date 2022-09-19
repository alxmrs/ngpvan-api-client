from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.emailmessageemailid_response_200_email_message_content_item import (
    EmailmessageemailidResponse200EmailMessageContentItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailmessageemailidResponse200")


@attr.s(auto_attribs=True)
class EmailmessageemailidResponse200:
    """
    Attributes:
        foreign_message_id (Union[Unset, str]):  Example: K3Jy8GbLEeuYiQAVXUPJkg2.
        name (Union[Unset, str]):  Example: Tom Nook Email.
        created_by (Union[Unset, str]):  Example: Max Kamin-Cross.
        date_created (Union[Unset, str]):  Example: 2021-02-04T04:27:00Z.
        date_scheduled (Union[Unset, str]):  Example: 2021-02-04T04:29:00Z.
        campaign_id (Union[Unset, int]):  Example: 725.
        date_modified (Union[Unset, str]):  Example: 2021-02-04T04:29:21.653Z.
        email_message_content (Union[Unset, List[EmailmessageemailidResponse200EmailMessageContentItem]]):
    """

    foreign_message_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    date_scheduled: Union[Unset, str] = UNSET
    campaign_id: Union[Unset, int] = 0
    date_modified: Union[Unset, str] = UNSET
    email_message_content: Union[Unset, List[EmailmessageemailidResponse200EmailMessageContentItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        foreign_message_id = self.foreign_message_id
        name = self.name
        created_by = self.created_by
        date_created = self.date_created
        date_scheduled = self.date_scheduled
        campaign_id = self.campaign_id
        date_modified = self.date_modified
        email_message_content: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.email_message_content, Unset):
            email_message_content = []
            for email_message_content_item_data in self.email_message_content:
                email_message_content_item = email_message_content_item_data.to_dict()

                email_message_content.append(email_message_content_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if foreign_message_id is not UNSET:
            field_dict["foreignMessageId"] = foreign_message_id
        if name is not UNSET:
            field_dict["name"] = name
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_scheduled is not UNSET:
            field_dict["dateScheduled"] = date_scheduled
        if campaign_id is not UNSET:
            field_dict["campaignID"] = campaign_id
        if date_modified is not UNSET:
            field_dict["dateModified"] = date_modified
        if email_message_content is not UNSET:
            field_dict["emailMessageContent"] = email_message_content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        foreign_message_id = d.pop("foreignMessageId", UNSET)

        name = d.pop("name", UNSET)

        created_by = d.pop("createdBy", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        date_scheduled = d.pop("dateScheduled", UNSET)

        campaign_id = d.pop("campaignID", UNSET)

        date_modified = d.pop("dateModified", UNSET)

        email_message_content = []
        _email_message_content = d.pop("emailMessageContent", UNSET)
        for email_message_content_item_data in _email_message_content or []:
            email_message_content_item = EmailmessageemailidResponse200EmailMessageContentItem.from_dict(
                email_message_content_item_data
            )

            email_message_content.append(email_message_content_item)

        emailmessageemailid_response_200 = cls(
            foreign_message_id=foreign_message_id,
            name=name,
            created_by=created_by,
            date_created=date_created,
            date_scheduled=date_scheduled,
            campaign_id=campaign_id,
            date_modified=date_modified,
            email_message_content=email_message_content,
        )

        emailmessageemailid_response_200.additional_properties = d
        return emailmessageemailid_response_200

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
