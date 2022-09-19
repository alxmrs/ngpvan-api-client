from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_campaigns_response_200_items_item_campaign_type import GetCampaignsResponse200ItemsItemCampaignType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCampaignsResponse200ItemsItem")


@attr.s(auto_attribs=True)
class GetCampaignsResponse200ItemsItem:
    """
    Attributes:
        campaign_id (Union[Unset, int]):  Example: 7919.
        name (Union[Unset, str]):  Example: Increase the Minimum Wage.
        campaign_type (Union[Unset, GetCampaignsResponse200ItemsItemCampaignType]):
        campaign_display_name (Union[Unset, str]):  Example: Advocacy: Increase the Minimum Wage.
        status (Union[Unset, str]):  Example: Active.
        contents (Union[Unset, Any]):
    """

    campaign_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    campaign_type: Union[Unset, GetCampaignsResponse200ItemsItemCampaignType] = UNSET
    campaign_display_name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    contents: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        campaign_id = self.campaign_id
        name = self.name
        campaign_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.campaign_type, Unset):
            campaign_type = self.campaign_type.to_dict()

        campaign_display_name = self.campaign_display_name
        status = self.status
        contents = self.contents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if name is not UNSET:
            field_dict["name"] = name
        if campaign_type is not UNSET:
            field_dict["campaignType"] = campaign_type
        if campaign_display_name is not UNSET:
            field_dict["campaignDisplayName"] = campaign_display_name
        if status is not UNSET:
            field_dict["status"] = status
        if contents is not UNSET:
            field_dict["contents"] = contents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        campaign_id = d.pop("campaignId", UNSET)

        name = d.pop("name", UNSET)

        _campaign_type = d.pop("campaignType", UNSET)
        campaign_type: Union[Unset, GetCampaignsResponse200ItemsItemCampaignType]
        if isinstance(_campaign_type, Unset):
            campaign_type = UNSET
        else:
            campaign_type = GetCampaignsResponse200ItemsItemCampaignType.from_dict(_campaign_type)

        campaign_display_name = d.pop("campaignDisplayName", UNSET)

        status = d.pop("status", UNSET)

        contents = d.pop("contents", UNSET)

        get_campaigns_response_200_items_item = cls(
            campaign_id=campaign_id,
            name=name,
            campaign_type=campaign_type,
            campaign_display_name=campaign_display_name,
            status=status,
            contents=contents,
        )

        get_campaigns_response_200_items_item.additional_properties = d
        return get_campaigns_response_200_items_item

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
