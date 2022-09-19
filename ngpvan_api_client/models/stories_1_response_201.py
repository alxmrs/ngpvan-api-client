from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.stories_1_response_201_story_status import Stories1Response201StoryStatus
from ..models.stories_1_response_201_tags_item import Stories1Response201TagsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Stories1Response201")


@attr.s(auto_attribs=True)
class Stories1Response201:
    """
    Attributes:
        story_id (Union[Unset, int]):  Example: 124.
        title (Union[Unset, str]):  Example: A Tale of Two Cities.
        story_text (Union[Unset, str]):  Example: It was the best of times, it was the worst of times ....
        story_status (Union[Unset, Stories1Response201StoryStatus]):
        van_id (Union[Unset, int]):  Example: 1000000000.
        tags (Union[Unset, List[Stories1Response201TagsItem]]):
        campaign_id (Union[Unset, int]):  Example: 123456.
    """

    story_id: Union[Unset, int] = 0
    title: Union[Unset, str] = UNSET
    story_text: Union[Unset, str] = UNSET
    story_status: Union[Unset, Stories1Response201StoryStatus] = UNSET
    van_id: Union[Unset, int] = 0
    tags: Union[Unset, List[Stories1Response201TagsItem]] = UNSET
    campaign_id: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        story_id = self.story_id
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
        if story_id is not UNSET:
            field_dict["storyId"] = story_id
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
        story_id = d.pop("storyId", UNSET)

        title = d.pop("title", UNSET)

        story_text = d.pop("storyText", UNSET)

        _story_status = d.pop("storyStatus", UNSET)
        story_status: Union[Unset, Stories1Response201StoryStatus]
        if isinstance(_story_status, Unset):
            story_status = UNSET
        else:
            story_status = Stories1Response201StoryStatus.from_dict(_story_status)

        van_id = d.pop("vanId", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = Stories1Response201TagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        campaign_id = d.pop("campaignId", UNSET)

        stories_1_response_201 = cls(
            story_id=story_id,
            title=title,
            story_text=story_text,
            story_status=story_status,
            van_id=van_id,
            tags=tags,
            campaign_id=campaign_id,
        )

        stories_1_response_201.additional_properties = d
        return stories_1_response_201

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
