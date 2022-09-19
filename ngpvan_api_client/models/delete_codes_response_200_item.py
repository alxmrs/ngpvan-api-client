from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteCodesResponse200Item")


@attr.s(auto_attribs=True)
class DeleteCodesResponse200Item:
    """
    Attributes:
        field_1020112 (Union[Unset, str]):  Example: This code does not exist or you do not have access to it.
    """

    field_1020112: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_1020112 = self.field_1020112

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_1020112 is not UNSET:
            field_dict["1020112"] = field_1020112

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_1020112 = d.pop("1020112", UNSET)

        delete_codes_response_200_item = cls(
            field_1020112=field_1020112,
        )

        delete_codes_response_200_item.additional_properties = d
        return delete_codes_response_200_item

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
