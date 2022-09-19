from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.emailmessageemailid_response_200_email_message_content_item_email_message_content_distributions import (
    EmailmessageemailidResponse200EmailMessageContentItemEmailMessageContentDistributions,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailmessageemailidResponse200EmailMessageContentItem")


@attr.s(auto_attribs=True)
class EmailmessageemailidResponse200EmailMessageContentItem:
    """
    Attributes:
        name (Union[Unset, str]):  Example: Tom Nook Email.
        sender_display_name (Union[Unset, str]):  Example: Deserted Island Getaway Package.
        sender_email_address (Union[Unset, str]):  Example: nook@nook.inc.
        created_by (Union[Unset, str]):  Example: Max Kamin-Cross.
        date_created (Union[Unset, str]):  Example: 2021-02-04T04:29:00Z.
        email_message_content_distributions (Union[Unset,
            EmailmessageemailidResponse200EmailMessageContentItemEmailMessageContentDistributions]):
    """

    name: Union[Unset, str] = UNSET
    sender_display_name: Union[Unset, str] = UNSET
    sender_email_address: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    email_message_content_distributions: Union[
        Unset, EmailmessageemailidResponse200EmailMessageContentItemEmailMessageContentDistributions
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        sender_display_name = self.sender_display_name
        sender_email_address = self.sender_email_address
        created_by = self.created_by
        date_created = self.date_created
        email_message_content_distributions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email_message_content_distributions, Unset):
            email_message_content_distributions = self.email_message_content_distributions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sender_display_name is not UNSET:
            field_dict["senderDisplayName"] = sender_display_name
        if sender_email_address is not UNSET:
            field_dict["senderEmailAddress"] = sender_email_address
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if email_message_content_distributions is not UNSET:
            field_dict["emailMessageContentDistributions"] = email_message_content_distributions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        sender_display_name = d.pop("senderDisplayName", UNSET)

        sender_email_address = d.pop("senderEmailAddress", UNSET)

        created_by = d.pop("createdBy", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        _email_message_content_distributions = d.pop("emailMessageContentDistributions", UNSET)
        email_message_content_distributions: Union[
            Unset, EmailmessageemailidResponse200EmailMessageContentItemEmailMessageContentDistributions
        ]
        if isinstance(_email_message_content_distributions, Unset):
            email_message_content_distributions = UNSET
        else:
            email_message_content_distributions = (
                EmailmessageemailidResponse200EmailMessageContentItemEmailMessageContentDistributions.from_dict(
                    _email_message_content_distributions
                )
            )

        emailmessageemailid_response_200_email_message_content_item = cls(
            name=name,
            sender_display_name=sender_display_name,
            sender_email_address=sender_email_address,
            created_by=created_by,
            date_created=date_created,
            email_message_content_distributions=email_message_content_distributions,
        )

        emailmessageemailid_response_200_email_message_content_item.additional_properties = d
        return emailmessageemailid_response_200_email_message_content_item

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
