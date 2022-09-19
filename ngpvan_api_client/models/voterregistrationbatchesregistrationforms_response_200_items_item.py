from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoterregistrationbatchesregistrationformsResponse200ItemsItem")


@attr.s(auto_attribs=True)
class VoterregistrationbatchesregistrationformsResponse200ItemsItem:
    """
    Attributes:
        form_id (Union[Unset, int]):  Example: 101.
        name (Union[Unset, str]):  Example: VR Form.
    """

    form_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        form_id = self.form_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if form_id is not UNSET:
            field_dict["formId"] = form_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        form_id = d.pop("formId", UNSET)

        name = d.pop("name", UNSET)

        voterregistrationbatchesregistrationforms_response_200_items_item = cls(
            form_id=form_id,
            name=name,
        )

        voterregistrationbatchesregistrationforms_response_200_items_item.additional_properties = d
        return voterregistrationbatchesregistrationforms_response_200_items_item

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
