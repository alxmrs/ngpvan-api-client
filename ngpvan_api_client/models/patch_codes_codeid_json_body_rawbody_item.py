from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.patch_codes_codeid_json_body_rawbody_item_op import PatchCodesCodeidJsonBodyRAWBODYItemOp
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchCodesCodeidJsonBodyRAWBODYItem")


@attr.s(auto_attribs=True)
class PatchCodesCodeidJsonBodyRAWBODYItem:
    """
    Attributes:
        op (PatchCodesCodeidJsonBodyRAWBODYItemOp): The operation to perform on the target document
        path (str): A JSON Pointer to the specific property in the document to operate on. Uses [RFC
            6901](https://datatracker.ietf.org/doc/html/rfc6901/).
        value (Union[Unset, str]): Value of the same type as `path`. Required for `add`, `replace`, and `test`
            operations.
        from_ (Union[Unset, str]): A JSON Pointer to a specific property in the document. Required for `copy` and `move`
            operations.
    """

    op: PatchCodesCodeidJsonBodyRAWBODYItemOp
    path: str
    value: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        op = self.op.value

        path = self.path
        value = self.value
        from_ = self.from_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "path": path,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        op = PatchCodesCodeidJsonBodyRAWBODYItemOp(d.pop("op"))

        path = d.pop("path")

        value = d.pop("value", UNSET)

        from_ = d.pop("from", UNSET)

        patch_codes_codeid_json_body_rawbody_item = cls(
            op=op,
            path=path,
            value=value,
            from_=from_,
        )

        patch_codes_codeid_json_body_rawbody_item.additional_properties = d
        return patch_codes_codeid_json_body_rawbody_item

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
