from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Bargainingunits1JsonBody")


@attr.s(auto_attribs=True)
class Bargainingunits1JsonBody:
    """
    Attributes:
        name (Union[Unset, str]): Required; name for the Bargaining Unit Default: 'Healthcare Professionals'.
        short_name (Union[Unset, str]): Required; short name for the Bargaining Unit Default: 'Healthcare Prof'.
    """

    name: Union[Unset, str] = "Healthcare Professionals"
    short_name: Union[Unset, str] = "Healthcare Prof"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        bargainingunits_1_json_body = cls(
            name=name,
            short_name=short_name,
        )

        bargainingunits_1_json_body.additional_properties = d
        return bargainingunits_1_json_body

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
