from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Stories1Response201StoryStatus")


@attr.s(auto_attribs=True)
class Stories1Response201StoryStatus:
    """
    Attributes:
        story_status_id (Union[Unset, int]):  Example: 1.
    """

    story_status_id: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        story_status_id = self.story_status_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if story_status_id is not UNSET:
            field_dict["storyStatusId"] = story_status_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        story_status_id = d.pop("storyStatusId", UNSET)

        stories_1_response_201_story_status = cls(
            story_status_id=story_status_id,
        )

        stories_1_response_201_story_status.additional_properties = d
        return stories_1_response_201_story_status

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