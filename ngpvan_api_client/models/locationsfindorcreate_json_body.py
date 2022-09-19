from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.locationsfindorcreate_json_body_address import LocationsfindorcreateJsonBodyAddress
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationsfindorcreateJsonBody")


@attr.s(auto_attribs=True)
class LocationsfindorcreateJsonBody:
    """
    Attributes:
        name (Union[Unset, str]):  Default: 'Campaign HQ'.
        address (Union[Unset, LocationsfindorcreateJsonBodyAddress]):
    """

    name: Union[Unset, str] = "Campaign HQ"
    address: Union[Unset, LocationsfindorcreateJsonBodyAddress] = UNSET
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
        address: Union[Unset, LocationsfindorcreateJsonBodyAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = LocationsfindorcreateJsonBodyAddress.from_dict(_address)

        locationsfindorcreate_json_body = cls(
            name=name,
            address=address,
        )

        locationsfindorcreate_json_body.additional_properties = d
        return locationsfindorcreate_json_body

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
