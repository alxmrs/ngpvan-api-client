from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BallottypesballottypeidResponse200")


@attr.s(auto_attribs=True)
class BallottypesballottypeidResponse200:
    """
    Attributes:
        ballot_type_id (Union[Unset, int]):  Example: 7.
        name (Union[Unset, str]):  Example: Overseas.
    """

    ballot_type_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ballot_type_id = self.ballot_type_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ballot_type_id is not UNSET:
            field_dict["ballotTypeId"] = ballot_type_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ballot_type_id = d.pop("ballotTypeId", UNSET)

        name = d.pop("name", UNSET)

        ballottypesballottypeid_response_200 = cls(
            ballot_type_id=ballot_type_id,
            name=name,
        )

        ballottypesballottypeid_response_200.additional_properties = d
        return ballottypesballottypeid_response_200

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
