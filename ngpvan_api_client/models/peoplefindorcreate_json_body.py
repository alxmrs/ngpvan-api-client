import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplefindorcreateJsonBody")


@attr.s(auto_attribs=True)
class PeoplefindorcreateJsonBody:
    """
    Attributes:
        van_id (Union[Unset, str]):  Default: '100476252'.
        first_name (Union[Unset, str]):  Default: 'James'.
        last_name (Union[Unset, str]):  Default: 'Gordon'.
        date_of_birth (Union[Unset, datetime.date]):
    """

    van_id: Union[Unset, str] = "100476252"
    first_name: Union[Unset, str] = "James"
    last_name: Union[Unset, str] = "Gordon"
    date_of_birth: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        van_id = self.van_id
        first_name = self.first_name
        last_name = self.last_name
        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if van_id is not UNSET:
            field_dict["vanId"] = van_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        van_id = d.pop("vanId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, datetime.date]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth).date()

        peoplefindorcreate_json_body = cls(
            van_id=van_id,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
        )

        peoplefindorcreate_json_body.additional_properties = d
        return peoplefindorcreate_json_body

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
