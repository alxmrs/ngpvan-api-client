from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoresscoreidOKRangeScore")


@attr.s(auto_attribs=True)
class ScoresscoreidOKRangeScore:
    """
    Attributes:
        score_id (Union[Unset, int]):  Example: 123.
        name (Union[Unset, str]):  Example: Haberdashery score.
        short_name (Union[Unset, str]):  Example: HATS.
        description (Union[Unset, str]):  Example: Estimation of how many hats an individual owns.
        score_type (Union[Unset, str]):  Example: Range.
        min_value (Union[Unset, int]):  Example: 1.
        max_value (Union[Unset, int]):  Example: 10.
    """

    score_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    score_type: Union[Unset, str] = UNSET
    min_value: Union[Unset, int] = 0
    max_value: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        score_id = self.score_id
        name = self.name
        short_name = self.short_name
        description = self.description
        score_type = self.score_type
        min_value = self.min_value
        max_value = self.max_value

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
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        score_id = d.pop("scoreId", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        description = d.pop("description", UNSET)

        score_type = d.pop("scoreType", UNSET)

        min_value = d.pop("minValue", UNSET)

        max_value = d.pop("maxValue", UNSET)

        scoresscoreid_ok_range_score = cls(
            score_id=score_id,
            name=name,
            short_name=short_name,
            description=description,
            score_type=score_type,
            min_value=min_value,
            max_value=max_value,
        )

        scoresscoreid_ok_range_score.additional_properties = d
        return scoresscoreid_ok_range_score

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
