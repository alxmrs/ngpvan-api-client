from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteCodesJsonBody")


@attr.s(auto_attribs=True)
class DeleteCodesJsonBody:
    """
    Attributes:
        code_ids (Union[Unset, List[int]]): Accepts a comma-separated array of codeIds
    """

    code_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.code_ids, Unset):
            code_ids = self.code_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code_ids is not UNSET:
            field_dict["codeIds"] = code_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code_ids = cast(List[int], d.pop("codeIds", UNSET))

        delete_codes_json_body = cls(
            code_ids=code_ids,
        )

        delete_codes_json_body.additional_properties = d
        return delete_codes_json_body

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
