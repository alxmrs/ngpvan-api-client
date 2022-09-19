from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodesCodeidGetSourceCodeWithExpandCostCenter")


@attr.s(auto_attribs=True)
class CodesCodeidGetSourceCodeWithExpandCostCenter:
    """
    Attributes:
        cost_center_id (Union[Unset, int]):  Example: 47.
        name (Union[Unset, str]):  Example: API Cost Center for Tests.
        description (Union[Unset, str]):  Example: Cost Center for API Tests (Source Codes).
        is_active (Union[Unset, bool]):  Default: True. Example: True.
    """

    cost_center_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cost_center_id = self.cost_center_id
        name = self.name
        description = self.description
        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cost_center_id is not UNSET:
            field_dict["costCenterId"] = cost_center_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cost_center_id = d.pop("costCenterId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_active = d.pop("isActive", UNSET)

        codes_codeid_get_source_code_with_expand_cost_center = cls(
            cost_center_id=cost_center_id,
            name=name,
            description=description,
            is_active=is_active,
        )

        codes_codeid_get_source_code_with_expand_cost_center.additional_properties = d
        return codes_codeid_get_source_code_with_expand_cost_center

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
