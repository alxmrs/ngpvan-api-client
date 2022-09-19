from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Locations2JsonBodyAddress")


@attr.s(auto_attribs=True)
class Locations2JsonBodyAddress:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):  Default: '48 Grove St'.
        city (Union[Unset, str]):  Default: 'Somerville'.
        state_or_province (Union[Unset, str]):  Default: 'MA'.
        zip_or_postal_code (Union[Unset, str]):  Default: '02144'.
    """

    address_line_1: Union[Unset, str] = "48 Grove St"
    city: Union[Unset, str] = "Somerville"
    state_or_province: Union[Unset, str] = "MA"
    zip_or_postal_code: Union[Unset, str] = "02144"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_line_1 = self.address_line_1
        city = self.city
        state_or_province = self.state_or_province
        zip_or_postal_code = self.zip_or_postal_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if city is not UNSET:
            field_dict["city"] = city
        if state_or_province is not UNSET:
            field_dict["stateOrProvince"] = state_or_province
        if zip_or_postal_code is not UNSET:
            field_dict["zipOrPostalCode"] = zip_or_postal_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        city = d.pop("city", UNSET)

        state_or_province = d.pop("stateOrProvince", UNSET)

        zip_or_postal_code = d.pop("zipOrPostalCode", UNSET)

        locations_2_json_body_address = cls(
            address_line_1=address_line_1,
            city=city,
            state_or_province=state_or_province,
            zip_or_postal_code=zip_or_postal_code,
        )

        locations_2_json_body_address.additional_properties = d
        return locations_2_json_body_address

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
