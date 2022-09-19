from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmssyncResponse200")


@attr.s(auto_attribs=True)
class SmssyncResponse200:
    """
    Attributes:
        saved_list_id (Union[Unset, int]):  Example: 123.
    """

    saved_list_id: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        saved_list_id = self.saved_list_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if saved_list_id is not UNSET:
            field_dict["savedListId"] = saved_list_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        saved_list_id = d.pop("savedListId", UNSET)

        smssync_response_200 = cls(
            saved_list_id=saved_list_id,
        )

        smssync_response_200.additional_properties = d
        return smssync_response_200

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
