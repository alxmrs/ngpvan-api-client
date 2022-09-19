from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.voterregistrationbatchesbatchidpeople_json_body_registrants_item import (
    VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoterregistrationbatchesbatchidpeopleJsonBody")


@attr.s(auto_attribs=True)
class VoterregistrationbatchesbatchidpeopleJsonBody:
    """
    Attributes:
        registrants (Union[Unset, List[VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItem]]):
    """

    registrants: Union[Unset, List[VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        registrants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.registrants, Unset):
            registrants = []
            for registrants_item_data in self.registrants:
                registrants_item = registrants_item_data.to_dict()

                registrants.append(registrants_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if registrants is not UNSET:
            field_dict["registrants"] = registrants

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        registrants = []
        _registrants = d.pop("registrants", UNSET)
        for registrants_item_data in _registrants or []:
            registrants_item = VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItem.from_dict(
                registrants_item_data
            )

            registrants.append(registrants_item)

        voterregistrationbatchesbatchidpeople_json_body = cls(
            registrants=registrants,
        )

        voterregistrationbatchesbatchidpeople_json_body.additional_properties = d
        return voterregistrationbatchesbatchidpeople_json_body

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
