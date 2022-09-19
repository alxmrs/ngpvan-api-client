from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.employersemployeridbargainingunitsbargainingunitid_response_201_bargaining_unit import (
    EmployersemployeridbargainingunitsbargainingunitidResponse201BargainingUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployersemployeridbargainingunitsbargainingunitidResponse201")


@attr.s(auto_attribs=True)
class EmployersemployeridbargainingunitsbargainingunitidResponse201:
    """
    Attributes:
        employer_bargaining_unit_id (Union[Unset, int]):  Example: 98.
        bargaining_unit (Union[Unset, EmployersemployeridbargainingunitsbargainingunitidResponse201BargainingUnit]):
    """

    employer_bargaining_unit_id: Union[Unset, int] = 0
    bargaining_unit: Union[Unset, EmployersemployeridbargainingunitsbargainingunitidResponse201BargainingUnit] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employer_bargaining_unit_id = self.employer_bargaining_unit_id
        bargaining_unit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bargaining_unit, Unset):
            bargaining_unit = self.bargaining_unit.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employer_bargaining_unit_id is not UNSET:
            field_dict["employerBargainingUnitId"] = employer_bargaining_unit_id
        if bargaining_unit is not UNSET:
            field_dict["bargainingUnit"] = bargaining_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        employer_bargaining_unit_id = d.pop("employerBargainingUnitId", UNSET)

        _bargaining_unit = d.pop("bargainingUnit", UNSET)
        bargaining_unit: Union[Unset, EmployersemployeridbargainingunitsbargainingunitidResponse201BargainingUnit]
        if isinstance(_bargaining_unit, Unset):
            bargaining_unit = UNSET
        else:
            bargaining_unit = EmployersemployeridbargainingunitsbargainingunitidResponse201BargainingUnit.from_dict(
                _bargaining_unit
            )

        employersemployeridbargainingunitsbargainingunitid_response_201 = cls(
            employer_bargaining_unit_id=employer_bargaining_unit_id,
            bargaining_unit=bargaining_unit,
        )

        employersemployeridbargainingunitsbargainingunitid_response_201.additional_properties = d
        return employersemployeridbargainingunitsbargainingunitid_response_201

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
