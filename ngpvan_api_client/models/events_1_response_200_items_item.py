from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.events_1_response_200_items_item_event_type import Events1Response200ItemsItemEventType
from ..models.events_1_response_200_items_item_shifts_item import Events1Response200ItemsItemShiftsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Events1Response200ItemsItem")


@attr.s(auto_attribs=True)
class Events1Response200ItemsItem:
    """
    Attributes:
        event_id (Union[Unset, int]):  Example: 1370.
        name (Union[Unset, str]):  Example: Neighbors Calling Neighbors.
        short_name (Union[Unset, str]):  Example: NeighborCall.
        description (Union[Unset, str]):  Example: Come help get the word out about our great campaign..
        start_date (Union[Unset, str]):  Example: 2015-06-01T15:00:00-04:00.
        end_date (Union[Unset, str]):  Example: 2015-06-01T20:00:00-04:00.
        event_type (Union[Unset, Events1Response200ItemsItemEventType]):
        is_only_editable_by_creating_user (Union[Unset, bool]):  Default: True.
        is_publicly_viewable (Union[Unset, Any]):
        locations (Union[Unset, Any]):
        codes (Union[Unset, Any]):
        notes (Union[Unset, Any]):
        shifts (Union[Unset, List[Events1Response200ItemsItemShiftsItem]]):
        roles (Union[Unset, Any]):
        district_field_value (Union[Unset, str]):  Example: 003.
        voter_registration_batches (Union[Unset, Any]):
        created_date (Union[Unset, str]):  Example: 2015-04-05T13:18:00Z.
    """

    event_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    event_type: Union[Unset, Events1Response200ItemsItemEventType] = UNSET
    is_only_editable_by_creating_user: Union[Unset, bool] = True
    is_publicly_viewable: Union[Unset, Any] = UNSET
    locations: Union[Unset, Any] = UNSET
    codes: Union[Unset, Any] = UNSET
    notes: Union[Unset, Any] = UNSET
    shifts: Union[Unset, List[Events1Response200ItemsItemShiftsItem]] = UNSET
    roles: Union[Unset, Any] = UNSET
    district_field_value: Union[Unset, str] = UNSET
    voter_registration_batches: Union[Unset, Any] = UNSET
    created_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_id = self.event_id
        name = self.name
        short_name = self.short_name
        description = self.description
        start_date = self.start_date
        end_date = self.end_date
        event_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.to_dict()

        is_only_editable_by_creating_user = self.is_only_editable_by_creating_user
        is_publicly_viewable = self.is_publicly_viewable
        locations = self.locations
        codes = self.codes
        notes = self.notes
        shifts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shifts, Unset):
            shifts = []
            for shifts_item_data in self.shifts:
                shifts_item = shifts_item_data.to_dict()

                shifts.append(shifts_item)

        roles = self.roles
        district_field_value = self.district_field_value
        voter_registration_batches = self.voter_registration_batches
        created_date = self.created_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if is_only_editable_by_creating_user is not UNSET:
            field_dict["isOnlyEditableByCreatingUser"] = is_only_editable_by_creating_user
        if is_publicly_viewable is not UNSET:
            field_dict["isPubliclyViewable"] = is_publicly_viewable
        if locations is not UNSET:
            field_dict["locations"] = locations
        if codes is not UNSET:
            field_dict["codes"] = codes
        if notes is not UNSET:
            field_dict["notes"] = notes
        if shifts is not UNSET:
            field_dict["shifts"] = shifts
        if roles is not UNSET:
            field_dict["roles"] = roles
        if district_field_value is not UNSET:
            field_dict["districtFieldValue"] = district_field_value
        if voter_registration_batches is not UNSET:
            field_dict["voterRegistrationBatches"] = voter_registration_batches
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_id = d.pop("eventId", UNSET)

        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        description = d.pop("description", UNSET)

        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, Events1Response200ItemsItemEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = Events1Response200ItemsItemEventType.from_dict(_event_type)

        is_only_editable_by_creating_user = d.pop("isOnlyEditableByCreatingUser", UNSET)

        is_publicly_viewable = d.pop("isPubliclyViewable", UNSET)

        locations = d.pop("locations", UNSET)

        codes = d.pop("codes", UNSET)

        notes = d.pop("notes", UNSET)

        shifts = []
        _shifts = d.pop("shifts", UNSET)
        for shifts_item_data in _shifts or []:
            shifts_item = Events1Response200ItemsItemShiftsItem.from_dict(shifts_item_data)

            shifts.append(shifts_item)

        roles = d.pop("roles", UNSET)

        district_field_value = d.pop("districtFieldValue", UNSET)

        voter_registration_batches = d.pop("voterRegistrationBatches", UNSET)

        created_date = d.pop("createdDate", UNSET)

        events_1_response_200_items_item = cls(
            event_id=event_id,
            name=name,
            short_name=short_name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            event_type=event_type,
            is_only_editable_by_creating_user=is_only_editable_by_creating_user,
            is_publicly_viewable=is_publicly_viewable,
            locations=locations,
            codes=codes,
            notes=notes,
            shifts=shifts,
            roles=roles,
            district_field_value=district_field_value,
            voter_registration_batches=voter_registration_batches,
            created_date=created_date,
        )

        events_1_response_200_items_item.additional_properties = d
        return events_1_response_200_items_item

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
