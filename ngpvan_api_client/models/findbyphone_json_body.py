from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindbyphoneJsonBody")


@attr.s(auto_attribs=True)
class FindbyphoneJsonBody:
    """
    Attributes:
        phone_number (Union[Unset, str]): A valid phone number as an integer or string Default: '8005551212'.
    """

    phone_number: Union[Unset, str] = "8005551212"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phone_number = self.phone_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        phone_number = d.pop("phoneNumber", UNSET)

        findbyphone_json_body = cls(
            phone_number=phone_number,
        )

        findbyphone_json_body.additional_properties = d
        return findbyphone_json_body

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
