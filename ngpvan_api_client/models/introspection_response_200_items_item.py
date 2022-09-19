from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntrospectionResponse200ItemsItem")


@attr.s(auto_attribs=True)
class IntrospectionResponse200ItemsItem:
    """
    Attributes:
        database_name (Union[Unset, str]):  Example: SmartVAN Massachusetts.
        has_my_voters (Union[Unset, bool]):  Default: True. Example: True.
        has_my_campaign (Union[Unset, bool]):  Default: True. Example: True.
        committee_name (Union[Unset, str]):  Example: People for Good.
        api_key_type_name (Union[Unset, str]):  Example: Custom Integration.
        key_reference (Union[Unset, str]):  Example: 1234.
        user_first_name (Union[Unset, str]):  Example: peopleforgood.
        user_last_name (Union[Unset, str]):  Example: api.
        username (Union[Unset, str]):  Example: peopleforgood.api.
    """

    database_name: Union[Unset, str] = UNSET
    has_my_voters: Union[Unset, bool] = True
    has_my_campaign: Union[Unset, bool] = True
    committee_name: Union[Unset, str] = UNSET
    api_key_type_name: Union[Unset, str] = UNSET
    key_reference: Union[Unset, str] = UNSET
    user_first_name: Union[Unset, str] = UNSET
    user_last_name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        database_name = self.database_name
        has_my_voters = self.has_my_voters
        has_my_campaign = self.has_my_campaign
        committee_name = self.committee_name
        api_key_type_name = self.api_key_type_name
        key_reference = self.key_reference
        user_first_name = self.user_first_name
        user_last_name = self.user_last_name
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if database_name is not UNSET:
            field_dict["databaseName"] = database_name
        if has_my_voters is not UNSET:
            field_dict["hasMyVoters"] = has_my_voters
        if has_my_campaign is not UNSET:
            field_dict["hasMyCampaign"] = has_my_campaign
        if committee_name is not UNSET:
            field_dict["committeeName"] = committee_name
        if api_key_type_name is not UNSET:
            field_dict["apiKeyTypeName"] = api_key_type_name
        if key_reference is not UNSET:
            field_dict["keyReference"] = key_reference
        if user_first_name is not UNSET:
            field_dict["userFirstName"] = user_first_name
        if user_last_name is not UNSET:
            field_dict["userLastName"] = user_last_name
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        database_name = d.pop("databaseName", UNSET)

        has_my_voters = d.pop("hasMyVoters", UNSET)

        has_my_campaign = d.pop("hasMyCampaign", UNSET)

        committee_name = d.pop("committeeName", UNSET)

        api_key_type_name = d.pop("apiKeyTypeName", UNSET)

        key_reference = d.pop("keyReference", UNSET)

        user_first_name = d.pop("userFirstName", UNSET)

        user_last_name = d.pop("userLastName", UNSET)

        username = d.pop("username", UNSET)

        introspection_response_200_items_item = cls(
            database_name=database_name,
            has_my_voters=has_my_voters,
            has_my_campaign=has_my_campaign,
            committee_name=committee_name,
            api_key_type_name=api_key_type_name,
            key_reference=key_reference,
            user_first_name=user_first_name,
            user_last_name=user_last_name,
            username=username,
        )

        introspection_response_200_items_item.additional_properties = d
        return introspection_response_200_items_item

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
