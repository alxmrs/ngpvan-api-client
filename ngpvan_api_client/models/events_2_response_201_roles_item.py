from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Events2Response201RolesItem")


@attr.s(auto_attribs=True)
class Events2Response201RolesItem:
    """
    Attributes:
        role_id (Union[Unset, int]):  Example: 111687.
        name (Union[Unset, str]):  Example: Host.
        is_event_lead (Union[Unset, bool]):  Default: True. Example: True.
    """

    role_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    is_event_lead: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role_id = self.role_id
        name = self.name
        is_event_lead = self.is_event_lead

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if name is not UNSET:
            field_dict["name"] = name
        if is_event_lead is not UNSET:
            field_dict["isEventLead"] = is_event_lead

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role_id = d.pop("roleId", UNSET)

        name = d.pop("name", UNSET)

        is_event_lead = d.pop("isEventLead", UNSET)

        events_2_response_201_roles_item = cls(
            role_id=role_id,
            name=name,
            is_event_lead=is_event_lead,
        )

        events_2_response_201_roles_item.additional_properties = d
        return events_2_response_201_roles_item

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
