from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SavedlistssavedlistidResponse200")


@attr.s(auto_attribs=True)
class SavedlistssavedlistidResponse200:
    """
    Attributes:
        saved_list_id (Union[Unset, int]):  Example: 123.
        name (Union[Unset, str]):  Example: GOTV list.
        description (Union[Unset, str]):  Example: People we want to talk to for GOTV.
        list_count (Union[Unset, int]):  Example: 2000.
        door_count (Union[Unset, int]):  Example: 987.
    """

    saved_list_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    list_count: Union[Unset, int] = 0
    door_count: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        saved_list_id = self.saved_list_id
        name = self.name
        description = self.description
        list_count = self.list_count
        door_count = self.door_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if saved_list_id is not UNSET:
            field_dict["savedListId"] = saved_list_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if list_count is not UNSET:
            field_dict["listCount"] = list_count
        if door_count is not UNSET:
            field_dict["doorCount"] = door_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        saved_list_id = d.pop("savedListId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        list_count = d.pop("listCount", UNSET)

        door_count = d.pop("doorCount", UNSET)

        savedlistssavedlistid_response_200 = cls(
            saved_list_id=saved_list_id,
            name=name,
            description=description,
            list_count=list_count,
            door_count=door_count,
        )

        savedlistssavedlistid_response_200.additional_properties = d
        return savedlistssavedlistid_response_200

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
