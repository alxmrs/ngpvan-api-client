from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Contributions1JsonBodyContact")


@attr.s(auto_attribs=True)
class Contributions1JsonBodyContact:
    """The [Person](ref:people) who contributed

    Attributes:
        van_id (Union[Unset, str]):  Default: '10005165'.
    """

    van_id: Union[Unset, str] = "10005165"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        van_id = self.van_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if van_id is not UNSET:
            field_dict["vanId"] = van_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        van_id = d.pop("vanId", UNSET)

        contributions_1_json_body_contact = cls(
            van_id=van_id,
        )

        contributions_1_json_body_contact.additional_properties = d
        return contributions_1_json_body_contact

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
