import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.contributions_1_json_body_contact import Contributions1JsonBodyContact
from ..models.contributions_1_json_body_designation import Contributions1JsonBodyDesignation
from ..types import UNSET, Unset

T = TypeVar("T", bound="Contributions1JsonBody")


@attr.s(auto_attribs=True)
class Contributions1JsonBody:
    """
    Attributes:
        contact (Union[Unset, Contributions1JsonBodyContact]): The [Person](ref:people) who contributed
        designation (Union[Unset, Contributions1JsonBodyDesignation]): The financial entity which will receive this
            contribution.
        date_received (Union[Unset, datetime.date]): The date and time of this contribution; must occur before the time
            of the API call. Default: isoparse('2013-12-25T12:23:00Z').date().
        amount (Union[Unset, float]): The amount of the contribution. Non-positive values, and values that have more
            than 2 digits after the decimal point, will not be accepted. Default: 12.34.
        status (Union[Unset, str]): The current status of the contribution: `Declined`, `Pending`, or `Settled`.
            Default: 'Pending'.
        payment_type (Union[Unset, str]): A string representing the method of payment. Default: 'MoneyOrder'.
    """

    contact: Union[Unset, Contributions1JsonBodyContact] = UNSET
    designation: Union[Unset, Contributions1JsonBodyDesignation] = UNSET
    date_received: Union[Unset, datetime.date] = isoparse("2013-12-25T12:23:00Z").date()
    amount: Union[Unset, float] = 12.34
    status: Union[Unset, str] = "Pending"
    payment_type: Union[Unset, str] = "MoneyOrder"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        designation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.designation, Unset):
            designation = self.designation.to_dict()

        date_received: Union[Unset, str] = UNSET
        if not isinstance(self.date_received, Unset):
            date_received = self.date_received.isoformat()

        amount = self.amount
        status = self.status
        payment_type = self.payment_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if designation is not UNSET:
            field_dict["designation"] = designation
        if date_received is not UNSET:
            field_dict["dateReceived"] = date_received
        if amount is not UNSET:
            field_dict["amount"] = amount
        if status is not UNSET:
            field_dict["status"] = status
        if payment_type is not UNSET:
            field_dict["paymentType"] = payment_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, Contributions1JsonBodyContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = Contributions1JsonBodyContact.from_dict(_contact)

        _designation = d.pop("designation", UNSET)
        designation: Union[Unset, Contributions1JsonBodyDesignation]
        if isinstance(_designation, Unset):
            designation = UNSET
        else:
            designation = Contributions1JsonBodyDesignation.from_dict(_designation)

        _date_received = d.pop("dateReceived", UNSET)
        date_received: Union[Unset, datetime.date]
        if isinstance(_date_received, Unset):
            date_received = UNSET
        else:
            date_received = isoparse(_date_received).date()

        amount = d.pop("amount", UNSET)

        status = d.pop("status", UNSET)

        payment_type = d.pop("paymentType", UNSET)

        contributions_1_json_body = cls(
            contact=contact,
            designation=designation,
            date_received=date_received,
            amount=amount,
            status=status,
            payment_type=payment_type,
        )

        contributions_1_json_body.additional_properties = d
        return contributions_1_json_body

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
