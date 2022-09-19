from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberstatusesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class MemberstatusesResponse200ItemsItem:
    """
    Attributes:
        member_status_id (Union[Unset, int]):  Example: 123.
        name (Union[Unset, str]):  Example: Active Retired.
        is_member (Union[Unset, bool]):  Default: True. Example: True.
    """

    member_status_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    is_member: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        member_status_id = self.member_status_id
        name = self.name
        is_member = self.is_member

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member_status_id is not UNSET:
            field_dict["memberStatusId"] = member_status_id
        if name is not UNSET:
            field_dict["name"] = name
        if is_member is not UNSET:
            field_dict["isMember"] = is_member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        member_status_id = d.pop("memberStatusId", UNSET)

        name = d.pop("name", UNSET)

        is_member = d.pop("isMember", UNSET)

        memberstatuses_response_200_items_item = cls(
            member_status_id=member_status_id,
            name=name,
            is_member=is_member,
        )

        memberstatuses_response_200_items_item.additional_properties = d
        return memberstatuses_response_200_items_item

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
