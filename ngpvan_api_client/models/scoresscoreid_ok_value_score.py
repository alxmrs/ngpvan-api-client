from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.scoresscoreid_ok_value_score_values_item import ScoresscoreidOKValueScoreValuesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoresscoreidOKValueScore")


@attr.s(auto_attribs=True)
class ScoresscoreidOKValueScore:
    """
    Attributes:
        score_id (Union[Unset, int]):  Example: 782.
        name (Union[Unset, str]):  Example: Estimated Hat Enthusiasm.
        short_name (Union[Unset, str]):  Example: ENTH.
        description (Union[Unset, str]):  Example: Estimated enthusiasm level.
        score_type (Union[Unset, str]):  Example: Value.
        values (Union[Unset, List[ScoresscoreidOKValueScoreValuesItem]]):
    """

    score_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    score_type: Union[Unset, str] = UNSET
    values: Union[Unset, List[ScoresscoreidOKValueScoreValuesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        score_id = self.score_id
        name = self.name
        short_name = self.short_name
        description = self.description
        score_type = self.score_type
        values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()

                values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score_id is not UNSET:
            field_dict["scoreId"] = score_id
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if description is not UNSET:
            field_dict["description"] = description
        if score_type is not UNSET:
            field_dict["scoreType"] = score_type
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        score_id = d.pop("scoreId", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        description = d.pop("description", UNSET)

        score_type = d.pop("scoreType", UNSET)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = ScoresscoreidOKValueScoreValuesItem.from_dict(values_item_data)

            values.append(values_item)

        scoresscoreid_ok_value_score = cls(
            score_id=score_id,
            name=name,
            short_name=short_name,
            description=description,
            score_type=score_type,
            values=values,
        )

        scoresscoreid_ok_value_score.additional_properties = d
        return scoresscoreid_ok_value_score

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
