from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.worksites_1_response_200_items_item_address import Worksites1Response200ItemsItemAddress
from ..models.worksites_1_response_200_items_item_employer import Worksites1Response200ItemsItemEmployer
from ..types import UNSET, Unset

T = TypeVar("T", bound="Worksites1Response200ItemsItem")


@attr.s(auto_attribs=True)
class Worksites1Response200ItemsItem:
    """
    Attributes:
        worksite_id (Union[Unset, int]):  Example: 124.
        name (Union[Unset, str]):  Example: Forestdale School.
        is_preferred (Union[Unset, bool]):  Default: True. Example: True.
        address (Union[Unset, Worksites1Response200ItemsItemAddress]):
        employer (Union[Unset, Worksites1Response200ItemsItemEmployer]):
        work_areas (Union[Unset, Any]):
    """

    worksite_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    is_preferred: Union[Unset, bool] = True
    address: Union[Unset, Worksites1Response200ItemsItemAddress] = UNSET
    employer: Union[Unset, Worksites1Response200ItemsItemEmployer] = UNSET
    work_areas: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        worksite_id = self.worksite_id
        name = self.name
        is_preferred = self.is_preferred
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        employer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.employer, Unset):
            employer = self.employer.to_dict()

        work_areas = self.work_areas

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
        if employer is not UNSET:
            field_dict["employer"] = employer
        if work_areas is not UNSET:
            field_dict["workAreas"] = work_areas

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        worksite_id = d.pop("worksiteId", UNSET)

        name = d.pop("name", UNSET)

        is_preferred = d.pop("isPreferred", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Worksites1Response200ItemsItemAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Worksites1Response200ItemsItemAddress.from_dict(_address)

        _employer = d.pop("employer", UNSET)
        employer: Union[Unset, Worksites1Response200ItemsItemEmployer]
        if isinstance(_employer, Unset):
            employer = UNSET
        else:
            employer = Worksites1Response200ItemsItemEmployer.from_dict(_employer)

        work_areas = d.pop("workAreas", UNSET)

        worksites_1_response_200_items_item = cls(
            worksite_id=worksite_id,
            name=name,
            is_preferred=is_preferred,
            address=address,
            employer=employer,
            work_areas=work_areas,
        )

        worksites_1_response_200_items_item.additional_properties = d
        return worksites_1_response_200_items_item

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
