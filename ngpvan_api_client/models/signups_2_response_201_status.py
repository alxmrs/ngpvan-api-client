from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2Response201Status")


@attr.s(auto_attribs=True)
class Signups2Response201Status:
    """
    Attributes:
        status_id (Union[Unset, int]):  Example: 4.
        name (Union[Unset, str]):  Example: Invited.
    """

    status_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_id = self.status_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status_id = d.pop("statusId", UNSET)

        name = d.pop("name", UNSET)

        signups_2_response_201_status = cls(
            status_id=status_id,
            name=name,
        )

        signups_2_response_201_status.additional_properties = d
        return signups_2_response_201_status

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
