from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BallotreturnstatusesballotreturnstatusidResponse200")


@attr.s(auto_attribs=True)
class BallotreturnstatusesballotreturnstatusidResponse200:
    """
    Attributes:
        ballot_return_status_id (Union[Unset, int]):  Example: 14.
        name (Union[Unset, str]):  Example: Not Voted.
    """

    ballot_return_status_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ballot_return_status_id = self.ballot_return_status_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ballot_return_status_id is not UNSET:
            field_dict["ballotReturnStatusId"] = ballot_return_status_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ballot_return_status_id = d.pop("ballotReturnStatusId", UNSET)

        name = d.pop("name", UNSET)

        ballotreturnstatusesballotreturnstatusid_response_200 = cls(
            ballot_return_status_id=ballot_return_status_id,
            name=name,
        )

        ballotreturnstatusesballotreturnstatusid_response_200.additional_properties = d
        return ballotreturnstatusesballotreturnstatusid_response_200

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
