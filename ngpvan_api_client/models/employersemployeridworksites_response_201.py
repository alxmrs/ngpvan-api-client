from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.employersemployeridworksites_response_201_address import EmployersemployeridworksitesResponse201Address
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmployersemployeridworksitesResponse201")


@attr.s(auto_attribs=True)
class EmployersemployeridworksitesResponse201:
    """
    Attributes:
        worksite_id (Union[Unset, int]):  Example: 321.
        name (Union[Unset, str]):  Example: Administration.
        is_preferred (Union[Unset, bool]):  Default: True. Example: True.
        address (Union[Unset, EmployersemployeridworksitesResponse201Address]):
    """

    worksite_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    is_preferred: Union[Unset, bool] = True
    address: Union[Unset, EmployersemployeridworksitesResponse201Address] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worksite_id = self.worksite_id
        name = self.name
        is_preferred = self.is_preferred
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if worksite_id is not UNSET:
            field_dict["worksiteId"] = worksite_id
        if name is not UNSET:
            field_dict["name"] = name
        if is_preferred is not UNSET:
            field_dict["isPreferred"] = is_preferred
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        worksite_id = d.pop("worksiteId", UNSET)

        name = d.pop("name", UNSET)

        is_preferred = d.pop("isPreferred", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, EmployersemployeridworksitesResponse201Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = EmployersemployeridworksitesResponse201Address.from_dict(_address)

        employersemployeridworksites_response_201 = cls(
            worksite_id=worksite_id,
            name=name,
            is_preferred=is_preferred,
            address=address,
        )

        employersemployeridworksites_response_201.additional_properties = d
        return employersemployeridworksites_response_201

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
