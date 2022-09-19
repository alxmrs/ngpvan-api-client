from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.employers_2_json_body_employer import Employers2JsonBodyEmployer
from ..types import UNSET, Unset

T = TypeVar("T", bound="Employers2JsonBody")


@attr.s(auto_attribs=True)
class Employers2JsonBody:
    """
    Attributes:
        employer (Union[Unset, Employers2JsonBodyEmployer]): Accepts a standard Employer object with no read-only values
            specified.
    """

    employer: Union[Unset, Employers2JsonBodyEmployer] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employer, Unset):
            employer = self.employer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employer is not UNSET:
            field_dict["employer"] = employer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _employer = d.pop("employer", UNSET)
        employer: Union[Unset, Employers2JsonBodyEmployer]
        if isinstance(_employer, Unset):
            employer = UNSET
        else:
            employer = Employers2JsonBodyEmployer.from_dict(_employer)

        employers_2_json_body = cls(
            employer=employer,
        )

        employers_2_json_body.additional_properties = d
        return employers_2_json_body

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
