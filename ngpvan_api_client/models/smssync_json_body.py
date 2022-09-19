import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmssyncJsonBody")


@attr.s(auto_attribs=True)
class SmssyncJsonBody:
    """
    Attributes:
        sync_period_start (Union[Unset, datetime.date]): The date and time to begin including changes. In most
            scenarios, this will be the time of your last sync. Default:
            isoparse('2016-05-23T18:54:58.9123154-04:00').date().
        sync_period_end (Union[Unset, datetime.date]): The date and time to end including changes. In most scenarios,
            this will be the current date and time. Default: isoparse('2016-05-24T18:54:58.9123154-04:00').date().
    """

    sync_period_start: Union[Unset, datetime.date] = isoparse("2016-05-23T18:54:58.9123154-04:00").date()
    sync_period_end: Union[Unset, datetime.date] = isoparse("2016-05-24T18:54:58.9123154-04:00").date()
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sync_period_start: Union[Unset, str] = UNSET
        if not isinstance(self.sync_period_start, Unset):
            sync_period_start = self.sync_period_start.isoformat()

        sync_period_end: Union[Unset, str] = UNSET
        if not isinstance(self.sync_period_end, Unset):
            sync_period_end = self.sync_period_end.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sync_period_start is not UNSET:
            field_dict["syncPeriodStart"] = sync_period_start
        if sync_period_end is not UNSET:
            field_dict["syncPeriodEnd"] = sync_period_end

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sync_period_start = d.pop("syncPeriodStart", UNSET)
        sync_period_start: Union[Unset, datetime.date]
        if isinstance(_sync_period_start, Unset):
            sync_period_start = UNSET
        else:
            sync_period_start = isoparse(_sync_period_start).date()

        _sync_period_end = d.pop("syncPeriodEnd", UNSET)
        sync_period_end: Union[Unset, datetime.date]
        if isinstance(_sync_period_end, Unset):
            sync_period_end = UNSET
        else:
            sync_period_end = isoparse(_sync_period_end).date()

        smssync_json_body = cls(
            sync_period_start=sync_period_start,
            sync_period_end=sync_period_end,
        )

        smssync_json_body.additional_properties = d
        return smssync_json_body

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
