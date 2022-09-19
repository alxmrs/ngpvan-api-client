from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BallotrejectionreasonsballotrejectionreasonidResponse200")


@attr.s(auto_attribs=True)
class BallotrejectionreasonsballotrejectionreasonidResponse200:
    """
    Attributes:
        ballot_rejection_reason_id (Union[Unset, int]):  Example: 1.
        name (Union[Unset, str]):  Example: Rejected.
    """

    ballot_rejection_reason_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ballot_rejection_reason_id = self.ballot_rejection_reason_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ballot_rejection_reason_id is not UNSET:
            field_dict["ballotRejectionReasonId"] = ballot_rejection_reason_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ballot_rejection_reason_id = d.pop("ballotRejectionReasonId", UNSET)

        name = d.pop("name", UNSET)

        ballotrejectionreasonsballotrejectionreasonid_response_200 = cls(
            ballot_rejection_reason_id=ballot_rejection_reason_id,
            name=name,
        )

        ballotrejectionreasonsballotrejectionreasonid_response_200.additional_properties = d
        return ballotrejectionreasonsballotrejectionreasonid_response_200

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
