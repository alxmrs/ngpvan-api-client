from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_campaign_by_id_response_200_contents_item_content_type import (
    GetCampaignByIdResponse200ContentsItemContentType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCampaignByIdResponse200ContentsItem")


@attr.s(auto_attribs=True)
class GetCampaignByIdResponse200ContentsItem:
    """
    Attributes:
        content_id (Union[Unset, int]):  Example: 5328.
        content_type (Union[Unset, GetCampaignByIdResponse200ContentsItemContentType]):
        name (Union[Unset, str]):  Example: Pro Minimum Wage.
        short_name (Union[Unset, str]):  Example: Pro Wage.
        display_name (Union[Unset, str]):  Example: Literature: Pro Minimum Wage.
        description (Union[Unset, str]):  Example: This is a lit piece encouraging minimum wage increases.
        disposition (Union[Unset, str]):  Example: Positive.
    """

    content_id: Union[Unset, int] = 0
    content_type: Union[Unset, GetCampaignByIdResponse200ContentsItemContentType] = UNSET
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    disposition: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_id = self.content_id
        content_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.to_dict()

        name = self.name
        short_name = self.short_name
        display_name = self.display_name
        description = self.description
        disposition = self.disposition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_id is not UNSET:
            field_dict["contentId"] = content_id
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if disposition is not UNSET:
            field_dict["disposition"] = disposition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_id = d.pop("contentId", UNSET)

        _content_type = d.pop("contentType", UNSET)
        content_type: Union[Unset, GetCampaignByIdResponse200ContentsItemContentType]
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = GetCampaignByIdResponse200ContentsItemContentType.from_dict(_content_type)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        disposition = d.pop("disposition", UNSET)

        get_campaign_by_id_response_200_contents_item = cls(
            content_id=content_id,
            content_type=content_type,
            name=name,
            short_name=short_name,
            display_name=display_name,
            description=description,
            disposition=disposition,
        )

        get_campaign_by_id_response_200_contents_item.additional_properties = d
        return get_campaign_by_id_response_200_contents_item

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
