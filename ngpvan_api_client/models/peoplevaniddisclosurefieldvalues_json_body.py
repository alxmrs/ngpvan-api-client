from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplevaniddisclosurefieldvalues_json_body_disclosure_field_values_item import (
    PeoplevaniddisclosurefieldvaluesJsonBodyDisclosureFieldValuesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevaniddisclosurefieldvaluesJsonBody")


@attr.s(auto_attribs=True)
class PeoplevaniddisclosurefieldvaluesJsonBody:
    """
    Attributes:
        disclosure_field_values (Union[Unset, List[PeoplevaniddisclosurefieldvaluesJsonBodyDisclosureFieldValuesItem]]):
            An array of  [Disclosure Fields Value](ref:people#disclosure-field-values) objects associated with the
            contribution
    """

    disclosure_field_values: Union[
        Unset, List[PeoplevaniddisclosurefieldvaluesJsonBodyDisclosureFieldValuesItem]
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disclosure_field_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.disclosure_field_values, Unset):
            disclosure_field_values = []
            for disclosure_field_values_item_data in self.disclosure_field_values:
                disclosure_field_values_item = disclosure_field_values_item_data.to_dict()

                disclosure_field_values.append(disclosure_field_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disclosure_field_values is not UNSET:
            field_dict["disclosureFieldValues"] = disclosure_field_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disclosure_field_values = []
        _disclosure_field_values = d.pop("disclosureFieldValues", UNSET)
        for disclosure_field_values_item_data in _disclosure_field_values or []:
            disclosure_field_values_item = PeoplevaniddisclosurefieldvaluesJsonBodyDisclosureFieldValuesItem.from_dict(
                disclosure_field_values_item_data
            )

            disclosure_field_values.append(disclosure_field_values_item)

        peoplevaniddisclosurefieldvalues_json_body = cls(
            disclosure_field_values=disclosure_field_values,
        )

        peoplevaniddisclosurefieldvalues_json_body.additional_properties = d
        return peoplevaniddisclosurefieldvalues_json_body

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
