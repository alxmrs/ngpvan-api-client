from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.locations_2_json_body_address import Locations2JsonBodyAddress
from ..types import UNSET, Unset

T = TypeVar("T", bound="Locations2JsonBody")


@attr.s(auto_attribs=True)
class Locations2JsonBody:
    """
    Attributes:
        name (Union[Unset, str]):  Default: 'Campaign HQ'.
        address (Union[Unset, Locations2JsonBodyAddress]):
    """

    name: Union[Unset, str] = "Campaign HQ"
    address: Union[Unset, Locations2JsonBodyAddress] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Locations2JsonBodyAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Locations2JsonBodyAddress.from_dict(_address)

        locations_2_json_body = cls(
            name=name,
            address=address,
        )

        locations_2_json_body.additional_properties = d
        return locations_2_json_body

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
