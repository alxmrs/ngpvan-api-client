from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplevanidnotes_1_json_body_category import Peoplevanidnotes1JsonBodyCategory
from ..models.peoplevanidnotes_1_json_body_contact_history import Peoplevanidnotes1JsonBodyContactHistory
from ..types import UNSET, Unset

T = TypeVar("T", bound="Peoplevanidnotes1JsonBody")


@attr.s(auto_attribs=True)
class Peoplevanidnotes1JsonBody:
    """
    Attributes:
        text (Union[Unset, str]): Required; the content of the description of the Person. Default: 'Great chat! This
            person will be able to volunteer next year.'.
        is_view_restricted (Union[Unset, bool]): Required; set to `true` if the note should be restricted only to
            certain users within the current context; set to `false` if the note may be viewed by any user in the current
            context.
        category (Union[Unset, Peoplevanidnotes1JsonBodyCategory]): Optional; if specified, must be an object whose
            `noteCategoryId` corresponds to a Note Category which may be applied to People, and which is available at `GET
            /notes/categories`,
        contact_history (Union[Unset, Peoplevanidnotes1JsonBodyContactHistory]): Optional; if specified, creates a
            Contact History record with the note, and must be a valid `Contact History` object
    """

    text: Union[Unset, str] = "Great chat! This person will be able to volunteer next year."
    is_view_restricted: Union[Unset, bool] = False
    category: Union[Unset, Peoplevanidnotes1JsonBodyCategory] = UNSET
    contact_history: Union[Unset, Peoplevanidnotes1JsonBodyContactHistory] = UNSET
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
        category: Union[Unset, Peoplevanidnotes1JsonBodyCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Peoplevanidnotes1JsonBodyCategory.from_dict(_category)

        _contact_history = d.pop("contactHistory", UNSET)
        contact_history: Union[Unset, Peoplevanidnotes1JsonBodyContactHistory]
        if isinstance(_contact_history, Unset):
            contact_history = UNSET
        else:
            contact_history = Peoplevanidnotes1JsonBodyContactHistory.from_dict(_contact_history)

        peoplevanidnotes_1_json_body = cls(
            text=text,
            is_view_restricted=is_view_restricted,
            category=category,
            contact_history=contact_history,
        )

        peoplevanidnotes_1_json_body.additional_properties = d
        return peoplevanidnotes_1_json_body

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
