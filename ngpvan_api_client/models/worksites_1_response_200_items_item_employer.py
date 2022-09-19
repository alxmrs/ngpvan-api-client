from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Worksites1Response200ItemsItemEmployer")


@attr.s(auto_attribs=True)
class Worksites1Response200ItemsItemEmployer:
    """
    Attributes:
        employer_id (Union[Unset, int]):  Example: 99.
        name (Union[Unset, str]):  Example: Malden Public Schools.
    """

    employer_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        employer_id = self.employer_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employer_id is not UNSET:
            field_dict["employerId"] = employer_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        employer_id = d.pop("employerId", UNSET)

        name = d.pop("name", UNSET)

        worksites_1_response_200_items_item_employer = cls(
            employer_id=employer_id,
            name=name,
        )

        worksites_1_response_200_items_item_employer.additional_properties = d
        return worksites_1_response_200_items_item_employer

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
