from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidnotesnoteidJsonBodyCategory")


@attr.s(auto_attribs=True)
class PeoplevanidnotesnoteidJsonBodyCategory:
    """Optional; if specified, must be an object whose `noteCategoryId` corresponds to a Note Category which may be applied
    to People, and which is available at `GET /notes/categories`,

        Attributes:
            note_category_id (Union[Unset, int]): Unique identifier for a Note Category in this context Default: 99.
    """

    note_category_id: Union[Unset, int] = 99
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note_category_id = self.note_category_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note_category_id is not UNSET:
            field_dict["noteCategoryId"] = note_category_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        note_category_id = d.pop("noteCategoryId", UNSET)

        peoplevanidnotesnoteid_json_body_category = cls(
            note_category_id=note_category_id,
        )

        peoplevanidnotesnoteid_json_body_category.additional_properties = d
        return peoplevanidnotesnoteid_json_body_category

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
