from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.employersemployeridworksites_json_body_worksite import EmployersemployeridworksitesJsonBodyWorksite
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployersemployeridworksitesJsonBody")


@attr.s(auto_attribs=True)
class EmployersemployeridworksitesJsonBody:
    """
    Attributes:
        worksite (Union[Unset, EmployersemployeridworksitesJsonBodyWorksite]): Accepts a standard
            [Worksite](https://everyaction.readme.io/reference#common-models-16) object with no read-only values specified.
            If supplied, the name of the Worksite must be unique to the Employer.
    """

    worksite: Union[Unset, EmployersemployeridworksitesJsonBodyWorksite] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worksite: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.worksite, Unset):
            worksite = self.worksite.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if worksite is not UNSET:
            field_dict["worksite"] = worksite

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _worksite = d.pop("worksite", UNSET)
        worksite: Union[Unset, EmployersemployeridworksitesJsonBodyWorksite]
        if isinstance(_worksite, Unset):
            worksite = UNSET
        else:
            worksite = EmployersemployeridworksitesJsonBodyWorksite.from_dict(_worksite)

        employersemployeridworksites_json_body = cls(
            worksite=worksite,
        )

        employersemployeridworksites_json_body.additional_properties = d
        return employersemployeridworksites_json_body

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
