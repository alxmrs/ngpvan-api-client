from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplevanidnotesnoteid_json_body_category import PeoplevanidnotesnoteidJsonBodyCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidnotesnoteidJsonBody")


@attr.s(auto_attribs=True)
class PeoplevanidnotesnoteidJsonBody:
    """
    Attributes:
        text (Union[Unset, str]): Required; the content of the description of the Person. Default: 'Great chat! This
            person will be able to volunteer next year.'.
        is_view_restricted (Union[Unset, bool]): Required; set to `true` if the note should be restricted only to
            certain users within the current context; set to `false` if the note may be viewed by any user in the current
            context.
        category (Union[Unset, PeoplevanidnotesnoteidJsonBodyCategory]): Optional; if specified, must be an object whose
            `noteCategoryId` corresponds to a Note Category which may be applied to People, and which is available at `GET
            /notes/categories`,
    """

    text: Union[Unset, str] = "Great chat! This person will be able to volunteer next year."
    is_view_restricted: Union[Unset, bool] = False
    category: Union[Unset, PeoplevanidnotesnoteidJsonBodyCategory] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        is_view_restricted = self.is_view_restricted
        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if is_view_restricted is not UNSET:
            field_dict["isViewRestricted"] = is_view_restricted
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        is_view_restricted = d.pop("isViewRestricted", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, PeoplevanidnotesnoteidJsonBodyCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PeoplevanidnotesnoteidJsonBodyCategory.from_dict(_category)

        peoplevanidnotesnoteid_json_body = cls(
            text=text,
            is_view_restricted=is_view_restricted,
            category=category,
        )

        peoplevanidnotesnoteid_json_body.additional_properties = d
        return peoplevanidnotesnoteid_json_body

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
