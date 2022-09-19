from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201BargainingUnit"
)


@attr.s(auto_attribs=True)
class EmployersemployeridbargainingunitsbargainingunitidjobclassesjobclassidResponse201BargainingUnit:
    """
    Attributes:
        bargaining_unit_id (Union[Unset, int]):  Example: 35.
        name (Union[Unset, str]):  Example: Maintenance.
    """

    bargaining_unit_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bargaining_unit_id = self.bargaining_unit_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bargaining_unit_id is not UNSET:
            field_dict["bargainingUnitId"] = bargaining_unit_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bargaining_unit_id = d.pop("bargainingUnitId", UNSET)

        name = d.pop("name", UNSET)

        employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_201_bargaining_unit = cls(
            bargaining_unit_id=bargaining_unit_id,
            name=name,
        )

        employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_201_bargaining_unit.additional_properties = (
            d
        )
        return employersemployeridbargainingunitsbargainingunitidjobclassesjobclassid_response_201_bargaining_unit

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
