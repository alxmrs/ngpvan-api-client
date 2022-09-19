from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Usersuseriddistrictfieldvalues2Response200")


@attr.s(auto_attribs=True)
class Usersuseriddistrictfieldvalues2Response200:
    """
    Attributes:
        district_field_values (Union[Unset, List[str]]):
    """

    district_field_values: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        district_field_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.district_field_values, Unset):
            district_field_values = self.district_field_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district_field_values is not UNSET:
            field_dict["districtFieldValues"] = district_field_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        district_field_values = cast(List[str], d.pop("districtFieldValues", UNSET))

        usersuseriddistrictfieldvalues_2_response_200 = cls(
            district_field_values=district_field_values,
        )

        usersuseriddistrictfieldvalues_2_response_200.additional_properties = d
        return usersuseriddistrictfieldvalues_2_response_200

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
