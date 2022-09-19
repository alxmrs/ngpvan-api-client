from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Events2Response201VoterRegistrationBatchesItem")


@attr.s(auto_attribs=True)
class Events2Response201VoterRegistrationBatchesItem:
    """
    Attributes:
        voter_registration_batch_id (Union[Unset, int]):  Example: 999.
    """

    voter_registration_batch_id: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        voter_registration_batch_id = self.voter_registration_batch_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voter_registration_batch_id is not UNSET:
            field_dict["voterRegistrationBatchId"] = voter_registration_batch_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        voter_registration_batch_id = d.pop("voterRegistrationBatchId", UNSET)

        events_2_response_201_voter_registration_batches_item = cls(
            voter_registration_batch_id=voter_registration_batch_id,
        )

        events_2_response_201_voter_registration_batches_item.additional_properties = d
        return events_2_response_201_voter_registration_batches_item

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
