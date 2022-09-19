from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplepersonidtypepersoniddisclosurefieldvaluesJsonBodyDisclosureFieldValuesItem")


@attr.s(auto_attribs=True)
class PeoplepersonidtypepersoniddisclosurefieldvaluesJsonBodyDisclosureFieldValuesItem:
    """
    Attributes:
        disclosure_field_id (Union[Unset, str]): Identifies the Disclosure Field. Together, the designation id and
            disclosure field id provide a unique identifier of a Disclosure Field. Default: '1001'.
        disclosure_field_value (Union[Unset, str]): The value of the Disclosure Field Default: 'John'.
        designation_id (Union[Unset, str]): The unique identifier of the
            [Designation](https://everyaction.readme.io/reference#designations) of the Disclosure Field Default: '740'.
    """

    disclosure_field_id: Union[Unset, str] = "1001"
    disclosure_field_value: Union[Unset, str] = "John"
    designation_id: Union[Unset, str] = "740"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disclosure_field_id = self.disclosure_field_id
        disclosure_field_value = self.disclosure_field_value
        designation_id = self.designation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disclosure_field_id is not UNSET:
            field_dict["disclosureFieldId"] = disclosure_field_id
        if disclosure_field_value is not UNSET:
            field_dict["disclosureFieldValue"] = disclosure_field_value
        if designation_id is not UNSET:
            field_dict["designationId"] = designation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disclosure_field_id = d.pop("disclosureFieldId", UNSET)

        disclosure_field_value = d.pop("disclosureFieldValue", UNSET)

        designation_id = d.pop("designationId", UNSET)

        peoplepersonidtypepersoniddisclosurefieldvalues_json_body_disclosure_field_values_item = cls(
            disclosure_field_id=disclosure_field_id,
            disclosure_field_value=disclosure_field_value,
            designation_id=designation_id,
        )

        peoplepersonidtypepersoniddisclosurefieldvalues_json_body_disclosure_field_values_item.additional_properties = d
        return peoplepersonidtypepersoniddisclosurefieldvalues_json_body_disclosure_field_values_item

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
