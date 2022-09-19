import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContributionscontributionidattributionsvanidJsonBody")


@attr.s(auto_attribs=True)
class ContributionscontributionidattributionsvanidJsonBody:
    """
    Attributes:
        van_id (Union[Unset, str]): Unique identifier for the attributed contact. Represents contacts who acted as
            fundraisers, rather than contributors. Default: '215501'.
        amount_attributed (Union[Unset, str]): Optional; The amount of the attribution. Values that have more than 2
            digits after the decimal point will not be accepted. If no amount is provided, default to contribution amount.
            Default: '100.00'.
        attribution_type (Union[Unset, str]): Optional; A string representing the attribution type. See below for valid
            values of Attribution Type. If no type is provided, default to “DefaultAttribution” type Default:
            'BoardMemberGiving'.
        date_thanked (Union[Unset, datetime.date]): Optional; The date on which the attributed contact was thanked for
            the contribution. Default: isoparse('2019-10-08').date().
        notes (Union[Unset, str]): Optional; A note describing the attribution. Max length of 100 characters. Default:
            'This will be created or updated'.
    """

    van_id: Union[Unset, str] = "215501"
    amount_attributed: Union[Unset, str] = "100.00"
    attribution_type: Union[Unset, str] = "BoardMemberGiving"
    date_thanked: Union[Unset, datetime.date] = isoparse("2019-10-08").date()
    notes: Union[Unset, str] = "This will be created or updated"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        van_id = self.van_id
        amount_attributed = self.amount_attributed
        attribution_type = self.attribution_type
        date_thanked: Union[Unset, str] = UNSET
        if not isinstance(self.date_thanked, Unset):
            date_thanked = self.date_thanked.isoformat()

        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if van_id is not UNSET:
            field_dict["vanId"] = van_id
        if amount_attributed is not UNSET:
            field_dict["amountAttributed"] = amount_attributed
        if attribution_type is not UNSET:
            field_dict["attributionType"] = attribution_type
        if date_thanked is not UNSET:
            field_dict["dateThanked"] = date_thanked
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        van_id = d.pop("vanId", UNSET)

        amount_attributed = d.pop("amountAttributed", UNSET)

        attribution_type = d.pop("attributionType", UNSET)

        _date_thanked = d.pop("dateThanked", UNSET)
        date_thanked: Union[Unset, datetime.date]
        if isinstance(_date_thanked, Unset):
            date_thanked = UNSET
        else:
            date_thanked = isoparse(_date_thanked).date()

        notes = d.pop("notes", UNSET)

        contributionscontributionidattributionsvanid_json_body = cls(
            van_id=van_id,
            amount_attributed=amount_attributed,
            attribution_type=attribution_type,
            date_thanked=date_thanked,
            notes=notes,
        )

        contributionscontributionidattributionsvanid_json_body.additional_properties = d
        return contributionscontributionidattributionsvanid_json_body

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
