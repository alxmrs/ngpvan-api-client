from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Events2Response201LocationsItem")


@attr.s(auto_attribs=True)
class Events2Response201LocationsItem:
    """
    Attributes:
        location_id (Union[Unset, int]):  Example: 273.
    """

    location_id: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location_id = self.location_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_id is not UNSET:
            field_dict["locationId"] = location_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location_id = d.pop("locationId", UNSET)

        events_2_response_201_locations_item = cls(
            location_id=location_id,
        )

        events_2_response_201_locations_item.additional_properties = d
        return events_2_response_201_locations_item

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
