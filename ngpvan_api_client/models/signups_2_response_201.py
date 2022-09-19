from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.signups_2_response_201_event import Signups2Response201Event
from ..models.signups_2_response_201_location import Signups2Response201Location
from ..models.signups_2_response_201_person import Signups2Response201Person
from ..models.signups_2_response_201_role import Signups2Response201Role
from ..models.signups_2_response_201_shift import Signups2Response201Shift
from ..models.signups_2_response_201_status import Signups2Response201Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2Response201")


@attr.s(auto_attribs=True)
class Signups2Response201:
    """
    Attributes:
        event_signup_id (Union[Unset, int]):  Example: 2452.
        person (Union[Unset, Signups2Response201Person]):
        event (Union[Unset, Signups2Response201Event]):
        shift (Union[Unset, Signups2Response201Shift]):
        role (Union[Unset, Signups2Response201Role]):
        status (Union[Unset, Signups2Response201Status]):
        location (Union[Unset, Signups2Response201Location]):
        start_time_override (Union[Unset, str]):  Example: 2015-06-01T15:00:00-04:00.
        end_time_override (Union[Unset, str]):  Example: 2015-06-01T16:00:00-04:00.
    """

    event_signup_id: Union[Unset, int] = 0
    person: Union[Unset, Signups2Response201Person] = UNSET
    event: Union[Unset, Signups2Response201Event] = UNSET
    shift: Union[Unset, Signups2Response201Shift] = UNSET
    role: Union[Unset, Signups2Response201Role] = UNSET
    status: Union[Unset, Signups2Response201Status] = UNSET
    location: Union[Unset, Signups2Response201Location] = UNSET
    start_time_override: Union[Unset, str] = UNSET
    end_time_override: Union[Unset, str] = UNSET
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

        start_time_override = self.start_time_override
        end_time_override = self.end_time_override

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
        if start_time_override is not UNSET:
            field_dict["startTimeOverride"] = start_time_override
        if end_time_override is not UNSET:
            field_dict["endTimeOverride"] = end_time_override

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_signup_id = d.pop("eventSignupId", UNSET)

        _person = d.pop("person", UNSET)
        person: Union[Unset, Signups2Response201Person]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = Signups2Response201Person.from_dict(_person)

        _event = d.pop("event", UNSET)
        event: Union[Unset, Signups2Response201Event]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = Signups2Response201Event.from_dict(_event)

        _shift = d.pop("shift", UNSET)
        shift: Union[Unset, Signups2Response201Shift]
        if isinstance(_shift, Unset):
            shift = UNSET
        else:
            shift = Signups2Response201Shift.from_dict(_shift)

        _role = d.pop("role", UNSET)
        role: Union[Unset, Signups2Response201Role]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = Signups2Response201Role.from_dict(_role)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Signups2Response201Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Signups2Response201Status.from_dict(_status)

        _location = d.pop("location", UNSET)
        location: Union[Unset, Signups2Response201Location]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = Signups2Response201Location.from_dict(_location)

        start_time_override = d.pop("startTimeOverride", UNSET)

        end_time_override = d.pop("endTimeOverride", UNSET)

        signups_2_response_201 = cls(
            event_signup_id=event_signup_id,
            person=person,
            event=event,
            shift=shift,
            role=role,
            status=status,
            location=location,
            start_time_override=start_time_override,
            end_time_override=end_time_override,
        )

        signups_2_response_201.additional_properties = d
        return signups_2_response_201

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
