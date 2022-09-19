import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContributionscontributionidadjustmentsJsonBody")


@attr.s(auto_attribs=True)
class ContributionscontributionidadjustmentsJsonBody:
    """
    Attributes:
        adjustment_type (Union[Unset, str]):  Default: 'Refund'.
        amount (Union[Unset, float]):  Default: 10.0.
        date_posted (Union[Unset, datetime.date]):  Default: isoparse('2020-03-31').date().
    """

    adjustment_type: Union[Unset, str] = "Refund"
    amount: Union[Unset, float] = 10.0
    date_posted: Union[Unset, datetime.date] = isoparse("2020-03-31").date()
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        adjustment_type = self.adjustment_type
        amount = self.amount
        date_posted: Union[Unset, str] = UNSET
        if not isinstance(self.date_posted, Unset):
            date_posted = self.date_posted.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjustment_type is not UNSET:
            field_dict["adjustmentType"] = adjustment_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if date_posted is not UNSET:
            field_dict["datePosted"] = date_posted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        adjustment_type = d.pop("adjustmentType", UNSET)

        amount = d.pop("amount", UNSET)

        _date_posted = d.pop("datePosted", UNSET)
        date_posted: Union[Unset, datetime.date]
        if isinstance(_date_posted, Unset):
            date_posted = UNSET
        else:
            date_posted = isoparse(_date_posted).date()

        contributionscontributionidadjustments_json_body = cls(
            adjustment_type=adjustment_type,
            amount=amount,
            date_posted=date_posted,
        )

        contributionscontributionidadjustments_json_body.additional_properties = d
        return contributionscontributionidadjustments_json_body

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
