from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidrelationshipsJsonBody")


@attr.s(auto_attribs=True)
class PeoplevanidrelationshipsJsonBody:
    """
    Attributes:
        relationship_id (Union[Unset, str]): Required; Unique identifier for an existing
            [Relationship](ref:relationships). Default: '19'.
        van_id (Union[Unset, str]): Required; Unique identifier of the Person who is related to the Person from the URL
            route. Default: '7890123'.
    """

    relationship_id: Union[Unset, str] = "19"
    van_id: Union[Unset, str] = "7890123"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relationship_id = self.relationship_id
        van_id = self.van_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relationship_id is not UNSET:
            field_dict["relationshipId"] = relationship_id
        if van_id is not UNSET:
            field_dict["vanId"] = van_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        relationship_id = d.pop("relationshipId", UNSET)

        van_id = d.pop("vanId", UNSET)

        peoplevanidrelationships_json_body = cls(
            relationship_id=relationship_id,
            van_id=van_id,
        )

        peoplevanidrelationships_json_body.additional_properties = d
        return peoplevanidrelationships_json_body

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
