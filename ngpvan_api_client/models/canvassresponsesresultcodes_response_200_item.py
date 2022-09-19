from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CanvassresponsesresultcodesResponse200Item")


@attr.s(auto_attribs=True)
class CanvassresponsesresultcodesResponse200Item:
    """
    Attributes:
        result_code_id (Union[Unset, int]):  Example: 18.
        name (Union[Unset, str]):  Example: Busy.
        medium_name (Union[Unset, str]):  Example: Busy.
        short_name (Union[Unset, str]):  Example: BZ.
    """

    result_code_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    medium_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_code_id = self.result_code_id
        name = self.name
        medium_name = self.medium_name
        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_code_id is not UNSET:
            field_dict["resultCodeId"] = result_code_id
        if name is not UNSET:
            field_dict["name"] = name
        if medium_name is not UNSET:
            field_dict["mediumName"] = medium_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        result_code_id = d.pop("resultCodeId", UNSET)

        name = d.pop("name", UNSET)

        medium_name = d.pop("mediumName", UNSET)

        short_name = d.pop("shortName", UNSET)

        canvassresponsesresultcodes_response_200_item = cls(
            result_code_id=result_code_id,
            name=name,
            medium_name=medium_name,
            short_name=short_name,
        )

        canvassresponsesresultcodes_response_200_item.additional_properties = d
        return canvassresponsesresultcodes_response_200_item

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
