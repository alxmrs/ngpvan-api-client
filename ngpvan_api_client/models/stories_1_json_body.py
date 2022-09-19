from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.stories_1_json_body_story_status import Stories1JsonBodyStoryStatus
from ..models.stories_1_json_body_tags_item import Stories1JsonBodyTagsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Stories1JsonBody")


@attr.s(auto_attribs=True)
class Stories1JsonBody:
    """
    Attributes:
        title (Union[Unset, str]):  Default: 'A Tale of Two Cities'.
        story_text (Union[Unset, str]):  Default: 'It was the best of times, it was the worst of times ...'.
        story_status (Union[Unset, Stories1JsonBodyStoryStatus]):
        van_id (Union[Unset, str]):  Default: '1000000000'.
        tags (Union[Unset, List[Stories1JsonBodyTagsItem]]):
        campaign_id (Union[Unset, int]):  Default: 123456.
    """

    title: Union[Unset, str] = "A Tale of Two Cities"
    story_text: Union[Unset, str] = "It was the best of times, it was the worst of times ..."
    story_status: Union[Unset, Stories1JsonBodyStoryStatus] = UNSET
    van_id: Union[Unset, str] = "1000000000"
    tags: Union[Unset, List[Stories1JsonBodyTagsItem]] = UNSET
    campaign_id: Union[Unset, int] = 123456
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        story_text = self.story_text
        story_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.story_status, Unset):
            story_status = self.story_status.to_dict()

        van_id = self.van_id
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        campaign_id = self.campaign_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if story_text is not UNSET:
            field_dict["storyText"] = story_text
        if story_status is not UNSET:
            field_dict["storyStatus"] = story_status
        if van_id is not UNSET:
            field_dict["vanId"] = van_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        story_text = d.pop("storyText", UNSET)

        _story_status = d.pop("storyStatus", UNSET)
        story_status: Union[Unset, Stories1JsonBodyStoryStatus]
        if isinstance(_story_status, Unset):
            story_status = UNSET
        else:
            story_status = Stories1JsonBodyStoryStatus.from_dict(_story_status)

        van_id = d.pop("vanId", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = Stories1JsonBodyTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        campaign_id = d.pop("campaignId", UNSET)

        stories_1_json_body = cls(
            title=title,
            story_text=story_text,
            story_status=story_status,
            van_id=van_id,
            tags=tags,
            campaign_id=campaign_id,
        )

        stories_1_json_body.additional_properties = d
        return stories_1_json_body

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
