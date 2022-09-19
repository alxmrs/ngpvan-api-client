from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.patch_codes_codeid_json_body_rawbody_item import PatchCodesCodeidJsonBodyRAWBODYItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchCodesCodeidJsonBody")


@attr.s(auto_attribs=True)
class PatchCodesCodeidJsonBody:
    """
    Attributes:
        raw_body (Union[Unset, List[PatchCodesCodeidJsonBodyRAWBODYItem]]): An ordered list of operations to perform on
            the given Code.
    """

    raw_body: Union[Unset, List[PatchCodesCodeidJsonBodyRAWBODYItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        raw_body: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.raw_body, Unset):
            raw_body = []
            for raw_body_item_data in self.raw_body:
                raw_body_item = raw_body_item_data.to_dict()

                raw_body.append(raw_body_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if raw_body is not UNSET:
            field_dict["RAW_BODY"] = raw_body

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        raw_body = []
        _raw_body = d.pop("RAW_BODY", UNSET)
        for raw_body_item_data in _raw_body or []:
            raw_body_item = PatchCodesCodeidJsonBodyRAWBODYItem.from_dict(raw_body_item_data)

            raw_body.append(raw_body_item)

        patch_codes_codeid_json_body = cls(
            raw_body=raw_body,
        )

        patch_codes_codeid_json_body.additional_properties = d
        return patch_codes_codeid_json_body

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
