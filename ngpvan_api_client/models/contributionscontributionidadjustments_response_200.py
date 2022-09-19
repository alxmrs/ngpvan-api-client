from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContributionscontributionidadjustmentsResponse200")


@attr.s(auto_attribs=True)
class ContributionscontributionidadjustmentsResponse200:
    """
    Attributes:
        contribution_id (Union[Unset, int]):  Example: 123.
        original_amount (Union[Unset, int]):  Example: 20.
        remaining_amount (Union[Unset, int]):  Example: 10.
        date_adjusted (Union[Unset, str]):  Example: 2020-03-04.
    """

    contribution_id: Union[Unset, int] = 0
    original_amount: Union[Unset, int] = 0
    remaining_amount: Union[Unset, int] = 0
    date_adjusted: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contribution_id = self.contribution_id
        original_amount = self.original_amount
        remaining_amount = self.remaining_amount
        date_adjusted = self.date_adjusted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contribution_id is not UNSET:
            field_dict["contributionId"] = contribution_id
        if original_amount is not UNSET:
            field_dict["originalAmount"] = original_amount
        if remaining_amount is not UNSET:
            field_dict["remainingAmount"] = remaining_amount
        if date_adjusted is not UNSET:
            field_dict["dateAdjusted"] = date_adjusted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contribution_id = d.pop("contributionId", UNSET)

        original_amount = d.pop("originalAmount", UNSET)

        remaining_amount = d.pop("remainingAmount", UNSET)

        date_adjusted = d.pop("dateAdjusted", UNSET)

        contributionscontributionidadjustments_response_200 = cls(
            contribution_id=contribution_id,
            original_amount=original_amount,
            remaining_amount=remaining_amount,
            date_adjusted=date_adjusted,
        )

        contributionscontributionidadjustments_response_200.additional_properties = d
        return contributionscontributionidadjustments_response_200

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
