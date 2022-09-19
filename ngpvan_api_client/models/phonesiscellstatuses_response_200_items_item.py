from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhonesiscellstatusesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class PhonesiscellstatusesResponse200ItemsItem:
    """
    Attributes:
        status_id (Union[Unset, int]):  Example: 1.
        status_name (Union[Unset, str]):  Example: Verified Cell.
    """

    status_id: Union[Unset, int] = 0
    status_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_id = self.status_id
        status_name = self.status_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if status_name is not UNSET:
            field_dict["statusName"] = status_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_id = d.pop("statusId", UNSET)

        status_name = d.pop("statusName", UNSET)

        phonesiscellstatuses_response_200_items_item = cls(
            status_id=status_id,
            status_name=status_name,
        )

        phonesiscellstatuses_response_200_items_item.additional_properties = d
        return phonesiscellstatuses_response_200_items_item

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
