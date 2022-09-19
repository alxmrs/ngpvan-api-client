from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Contributions1JsonBodyDesignation")


@attr.s(auto_attribs=True)
class Contributions1JsonBodyDesignation:
    """The financial entity which will receive this contribution.

    Attributes:
        designation_id (Union[Unset, int]):  Default: 18754.
    """

    designation_id: Union[Unset, int] = 18754
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        designation_id = self.designation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if designation_id is not UNSET:
            field_dict["designationId"] = designation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        designation_id = d.pop("designationId", UNSET)

        contributions_1_json_body_designation = cls(
            designation_id=designation_id,
        )

        contributions_1_json_body_designation.additional_properties = d
        return contributions_1_json_body_designation

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
