from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoriesstoryidResponse200TagsItem")


@attr.s(auto_attribs=True)
class StoriesstoryidResponse200TagsItem:
    """
    Attributes:
        code_id (Union[Unset, int]):  Example: 123.
        code_name (Union[Unset, str]):  Example: Book.
    """

    code_id: Union[Unset, int] = 0
    code_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code_id = self.code_id
        code_name = self.code_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code_id is not UNSET:
            field_dict["codeId"] = code_id
        if code_name is not UNSET:
            field_dict["codeName"] = code_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code_id = d.pop("codeId", UNSET)

        code_name = d.pop("codeName", UNSET)

        storiesstoryid_response_200_tags_item = cls(
            code_id=code_id,
            code_name=code_name,
        )

        storiesstoryid_response_200_tags_item.additional_properties = d
        return storiesstoryid_response_200_tags_item

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
