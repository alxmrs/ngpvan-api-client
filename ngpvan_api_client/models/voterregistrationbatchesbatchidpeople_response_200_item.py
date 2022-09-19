from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoterregistrationbatchesbatchidpeopleResponse200Item")


@attr.s(auto_attribs=True)
class VoterregistrationbatchesbatchidpeopleResponse200Item:
    """
    Attributes:
        alternate_id (Union[Unset, str]):  Example: ab694282-1d74-474b-90dc-173aa73f44b1.
        van_id (Union[Unset, str]):  Example: 10000000.
        result (Union[Unset, str]):  Example: Success.
        errors (Union[Unset, Any]):
    """

    alternate_id: Union[Unset, str] = UNSET
    van_id: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    errors: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alternate_id = self.alternate_id
        van_id = self.van_id
        result = self.result
        errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alternate_id is not UNSET:
            field_dict["alternateId"] = alternate_id
        if van_id is not UNSET:
            field_dict["vanId"] = van_id
        if result is not UNSET:
            field_dict["result"] = result
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alternate_id = d.pop("alternateId", UNSET)

        van_id = d.pop("vanId", UNSET)

        result = d.pop("result", UNSET)

        errors = d.pop("errors", UNSET)

        voterregistrationbatchesbatchidpeople_response_200_item = cls(
            alternate_id=alternate_id,
            van_id=van_id,
            result=result,
            errors=errors,
        )

        voterregistrationbatchesbatchidpeople_response_200_item.additional_properties = d
        return voterregistrationbatchesbatchidpeople_response_200_item

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
