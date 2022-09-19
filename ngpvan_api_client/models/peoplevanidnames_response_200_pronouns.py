from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidnamesResponse200Pronouns")


@attr.s(auto_attribs=True)
class PeoplevanidnamesResponse200Pronouns:
    """
    Attributes:
        pronoun_id (Union[Unset, int]):  Example: 11.
        pronoun_name (Union[Unset, str]):  Example: He/Him/His.
    """

    pronoun_id: Union[Unset, int] = 0
    pronoun_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pronoun_id = self.pronoun_id
        pronoun_name = self.pronoun_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pronoun_id is not UNSET:
            field_dict["pronounId"] = pronoun_id
        if pronoun_name is not UNSET:
            field_dict["pronounName"] = pronoun_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pronoun_id = d.pop("pronounId", UNSET)

        pronoun_name = d.pop("pronounName", UNSET)

        peoplevanidnames_response_200_pronouns = cls(
            pronoun_id=pronoun_id,
            pronoun_name=pronoun_name,
        )

        peoplevanidnames_response_200_pronouns.additional_properties = d
        return peoplevanidnames_response_200_pronouns

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
