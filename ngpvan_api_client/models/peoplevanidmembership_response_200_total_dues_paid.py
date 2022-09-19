from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidmembershipResponse200TotalDuesPaid")


@attr.s(auto_attribs=True)
class PeoplevanidmembershipResponse200TotalDuesPaid:
    """
    Attributes:
        currency_type (Union[Unset, Any]):
        amount (Union[Unset, int]):  Example: 10.
    """

    currency_type: Union[Unset, Any] = UNSET
    amount: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency_type = self.currency_type
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_type is not UNSET:
            field_dict["currencyType"] = currency_type
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency_type = d.pop("currencyType", UNSET)

        amount = d.pop("amount", UNSET)

        peoplevanidmembership_response_200_total_dues_paid = cls(
            currency_type=currency_type,
            amount=amount,
        )

        peoplevanidmembership_response_200_total_dues_paid.additional_properties = d
        return peoplevanidmembership_response_200_total_dues_paid

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
