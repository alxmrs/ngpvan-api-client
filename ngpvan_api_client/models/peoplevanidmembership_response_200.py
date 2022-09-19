from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplevanidmembership_response_200_dues_paid import PeoplevanidmembershipResponse200DuesPaid
from ..models.peoplevanidmembership_response_200_first_membership_source_code import (
    PeoplevanidmembershipResponse200FirstMembershipSourceCode,
)
from ..models.peoplevanidmembership_response_200_total_dues_paid import PeoplevanidmembershipResponse200TotalDuesPaid
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidmembershipResponse200")


@attr.s(auto_attribs=True)
class PeoplevanidmembershipResponse200:
    """
    Attributes:
        level_id (Union[Unset, int]):  Example: 123.
        level_name (Union[Unset, str]):  Example: Family Level.
        status_name (Union[Unset, str]):  Example: Active.
        date_expire_membership (Union[Unset, str]):  Example: 2020-11-01T00:00:00Z.
        enrollment_type_name (Union[Unset, str]):  Example: New.
        change_type_name (Union[Unset, str]):  Example: NoChange.
        dues_paid (Union[Unset, PeoplevanidmembershipResponse200DuesPaid]):
        dues_entity_type_name (Union[Unset, str]):  Example: Contributions.
        dues_attribution_type_name (Union[Unset, str]):  Example: GiftMembership.
        date_cards_sent (Union[Unset, str]):  Example: 2020-11-26T00:00:00Z.
        number_of_cards (Union[Unset, int]):  Example: 2.
        date_start_membership (Union[Unset, str]):  Example: 2020-11-25T00:00:00Z.
        first_membership_source_code (Union[Unset, PeoplevanidmembershipResponse200FirstMembershipSourceCode]):
        number_times_renewed (Union[Unset, int]):
        number_consecutive_years (Union[Unset, int]):
        date_last_renewed (Union[Unset, Any]):
        total_dues_paid (Union[Unset, PeoplevanidmembershipResponse200TotalDuesPaid]):
    """

    level_id: Union[Unset, int] = 0
    level_name: Union[Unset, str] = UNSET
    status_name: Union[Unset, str] = UNSET
    date_expire_membership: Union[Unset, str] = UNSET
    enrollment_type_name: Union[Unset, str] = UNSET
    change_type_name: Union[Unset, str] = UNSET
    dues_paid: Union[Unset, PeoplevanidmembershipResponse200DuesPaid] = UNSET
    dues_entity_type_name: Union[Unset, str] = UNSET
    dues_attribution_type_name: Union[Unset, str] = UNSET
    date_cards_sent: Union[Unset, str] = UNSET
    number_of_cards: Union[Unset, int] = 0
    date_start_membership: Union[Unset, str] = UNSET
    first_membership_source_code: Union[Unset, PeoplevanidmembershipResponse200FirstMembershipSourceCode] = UNSET
    number_times_renewed: Union[Unset, int] = 0
    number_consecutive_years: Union[Unset, int] = 0
    date_last_renewed: Union[Unset, Any] = UNSET
    total_dues_paid: Union[Unset, PeoplevanidmembershipResponse200TotalDuesPaid] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        level_id = self.level_id
        level_name = self.level_name
        status_name = self.status_name
        date_expire_membership = self.date_expire_membership
        enrollment_type_name = self.enrollment_type_name
        change_type_name = self.change_type_name
        dues_paid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dues_paid, Unset):
            dues_paid = self.dues_paid.to_dict()

        dues_entity_type_name = self.dues_entity_type_name
        dues_attribution_type_name = self.dues_attribution_type_name
        date_cards_sent = self.date_cards_sent
        number_of_cards = self.number_of_cards
        date_start_membership = self.date_start_membership
        first_membership_source_code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first_membership_source_code, Unset):
            first_membership_source_code = self.first_membership_source_code.to_dict()

        number_times_renewed = self.number_times_renewed
        number_consecutive_years = self.number_consecutive_years
        date_last_renewed = self.date_last_renewed
        total_dues_paid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_dues_paid, Unset):
            total_dues_paid = self.total_dues_paid.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level_id is not UNSET:
            field_dict["levelId"] = level_id
        if level_name is not UNSET:
            field_dict["levelName"] = level_name
        if status_name is not UNSET:
            field_dict["statusName"] = status_name
        if date_expire_membership is not UNSET:
            field_dict["dateExpireMembership"] = date_expire_membership
        if enrollment_type_name is not UNSET:
            field_dict["enrollmentTypeName"] = enrollment_type_name
        if change_type_name is not UNSET:
            field_dict["changeTypeName"] = change_type_name
        if dues_paid is not UNSET:
            field_dict["duesPaid"] = dues_paid
        if dues_entity_type_name is not UNSET:
            field_dict["duesEntityTypeName"] = dues_entity_type_name
        if dues_attribution_type_name is not UNSET:
            field_dict["duesAttributionTypeName"] = dues_attribution_type_name
        if date_cards_sent is not UNSET:
            field_dict["dateCardsSent"] = date_cards_sent
        if number_of_cards is not UNSET:
            field_dict["numberOfCards"] = number_of_cards
        if date_start_membership is not UNSET:
            field_dict["dateStartMembership"] = date_start_membership
        if first_membership_source_code is not UNSET:
            field_dict["firstMembershipSourceCode"] = first_membership_source_code
        if number_times_renewed is not UNSET:
            field_dict["numberTimesRenewed"] = number_times_renewed
        if number_consecutive_years is not UNSET:
            field_dict["numberConsecutiveYears"] = number_consecutive_years
        if date_last_renewed is not UNSET:
            field_dict["dateLastRenewed"] = date_last_renewed
        if total_dues_paid is not UNSET:
            field_dict["totalDuesPaid"] = total_dues_paid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        level_id = d.pop("levelId", UNSET)

        level_name = d.pop("levelName", UNSET)

        status_name = d.pop("statusName", UNSET)

        date_expire_membership = d.pop("dateExpireMembership", UNSET)

        enrollment_type_name = d.pop("enrollmentTypeName", UNSET)

        change_type_name = d.pop("changeTypeName", UNSET)

        _dues_paid = d.pop("duesPaid", UNSET)
        dues_paid: Union[Unset, PeoplevanidmembershipResponse200DuesPaid]
        if isinstance(_dues_paid, Unset):
            dues_paid = UNSET
        else:
            dues_paid = PeoplevanidmembershipResponse200DuesPaid.from_dict(_dues_paid)

        dues_entity_type_name = d.pop("duesEntityTypeName", UNSET)

        dues_attribution_type_name = d.pop("duesAttributionTypeName", UNSET)

        date_cards_sent = d.pop("dateCardsSent", UNSET)

        number_of_cards = d.pop("numberOfCards", UNSET)

        date_start_membership = d.pop("dateStartMembership", UNSET)

        _first_membership_source_code = d.pop("firstMembershipSourceCode", UNSET)
        first_membership_source_code: Union[Unset, PeoplevanidmembershipResponse200FirstMembershipSourceCode]
        if isinstance(_first_membership_source_code, Unset):
            first_membership_source_code = UNSET
        else:
            first_membership_source_code = PeoplevanidmembershipResponse200FirstMembershipSourceCode.from_dict(
                _first_membership_source_code
            )

        number_times_renewed = d.pop("numberTimesRenewed", UNSET)

        number_consecutive_years = d.pop("numberConsecutiveYears", UNSET)

        date_last_renewed = d.pop("dateLastRenewed", UNSET)

        _total_dues_paid = d.pop("totalDuesPaid", UNSET)
        total_dues_paid: Union[Unset, PeoplevanidmembershipResponse200TotalDuesPaid]
        if isinstance(_total_dues_paid, Unset):
            total_dues_paid = UNSET
        else:
            total_dues_paid = PeoplevanidmembershipResponse200TotalDuesPaid.from_dict(_total_dues_paid)

        peoplevanidmembership_response_200 = cls(
            level_id=level_id,
            level_name=level_name,
            status_name=status_name,
            date_expire_membership=date_expire_membership,
            enrollment_type_name=enrollment_type_name,
            change_type_name=change_type_name,
            dues_paid=dues_paid,
            dues_entity_type_name=dues_entity_type_name,
            dues_attribution_type_name=dues_attribution_type_name,
            date_cards_sent=date_cards_sent,
            number_of_cards=number_of_cards,
            date_start_membership=date_start_membership,
            first_membership_source_code=first_membership_source_code,
            number_times_renewed=number_times_renewed,
            number_consecutive_years=number_consecutive_years,
            date_last_renewed=date_last_renewed,
            total_dues_paid=total_dues_paid,
        )

        peoplevanidmembership_response_200.additional_properties = d
        return peoplevanidmembership_response_200

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
