from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="EmployersemployeridworksitesJsonBodyWorksite")


@attr.s(auto_attribs=True)
class EmployersemployeridworksitesJsonBodyWorksite:
    """Accepts a standard [Worksite](https://everyaction.readme.io/reference#common-models-16) object with no read-only
    values specified. If supplied, the name of the Worksite must be unique to the Employer.

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        employersemployeridworksites_json_body_worksite = cls()

        employersemployeridworksites_json_body_worksite.additional_properties = d
        return employersemployeridworksites_json_body_worksite

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
