from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContributionsattributiontypesResponse200Item")


@attr.s(auto_attribs=True)
class ContributionsattributiontypesResponse200Item:
    """
    Attributes:
        van_id (Union[Unset, int]):  Example: 303.
        amount_attributed (Union[Unset, str]):  Example: 100.50.
        attribution_type (Union[Unset, str]):  Example: DefaultAttribution.
        notes (Union[Unset, str]):  Example: some notes go here.
        date_thanked (Union[Unset, str]):  Example: 2013-12-30.
    """

    van_id: Union[Unset, int] = 0
    amount_attributed: Union[Unset, str] = UNSET
    attribution_type: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    date_thanked: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        van_id = self.van_id
        amount_attributed = self.amount_attributed
        attribution_type = self.attribution_type
        notes = self.notes
        date_thanked = self.date_thanked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if van_id is not UNSET:
            field_dict["vanId"] = van_id
        if amount_attributed is not UNSET:
            field_dict["amountAttributed"] = amount_attributed
        if attribution_type is not UNSET:
            field_dict["attributionType"] = attribution_type
        if notes is not UNSET:
            field_dict["notes"] = notes
        if date_thanked is not UNSET:
            field_dict["dateThanked"] = date_thanked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        van_id = d.pop("vanId", UNSET)

        amount_attributed = d.pop("amountAttributed", UNSET)

        attribution_type = d.pop("attributionType", UNSET)

        notes = d.pop("notes", UNSET)

        date_thanked = d.pop("dateThanked", UNSET)

        contributionsattributiontypes_response_200_item = cls(
            van_id=van_id,
            amount_attributed=amount_attributed,
            attribution_type=attribution_type,
            notes=notes,
            date_thanked=date_thanked,
        )

        contributionsattributiontypes_response_200_item.additional_properties = d
        return contributionsattributiontypes_response_200_item

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
