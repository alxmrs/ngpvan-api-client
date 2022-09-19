from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailmessageemailidResponse200EmailMessageContentItemEmailMessageContentDistributions")


@attr.s(auto_attribs=True)
class EmailmessageemailidResponse200EmailMessageContentItemEmailMessageContentDistributions:
    """
    Attributes:
        date_sent (Union[Unset, str]):  Example: 2021-02-04T04:29:00Z.
        recipient_count (Union[Unset, int]):  Example: 1.
        open_count (Union[Unset, int]):
        links_clicked_count (Union[Unset, int]):
        unsubscribe_count (Union[Unset, int]):
        bounce_count (Union[Unset, int]):  Example: 1.
        contribution_total (Union[Unset, int]):
        form_submission_count (Union[Unset, int]):
        contribution_count (Union[Unset, int]):
        machine_open_count (Union[Unset, int]):
    """

    date_sent: Union[Unset, str] = UNSET
    recipient_count: Union[Unset, int] = 0
    open_count: Union[Unset, int] = 0
    links_clicked_count: Union[Unset, int] = 0
    unsubscribe_count: Union[Unset, int] = 0
    bounce_count: Union[Unset, int] = 0
    contribution_total: Union[Unset, int] = 0
    form_submission_count: Union[Unset, int] = 0
    contribution_count: Union[Unset, int] = 0
    machine_open_count: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_sent = self.date_sent
        recipient_count = self.recipient_count
        open_count = self.open_count
        links_clicked_count = self.links_clicked_count
        unsubscribe_count = self.unsubscribe_count
        bounce_count = self.bounce_count
        contribution_total = self.contribution_total
        form_submission_count = self.form_submission_count
        contribution_count = self.contribution_count
        machine_open_count = self.machine_open_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_sent is not UNSET:
            field_dict["dateSent"] = date_sent
        if recipient_count is not UNSET:
            field_dict["recipientCount"] = recipient_count
        if open_count is not UNSET:
            field_dict["openCount"] = open_count
        if links_clicked_count is not UNSET:
            field_dict["linksClickedCount"] = links_clicked_count
        if unsubscribe_count is not UNSET:
            field_dict["unsubscribeCount"] = unsubscribe_count
        if bounce_count is not UNSET:
            field_dict["bounceCount"] = bounce_count
        if contribution_total is not UNSET:
            field_dict["contributionTotal"] = contribution_total
        if form_submission_count is not UNSET:
            field_dict["formSubmissionCount"] = form_submission_count
        if contribution_count is not UNSET:
            field_dict["contributionCount"] = contribution_count
        if machine_open_count is not UNSET:
            field_dict["machineOpenCount"] = machine_open_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date_sent = d.pop("dateSent", UNSET)

        recipient_count = d.pop("recipientCount", UNSET)

        open_count = d.pop("openCount", UNSET)

        links_clicked_count = d.pop("linksClickedCount", UNSET)

        unsubscribe_count = d.pop("unsubscribeCount", UNSET)

        bounce_count = d.pop("bounceCount", UNSET)

        contribution_total = d.pop("contributionTotal", UNSET)

        form_submission_count = d.pop("formSubmissionCount", UNSET)

        contribution_count = d.pop("contributionCount", UNSET)

        machine_open_count = d.pop("machineOpenCount", UNSET)

        emailmessageemailid_response_200_email_message_content_item_email_message_content_distributions = cls(
            date_sent=date_sent,
            recipient_count=recipient_count,
            open_count=open_count,
            links_clicked_count=links_clicked_count,
            unsubscribe_count=unsubscribe_count,
            bounce_count=bounce_count,
            contribution_total=contribution_total,
            form_submission_count=form_submission_count,
            contribution_count=contribution_count,
            machine_open_count=machine_open_count,
        )

        emailmessageemailid_response_200_email_message_content_item_email_message_content_distributions.additional_properties = (
            d
        )
        return emailmessageemailid_response_200_email_message_content_item_email_message_content_distributions

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
