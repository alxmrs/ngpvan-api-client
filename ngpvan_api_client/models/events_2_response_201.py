from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.events_2_response_201_codes_item import Events2Response201CodesItem
from ..models.events_2_response_201_event_type import Events2Response201EventType
from ..models.events_2_response_201_locations_item import Events2Response201LocationsItem
from ..models.events_2_response_201_notes_item import Events2Response201NotesItem
from ..models.events_2_response_201_roles_item import Events2Response201RolesItem
from ..models.events_2_response_201_shifts_item import Events2Response201ShiftsItem
from ..models.events_2_response_201_voter_registration_batches_item import (
    Events2Response201VoterRegistrationBatchesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="Events2Response201")


@attr.s(auto_attribs=True)
class Events2Response201:
    """
    Attributes:
        name (Union[Unset, str]):  Example: Neighbors Calling Neighbors.
        short_name (Union[Unset, str]):  Example: NeighborCall.
        description (Union[Unset, str]):  Example: Come help get the word out about our great campaign..
        start_date (Union[Unset, str]):  Example: 2015-06-02T15:00:00-04:00.
        end_date (Union[Unset, str]):  Example: 2015-06-02T20:00:00-04:00.
        event_type (Union[Unset, Events2Response201EventType]):
        is_only_editable_by_creating_user (Union[Unset, bool]):  Default: True.
        locations (Union[Unset, List[Events2Response201LocationsItem]]):
        codes (Union[Unset, List[Events2Response201CodesItem]]):
        notes (Union[Unset, List[Events2Response201NotesItem]]):
        shifts (Union[Unset, List[Events2Response201ShiftsItem]]):
        roles (Union[Unset, List[Events2Response201RolesItem]]):
        voter_registration_batches (Union[Unset, List[Events2Response201VoterRegistrationBatchesItem]]):
        district_field_value (Union[Unset, str]):  Example: 003.
    """

    name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    event_type: Union[Unset, Events2Response201EventType] = UNSET
    is_only_editable_by_creating_user: Union[Unset, bool] = True
    locations: Union[Unset, List[Events2Response201LocationsItem]] = UNSET
    codes: Union[Unset, List[Events2Response201CodesItem]] = UNSET
    notes: Union[Unset, List[Events2Response201NotesItem]] = UNSET
    shifts: Union[Unset, List[Events2Response201ShiftsItem]] = UNSET
    roles: Union[Unset, List[Events2Response201RolesItem]] = UNSET
    voter_registration_batches: Union[Unset, List[Events2Response201VoterRegistrationBatchesItem]] = UNSET
    district_field_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        short_name = self.short_name
        description = self.description
        start_date = self.start_date
        end_date = self.end_date
        event_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.to_dict()

        is_only_editable_by_creating_user = self.is_only_editable_by_creating_user
        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()

                locations.append(locations_item)

        codes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.codes, Unset):
            codes = []
            for codes_item_data in self.codes:
                codes_item = codes_item_data.to_dict()

                codes.append(codes_item)

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()

                notes.append(notes_item)

        shifts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shifts, Unset):
            shifts = []
            for shifts_item_data in self.shifts:
                shifts_item = shifts_item_data.to_dict()

                shifts.append(shifts_item)

        roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()

                roles.append(roles_item)

        voter_registration_batches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.voter_registration_batches, Unset):
            voter_registration_batches = []
            for voter_registration_batches_item_data in self.voter_registration_batches:
                voter_registration_batches_item = voter_registration_batches_item_data.to_dict()

                voter_registration_batches.append(voter_registration_batches_item)

        district_field_value = self.district_field_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if voter_registration_batches is not UNSET:
            field_dict["voterRegistrationBatches"] = voter_registration_batches
        if district_field_value is not UNSET:
            field_dict["districtFieldValue"] = district_field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        description = d.pop("description", UNSET)

        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, Events2Response201EventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = Events2Response201EventType.from_dict(_event_type)

        is_only_editable_by_creating_user = d.pop("isOnlyEditableByCreatingUser", UNSET)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = Events2Response201LocationsItem.from_dict(locations_item_data)

            locations.append(locations_item)

        codes = []
        _codes = d.pop("codes", UNSET)
        for codes_item_data in _codes or []:
            codes_item = Events2Response201CodesItem.from_dict(codes_item_data)

            codes.append(codes_item)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = Events2Response201NotesItem.from_dict(notes_item_data)

            notes.append(notes_item)

        shifts = []
        _shifts = d.pop("shifts", UNSET)
        for shifts_item_data in _shifts or []:
            shifts_item = Events2Response201ShiftsItem.from_dict(shifts_item_data)

            shifts.append(shifts_item)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = Events2Response201RolesItem.from_dict(roles_item_data)

            roles.append(roles_item)

        voter_registration_batches = []
        _voter_registration_batches = d.pop("voterRegistrationBatches", UNSET)
        for voter_registration_batches_item_data in _voter_registration_batches or []:
            voter_registration_batches_item = Events2Response201VoterRegistrationBatchesItem.from_dict(
                voter_registration_batches_item_data
            )

            voter_registration_batches.append(voter_registration_batches_item)

        district_field_value = d.pop("districtFieldValue", UNSET)

        events_2_response_201 = cls(
            name=name,
            short_name=short_name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            event_type=event_type,
            is_only_editable_by_creating_user=is_only_editable_by_creating_user,
            locations=locations,
            codes=codes,
            notes=notes,
            shifts=shifts,
            roles=roles,
            voter_registration_batches=voter_registration_batches,
            district_field_value=district_field_value,
        )

        events_2_response_201.additional_properties = d
        return events_2_response_201

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
