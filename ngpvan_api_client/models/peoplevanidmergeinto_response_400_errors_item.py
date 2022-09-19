from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidmergeintoResponse400ErrorsItem")


@attr.s(auto_attribs=True)
class PeoplevanidmergeintoResponse400ErrorsItem:
    """
    Attributes:
        code (Union[Unset, str]):  Example: INVALID_PARAMETER.
        text (Union[Unset, str]):  Example: You must have access to both contacts to merge them..
    """

    code: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        text = d.pop("text", UNSET)

        peoplevanidmergeinto_response_400_errors_item = cls(
            code=code,
            text=text,
        )

        peoplevanidmergeinto_response_400_errors_item.additional_properties = d
        return peoplevanidmergeinto_response_400_errors_item

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
