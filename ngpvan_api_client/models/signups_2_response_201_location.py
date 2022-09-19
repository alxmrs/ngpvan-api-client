from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2Response201Location")


@attr.s(auto_attribs=True)
class Signups2Response201Location:
    """
    Attributes:
        location_id (Union[Unset, int]):  Example: 272.
        name (Union[Unset, str]):  Example: Campaign HQ.
        display_name (Union[Unset, str]):  Example: Campaign HQ, 48 Grove St Somerville, MA 02144-2500.
    """

    location_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location_id = self.location_id
        name = self.name
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location_id = d.pop("locationId", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        signups_2_response_201_location = cls(
            location_id=location_id,
            name=name,
            display_name=display_name,
        )

        signups_2_response_201_location.additional_properties = d
        return signups_2_response_201_location

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
