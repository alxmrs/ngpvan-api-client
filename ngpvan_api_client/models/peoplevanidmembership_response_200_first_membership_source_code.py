from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidmembershipResponse200FirstMembershipSourceCode")


@attr.s(auto_attribs=True)
class PeoplevanidmembershipResponse200FirstMembershipSourceCode:
    """
    Attributes:
        code_id (Union[Unset, int]):  Example: 123456.
        code_name (Union[Unset, str]):  Example: Acquisition.
    """

    code_id: Union[Unset, int] = 0
    code_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code_id = self.code_id
        code_name = self.code_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code_id is not UNSET:
            field_dict["codeId"] = code_id
        if code_name is not UNSET:
            field_dict["codeName"] = code_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code_id = d.pop("codeId", UNSET)

        code_name = d.pop("codeName", UNSET)

        peoplevanidmembership_response_200_first_membership_source_code = cls(
            code_id=code_id,
            code_name=code_name,
        )

        peoplevanidmembership_response_200_first_membership_source_code.additional_properties = d
        return peoplevanidmembership_response_200_first_membership_source_code

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
