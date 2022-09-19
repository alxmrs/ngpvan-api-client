from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Employersemployerid1JsonBody")


@attr.s(auto_attribs=True)
class Employersemployerid1JsonBody:
    """
    Attributes:
        is_my_organization (Union[Unset, bool]): The new `isMyOrganization` status Default: True.
    """

    is_my_organization: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_my_organization = self.is_my_organization

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_my_organization is not UNSET:
            field_dict["isMyOrganization"] = is_my_organization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_my_organization = d.pop("isMyOrganization", UNSET)

        employersemployerid_1_json_body = cls(
            is_my_organization=is_my_organization,
        )

        employersemployerid_1_json_body.additional_properties = d
        return employersemployerid_1_json_body

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
