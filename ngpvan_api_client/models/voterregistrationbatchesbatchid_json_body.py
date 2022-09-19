from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoterregistrationbatchesbatchidJsonBody")


@attr.s(auto_attribs=True)
class VoterregistrationbatchesbatchidJsonBody:
    """
    Attributes:
        status (Union[Unset, str]):  Default: 'Completed'.
    """

    status: Union[Unset, str] = "Completed"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = d.pop("status", UNSET)

        voterregistrationbatchesbatchid_json_body = cls(
            status=status,
        )

        voterregistrationbatchesbatchid_json_body.additional_properties = d
        return voterregistrationbatchesbatchid_json_body

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
