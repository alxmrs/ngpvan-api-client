from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoresscoreidOKValueScoreValuesItem")


@attr.s(auto_attribs=True)
class ScoresscoreidOKValueScoreValuesItem:
    """
    Attributes:
        score_value_id (Union[Unset, int]):  Example: 12.
        name (Union[Unset, str]):  Example: Low.
        short_name (Union[Unset, str]):  Example: low.
        sort_order (Union[Unset, int]):  Example: 1.
    """

    score_value_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        score_value_id = self.score_value_id
        name = self.name
        short_name = self.short_name
        sort_order = self.sort_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score_value_id is not UNSET:
            field_dict["scoreValueId"] = score_value_id
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        score_value_id = d.pop("scoreValueId", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        scoresscoreid_ok_value_score_values_item = cls(
            score_value_id=score_value_id,
            name=name,
            short_name=short_name,
            sort_order=sort_order,
        )

        scoresscoreid_ok_value_score_values_item.additional_properties = d
        return scoresscoreid_ok_value_score_values_item

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
