from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlineactionsformsResponse200ItemsItemConfirmationEmailData")


@attr.s(auto_attribs=True)
class OnlineactionsformsResponse200ItemsItemConfirmationEmailData:
    """
    Attributes:
        from_email (Union[Unset, str]):  Example: jim@gotham.ci.us.
        from_name (Union[Unset, str]):  Example: Jim.
        from_subject (Union[Unset, str]):  Example: Thank you for signing up.
        reply_to_email (Union[Unset, str]):  Example: jim@gotham.ci.us.
        copy_to_emails (Union[Unset, List[str]]):
        is_confirmation_email_enabled (Union[Unset, bool]):  Default: True. Example: True.
        is_recurring_email_enabled (Union[Unset, bool]):  Default: True. Example: True.
    """

    from_email: Union[Unset, str] = UNSET
    from_name: Union[Unset, str] = UNSET
    from_subject: Union[Unset, str] = UNSET
    reply_to_email: Union[Unset, str] = UNSET
    copy_to_emails: Union[Unset, List[str]] = UNSET
    is_confirmation_email_enabled: Union[Unset, bool] = True
    is_recurring_email_enabled: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_email = self.from_email
        from_name = self.from_name
        from_subject = self.from_subject
        reply_to_email = self.reply_to_email
        copy_to_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.copy_to_emails, Unset):
            copy_to_emails = self.copy_to_emails

        is_confirmation_email_enabled = self.is_confirmation_email_enabled
        is_recurring_email_enabled = self.is_recurring_email_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_email is not UNSET:
            field_dict["fromEmail"] = from_email
        if from_name is not UNSET:
            field_dict["fromName"] = from_name
        if from_subject is not UNSET:
            field_dict["fromSubject"] = from_subject
        if reply_to_email is not UNSET:
            field_dict["replyToEmail"] = reply_to_email
        if copy_to_emails is not UNSET:
            field_dict["copyToEmails"] = copy_to_emails
        if is_confirmation_email_enabled is not UNSET:
            field_dict["isConfirmationEmailEnabled"] = is_confirmation_email_enabled
        if is_recurring_email_enabled is not UNSET:
            field_dict["isRecurringEmailEnabled"] = is_recurring_email_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_email = d.pop("fromEmail", UNSET)

        from_name = d.pop("fromName", UNSET)

        from_subject = d.pop("fromSubject", UNSET)

        reply_to_email = d.pop("replyToEmail", UNSET)

        copy_to_emails = cast(List[str], d.pop("copyToEmails", UNSET))

        is_confirmation_email_enabled = d.pop("isConfirmationEmailEnabled", UNSET)

        is_recurring_email_enabled = d.pop("isRecurringEmailEnabled", UNSET)

        onlineactionsforms_response_200_items_item_confirmation_email_data = cls(
            from_email=from_email,
            from_name=from_name,
            from_subject=from_subject,
            reply_to_email=reply_to_email,
            copy_to_emails=copy_to_emails,
            is_confirmation_email_enabled=is_confirmation_email_enabled,
            is_recurring_email_enabled=is_recurring_email_enabled,
        )

        onlineactionsforms_response_200_items_item_confirmation_email_data.additional_properties = d
        return onlineactionsforms_response_200_items_item_confirmation_email_data

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
