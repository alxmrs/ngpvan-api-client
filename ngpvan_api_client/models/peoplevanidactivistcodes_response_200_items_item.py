from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidactivistcodesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class PeoplevanidactivistcodesResponse200ItemsItem:
    """
    Attributes:
        activist_code_id (Union[Unset, int]):  Example: 3214.
        activist_code_name (Union[Unset, str]):  Example: Precinct Captain.
        date_created (Union[Unset, str]):  Example: 2019-05-28T08:45:00Z.
        canvassed_by (Union[Unset, Any]):
        date_canvassed (Union[Unset, str]):  Example: 2019-05-28T08:45:00Z.
    """

    activist_code_id: Union[Unset, int] = 0
    activist_code_name: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    canvassed_by: Union[Unset, Any] = UNSET
    date_canvassed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activist_code_id = self.activist_code_id
        activist_code_name = self.activist_code_name
        date_created = self.date_created
        canvassed_by = self.canvassed_by
        date_canvassed = self.date_canvassed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activist_code_id is not UNSET:
            field_dict["activistCodeId"] = activist_code_id
        if activist_code_name is not UNSET:
            field_dict["activistCodeName"] = activist_code_name
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if canvassed_by is not UNSET:
            field_dict["canvassedBy"] = canvassed_by
        if date_canvassed is not UNSET:
            field_dict["dateCanvassed"] = date_canvassed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        activist_code_id = d.pop("activistCodeId", UNSET)

        activist_code_name = d.pop("activistCodeName", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        canvassed_by = d.pop("canvassedBy", UNSET)

        date_canvassed = d.pop("dateCanvassed", UNSET)

        peoplevanidactivistcodes_response_200_items_item = cls(
            activist_code_id=activist_code_id,
            activist_code_name=activist_code_name,
            date_created=date_created,
            canvassed_by=canvassed_by,
            date_canvassed=date_canvassed,
        )

        peoplevanidactivistcodes_response_200_items_item.additional_properties = d
        return peoplevanidactivistcodes_response_200_items_item

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
