from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Voterregistrationbatches1JsonBodyForm")


@attr.s(auto_attribs=True)
class Voterregistrationbatches1JsonBodyForm:
    """
    Attributes:
        form_id (Union[Unset, int]):  Default: 101.
    """

    form_id: Union[Unset, int] = 101
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        form_id = self.form_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if form_id is not UNSET:
            field_dict["formId"] = form_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        form_id = d.pop("formId", UNSET)

        voterregistrationbatches_1_json_body_form = cls(
            form_id=form_id,
        )

        voterregistrationbatches_1_json_body_form.additional_properties = d
        return voterregistrationbatches_1_json_body_form

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
