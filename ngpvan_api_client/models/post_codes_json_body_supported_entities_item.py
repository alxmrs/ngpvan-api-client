from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCodesJsonBodySupportedEntitiesItem")


@attr.s(auto_attribs=True)
class PostCodesJsonBodySupportedEntitiesItem:
    """
    Attributes:
        name (Union[Unset, str]):  Default: 'Events'.
        is_searchable (Union[Unset, bool]):  Default: True.
        is_applicable (Union[Unset, bool]):  Default: True.
    """

    name: Union[Unset, str] = "Events"
    is_searchable: Union[Unset, bool] = True
    is_applicable: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_searchable = self.is_searchable
        is_applicable = self.is_applicable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if is_searchable is not UNSET:
            field_dict["isSearchable"] = is_searchable
        if is_applicable is not UNSET:
            field_dict["isApplicable"] = is_applicable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        is_searchable = d.pop("isSearchable", UNSET)

        is_applicable = d.pop("isApplicable", UNSET)

        post_codes_json_body_supported_entities_item = cls(
            name=name,
            is_searchable=is_searchable,
            is_applicable=is_applicable,
        )

        post_codes_json_body_supported_entities_item.additional_properties = d
        return post_codes_json_body_supported_entities_item

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
