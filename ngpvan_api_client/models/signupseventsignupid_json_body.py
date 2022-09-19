from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.signupseventsignupid_json_body_event import SignupseventsignupidJsonBodyEvent
from ..models.signupseventsignupid_json_body_location import SignupseventsignupidJsonBodyLocation
from ..models.signupseventsignupid_json_body_person import SignupseventsignupidJsonBodyPerson
from ..models.signupseventsignupid_json_body_role import SignupseventsignupidJsonBodyRole
from ..models.signupseventsignupid_json_body_shift import SignupseventsignupidJsonBodyShift
from ..models.signupseventsignupid_json_body_status import SignupseventsignupidJsonBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignupseventsignupidJsonBody")


@attr.s(auto_attribs=True)
class SignupseventsignupidJsonBody:
    """
    Attributes:
        event_signup_id (Union[Unset, int]):  Default: 2452.
        person (Union[Unset, SignupseventsignupidJsonBodyPerson]):
        event (Union[Unset, SignupseventsignupidJsonBodyEvent]):
        shift (Union[Unset, SignupseventsignupidJsonBodyShift]):
        role (Union[Unset, SignupseventsignupidJsonBodyRole]):
        status (Union[Unset, SignupseventsignupidJsonBodyStatus]):
        location (Union[Unset, SignupseventsignupidJsonBodyLocation]):
    """

    event_signup_id: Union[Unset, int] = 2452
    person: Union[Unset, SignupseventsignupidJsonBodyPerson] = UNSET
    event: Union[Unset, SignupseventsignupidJsonBodyEvent] = UNSET
    shift: Union[Unset, SignupseventsignupidJsonBodyShift] = UNSET
    role: Union[Unset, SignupseventsignupidJsonBodyRole] = UNSET
    status: Union[Unset, SignupseventsignupidJsonBodyStatus] = UNSET
    location: Union[Unset, SignupseventsignupidJsonBodyLocation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_signup_id = self.event_signup_id
        person: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        event: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        shift: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shift, Unset):
            shift = self.shift.to_dict()

        role: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_signup_id is not UNSET:
            field_dict["eventSignupId"] = event_signup_id
        if person is not UNSET:
            field_dict["person"] = person
        if event is not UNSET:
            field_dict["event"] = event
        if shift is not UNSET:
            field_dict["shift"] = shift
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_signup_id = d.pop("eventSignupId", UNSET)

        _person = d.pop("person", UNSET)
        person: Union[Unset, SignupseventsignupidJsonBodyPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = SignupseventsignupidJsonBodyPerson.from_dict(_person)

        _event = d.pop("event", UNSET)
        event: Union[Unset, SignupseventsignupidJsonBodyEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = SignupseventsignupidJsonBodyEvent.from_dict(_event)

        _shift = d.pop("shift", UNSET)
        shift: Union[Unset, SignupseventsignupidJsonBodyShift]
        if isinstance(_shift, Unset):
            shift = UNSET
        else:
            shift = SignupseventsignupidJsonBodyShift.from_dict(_shift)

        _role = d.pop("role", UNSET)
        role: Union[Unset, SignupseventsignupidJsonBodyRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = SignupseventsignupidJsonBodyRole.from_dict(_role)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SignupseventsignupidJsonBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SignupseventsignupidJsonBodyStatus.from_dict(_status)

        _location = d.pop("location", UNSET)
        location: Union[Unset, SignupseventsignupidJsonBodyLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = SignupseventsignupidJsonBodyLocation.from_dict(_location)

        signupseventsignupid_json_body = cls(
            event_signup_id=event_signup_id,
            person=person,
            event=event,
            shift=shift,
            role=role,
            status=status,
            location=location,
        )

        signupseventsignupid_json_body.additional_properties = d
        return signupseventsignupid_json_body

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
