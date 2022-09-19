import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangedentityexportjobsJsonBody")


@attr.s(auto_attribs=True)
class ChangedentityexportjobsJsonBody:
    """
    Attributes:
        date_changed_from (Union[Unset, datetime.date]): **Required**; timestamp in the format `YYYY-MM-DDThh:mm:ss.00Z`
            or `YYYY-MM-DDThh:mm:ss.00 -hh:mm`. Must be in the last 90 days. Default:
            isoparse('2021-01-01T01:02:03+04:00').date().
        date_changed_to (Union[Unset, datetime.date]): **Optional**; timestamp in the format `YYYY-MM-DDThh:mm:ss.00Z`
            or `YYYY-MM-DDThh:mm:ss.00 -hh:mm`. If provided, must be a date that is more recent than dateChangedFrom, and
            must be no later than the present. If not provided, will be set automatically to the time at which the API
            request is made. Default: isoparse('2021-02-14T01:09:03+04:00').date().
        resource_type (Union[Unset, str]): **Required**; available resource type specified at the
            [/resources](ref:changed-entities#changedentityexportjobsresources) endpoint Default: 'Contacts'.
        requested_ids (Union[Unset, List[int]]): IDs to be included in the exported set if available. Overrides the time
            window specified as well as the `includeInactive` property.
        requested_fields (Union[Unset, List[str]]): Names of non-core fields to be included in the export
        requested_custom_field_ids (Union[Unset, List[int]]): IDs of custom fields to be included in the export
        file_size_kb_limit (Union[Unset, int]): The maximum size in Kb (between 1000 and 100000) of any exported `.csv`
            file; defaults to 40000 Default: 40000.
        include_inactive (Union[Unset, bool]): If set to `true`, includes inactive records such as archived activist
            codes or deleted contacts. Defaults to `false`.
    """

    date_changed_from: Union[Unset, datetime.date] = isoparse("2021-01-01T01:02:03+04:00").date()
    date_changed_to: Union[Unset, datetime.date] = isoparse("2021-02-14T01:09:03+04:00").date()
    resource_type: Union[Unset, str] = "Contacts"
    requested_ids: Union[Unset, List[int]] = UNSET
    requested_fields: Union[Unset, List[str]] = UNSET
    requested_custom_field_ids: Union[Unset, List[int]] = UNSET
    file_size_kb_limit: Union[Unset, int] = 40000
    include_inactive: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_changed_from: Union[Unset, str] = UNSET
        if not isinstance(self.date_changed_from, Unset):
            date_changed_from = self.date_changed_from.isoformat()

        date_changed_to: Union[Unset, str] = UNSET
        if not isinstance(self.date_changed_to, Unset):
            date_changed_to = self.date_changed_to.isoformat()

        resource_type = self.resource_type
        requested_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.requested_ids, Unset):
            requested_ids = self.requested_ids

        requested_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.requested_fields, Unset):
            requested_fields = self.requested_fields

        requested_custom_field_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.requested_custom_field_ids, Unset):
            requested_custom_field_ids = self.requested_custom_field_ids

        file_size_kb_limit = self.file_size_kb_limit
        include_inactive = self.include_inactive

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_changed_from is not UNSET:
            field_dict["dateChangedFrom"] = date_changed_from
        if date_changed_to is not UNSET:
            field_dict["dateChangedTo"] = date_changed_to
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if requested_ids is not UNSET:
            field_dict["requestedIds"] = requested_ids
        if requested_fields is not UNSET:
            field_dict["requestedFields"] = requested_fields
        if requested_custom_field_ids is not UNSET:
            field_dict["requestedCustomFieldIds"] = requested_custom_field_ids
        if file_size_kb_limit is not UNSET:
            field_dict["fileSizeKbLimit"] = file_size_kb_limit
        if include_inactive is not UNSET:
            field_dict["includeInactive"] = include_inactive

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date_changed_from = d.pop("dateChangedFrom", UNSET)
        date_changed_from: Union[Unset, datetime.date]
        if isinstance(_date_changed_from, Unset):
            date_changed_from = UNSET
        else:
            date_changed_from = isoparse(_date_changed_from).date()

        _date_changed_to = d.pop("dateChangedTo", UNSET)
        date_changed_to: Union[Unset, datetime.date]
        if isinstance(_date_changed_to, Unset):
            date_changed_to = UNSET
        else:
            date_changed_to = isoparse(_date_changed_to).date()

        resource_type = d.pop("resourceType", UNSET)

        requested_ids = cast(List[int], d.pop("requestedIds", UNSET))

        requested_fields = cast(List[str], d.pop("requestedFields", UNSET))

        requested_custom_field_ids = cast(List[int], d.pop("requestedCustomFieldIds", UNSET))

        file_size_kb_limit = d.pop("fileSizeKbLimit", UNSET)

        include_inactive = d.pop("includeInactive", UNSET)

        changedentityexportjobs_json_body = cls(
            date_changed_from=date_changed_from,
            date_changed_to=date_changed_to,
            resource_type=resource_type,
            requested_ids=requested_ids,
            requested_fields=requested_fields,
            requested_custom_field_ids=requested_custom_field_ids,
            file_size_kb_limit=file_size_kb_limit,
            include_inactive=include_inactive,
        )

        changedentityexportjobs_json_body.additional_properties = d
        return changedentityexportjobs_json_body

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
