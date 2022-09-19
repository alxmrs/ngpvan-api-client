from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Events2Response201NotesItem")


@attr.s(auto_attribs=True)
class Events2Response201NotesItem:
    """
    Attributes:
        text (Union[Unset, str]):  Example: Lorem ipsum dolor sit amet, consectetur adipiscing elit....
        is_view_restricted (Union[Unset, bool]):  Default: True. Example: True.
    """

    text: Union[Unset, str] = UNSET
    is_view_restricted: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        is_view_restricted = self.is_view_restricted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if is_view_restricted is not UNSET:
            field_dict["isViewRestricted"] = is_view_restricted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        is_view_restricted = d.pop("isViewRestricted", UNSET)

        events_2_response_201_notes_item = cls(
            text=text,
            is_view_restricted=is_view_restricted,
        )

        events_2_response_201_notes_item.additional_properties = d
        return events_2_response_201_notes_item

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
