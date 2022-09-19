from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCampaignByIdResponse200CampaignType")


@attr.s(auto_attribs=True)
class GetCampaignByIdResponse200CampaignType:
    """
    Attributes:
        campaign_type_id (Union[Unset, int]):  Example: 1312.
        name (Union[Unset, str]):  Example: Advocacy.
    """

    campaign_type_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        campaign_type_id = self.campaign_type_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaign_type_id is not UNSET:
            field_dict["campaignTypeId"] = campaign_type_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        campaign_type_id = d.pop("campaignTypeId", UNSET)

        name = d.pop("name", UNSET)

        get_campaign_by_id_response_200_campaign_type = cls(
            campaign_type_id=campaign_type_id,
            name=name,
        )

        get_campaign_by_id_response_200_campaign_type.additional_properties = d
        return get_campaign_by_id_response_200_campaign_type

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
