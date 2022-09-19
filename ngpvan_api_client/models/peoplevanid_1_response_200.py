from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Peoplevanid1Response200")


@attr.s(auto_attribs=True)
class Peoplevanid1Response200:
    """
    Attributes:
        van_id (Union[Unset, int]):  Example: 100476252.
        first_name (Union[Unset, str]):  Example: James.
        last_name (Union[Unset, str]):  Example: Gordon.
        middle_name (Union[Unset, str]):  Example: Worthington.
        party (Union[Unset, str]):  Example: D.
        employer (Union[Unset, str]):  Example: Acme Medical Group.
        occupation (Union[Unset, str]):  Example: Physician.
        sex (Union[Unset, str]):  Example: M.
        date_of_birth (Union[Unset, str]):  Example: 1976-07-04T00:00:00Z.
    """

    van_id: Union[Unset, int] = 0
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    party: Union[Unset, str] = UNSET
    employer: Union[Unset, str] = UNSET
    occupation: Union[Unset, str] = UNSET
    sex: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        van_id = self.van_id
        first_name = self.first_name
        last_name = self.last_name
        middle_name = self.middle_name
        party = self.party
        employer = self.employer
        occupation = self.occupation
        sex = self.sex
        date_of_birth = self.date_of_birth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if van_id is not UNSET:
            field_dict["vanId"] = van_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if party is not UNSET:
            field_dict["party"] = party
        if employer is not UNSET:
            field_dict["employer"] = employer
        if occupation is not UNSET:
            field_dict["occupation"] = occupation
        if sex is not UNSET:
            field_dict["sex"] = sex
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        van_id = d.pop("vanId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        party = d.pop("party", UNSET)

        employer = d.pop("employer", UNSET)

        occupation = d.pop("occupation", UNSET)

        sex = d.pop("sex", UNSET)

        date_of_birth = d.pop("dateOfBirth", UNSET)

        peoplevanid_1_response_200 = cls(
            van_id=van_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            party=party,
            employer=employer,
            occupation=occupation,
            sex=sex,
            date_of_birth=date_of_birth,
        )

        peoplevanid_1_response_200.additional_properties = d
        return peoplevanid_1_response_200

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
