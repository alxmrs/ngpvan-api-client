from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.codes_batch_json_body_codes_item import CodesBatchJsonBodyCodesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodesBatchJsonBody")


@attr.s(auto_attribs=True)
class CodesBatchJsonBody:
    """
    Attributes:
        codes (Union[Unset, List[CodesBatchJsonBodyCodesItem]]): Required; An array of zero or more Code objects for
            batch operations.
    """

    codes: Union[Unset, List[CodesBatchJsonBodyCodesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        codes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.codes, Unset):
            codes = []
            for codes_item_data in self.codes:
                codes_item = codes_item_data.to_dict()

                codes.append(codes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codes is not UNSET:
            field_dict["codes"] = codes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        codes = []
        _codes = d.pop("codes", UNSET)
        for codes_item_data in _codes or []:
            codes_item = CodesBatchJsonBodyCodesItem.from_dict(codes_item_data)

            codes.append(codes_item)

        codes_batch_json_body = cls(
            codes=codes,
        )

        codes_batch_json_body.additional_properties = d
        return codes_batch_json_body

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
