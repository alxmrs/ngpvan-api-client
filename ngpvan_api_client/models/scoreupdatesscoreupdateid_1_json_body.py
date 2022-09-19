from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Scoreupdatesscoreupdateid1JsonBody")


@attr.s(auto_attribs=True)
class Scoreupdatesscoreupdateid1JsonBody:
    """
    Attributes:
        load_status (Union[Unset, str]): Required; The new status for a score update; one of: `PendingApproval` → Score
            updates in the pending state will not be applied, `Approved` → Approves the score update for application during
            off-peak hours, `Disapproved` → Explicitly indicates the score update should not be applied (e.g., because the
            load statistics indicate an issue with a source file), `Canceled` → Cancel the score update process (does not
            stop anything that is currently in process, behaves the same as Disapproved Default: 'Approved'.
    """

    load_status: Union[Unset, str] = "Approved"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        load_status = self.load_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if load_status is not UNSET:
            field_dict["loadStatus"] = load_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        load_status = d.pop("loadStatus", UNSET)

        scoreupdatesscoreupdateid_1_json_body = cls(
            load_status=load_status,
        )

        scoreupdatesscoreupdateid_1_json_body.additional_properties = d
        return scoreupdatesscoreupdateid_1_json_body

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
