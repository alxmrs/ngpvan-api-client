from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodesCodeidGetSourceCodeWithExpandContactType")


@attr.s(auto_attribs=True)
class CodesCodeidGetSourceCodeWithExpandContactType:
    """
    Attributes:
        contact_type_id (Union[Unset, int]):  Example: 82.
        channel_type_name (Union[Unset, str]):  Example: Mail.
        name (Union[Unset, str]):  Example: Direct Mail.
    """

    contact_type_id: Union[Unset, int] = 0
    channel_type_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact_type_id = self.contact_type_id
        channel_type_name = self.channel_type_name
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_type_id is not UNSET:
            field_dict["contactTypeId"] = contact_type_id
        if channel_type_name is not UNSET:
            field_dict["channelTypeName"] = channel_type_name
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact_type_id = d.pop("contactTypeId", UNSET)

        channel_type_name = d.pop("channelTypeName", UNSET)

        name = d.pop("name", UNSET)

        codes_codeid_get_source_code_with_expand_contact_type = cls(
            contact_type_id=contact_type_id,
            channel_type_name=channel_type_name,
            name=name,
        )

        codes_codeid_get_source_code_with_expand_contact_type.additional_properties = d
        return codes_codeid_get_source_code_with_expand_contact_type

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
