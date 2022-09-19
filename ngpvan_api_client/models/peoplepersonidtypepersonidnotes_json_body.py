from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplepersonidtypepersonidnotes_json_body_category import PeoplepersonidtypepersonidnotesJsonBodyCategory
from ..models.peoplepersonidtypepersonidnotes_json_body_contact_history import (
    PeoplepersonidtypepersonidnotesJsonBodyContactHistory,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplepersonidtypepersonidnotesJsonBody")


@attr.s(auto_attribs=True)
class PeoplepersonidtypepersonidnotesJsonBody:
    """
    Attributes:
        text (Union[Unset, str]): Required; the content of the description of the Person. Default: 'Great chat! This
            person will be able to volunteer next year.'.
        is_view_restricted (Union[Unset, str]): Required; set to `true` if the note should be restricted only to certain
            users within the current context; set to `false` if the note may be viewed by any user in the current context.
            Default: 'false'.
        category (Union[Unset, PeoplepersonidtypepersonidnotesJsonBodyCategory]): Optional; if specified, must be an
            object whose `noteCategoryId` corresponds to a Note Category which may be applied to People, and which is
            available at `GET /notes/categories`,
        contact_history (Union[Unset, PeoplepersonidtypepersonidnotesJsonBodyContactHistory]):
    """

    text: Union[Unset, str] = "Great chat! This person will be able to volunteer next year."
    is_view_restricted: Union[Unset, str] = "false"
    category: Union[Unset, PeoplepersonidtypepersonidnotesJsonBodyCategory] = UNSET
    contact_history: Union[Unset, PeoplepersonidtypepersonidnotesJsonBodyContactHistory] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        is_view_restricted = self.is_view_restricted
        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        contact_history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact_history, Unset):
            contact_history = self.contact_history.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if is_view_restricted is not UNSET:
            field_dict["isViewRestricted"] = is_view_restricted
        if category is not UNSET:
            field_dict["category"] = category
        if contact_history is not UNSET:
            field_dict["contactHistory"] = contact_history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text", UNSET)

        is_view_restricted = d.pop("isViewRestricted", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, PeoplepersonidtypepersonidnotesJsonBodyCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PeoplepersonidtypepersonidnotesJsonBodyCategory.from_dict(_category)

        _contact_history = d.pop("contactHistory", UNSET)
        contact_history: Union[Unset, PeoplepersonidtypepersonidnotesJsonBodyContactHistory]
        if isinstance(_contact_history, Unset):
            contact_history = UNSET
        else:
            contact_history = PeoplepersonidtypepersonidnotesJsonBodyContactHistory.from_dict(_contact_history)

        peoplepersonidtypepersonidnotes_json_body = cls(
            text=text,
            is_view_restricted=is_view_restricted,
            category=category,
            contact_history=contact_history,
        )

        peoplepersonidtypepersonidnotes_json_body.additional_properties = d
        return peoplepersonidtypepersonidnotes_json_body

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
