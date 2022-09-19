from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.signups_2_json_body_event import Signups2JsonBodyEvent
from ..models.signups_2_json_body_location import Signups2JsonBodyLocation
from ..models.signups_2_json_body_person import Signups2JsonBodyPerson
from ..models.signups_2_json_body_role import Signups2JsonBodyRole
from ..models.signups_2_json_body_shift import Signups2JsonBodyShift
from ..models.signups_2_json_body_status import Signups2JsonBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Signups2JsonBody")


@attr.s(auto_attribs=True)
class Signups2JsonBody:
    """
    Attributes:
        person (Union[Unset, Signups2JsonBodyPerson]):
        event (Union[Unset, Signups2JsonBodyEvent]):
        shift (Union[Unset, Signups2JsonBodyShift]):
        role (Union[Unset, Signups2JsonBodyRole]):
        status (Union[Unset, Signups2JsonBodyStatus]):
        location (Union[Unset, Signups2JsonBodyLocation]):
    """

    person: Union[Unset, Signups2JsonBodyPerson] = UNSET
    event: Union[Unset, Signups2JsonBodyEvent] = UNSET
    shift: Union[Unset, Signups2JsonBodyShift] = UNSET
    role: Union[Unset, Signups2JsonBodyRole] = UNSET
    status: Union[Unset, Signups2JsonBodyStatus] = UNSET
    location: Union[Unset, Signups2JsonBodyLocation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        _person = d.pop("person", UNSET)
        person: Union[Unset, Signups2JsonBodyPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = Signups2JsonBodyPerson.from_dict(_person)

        _event = d.pop("event", UNSET)
        event: Union[Unset, Signups2JsonBodyEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = Signups2JsonBodyEvent.from_dict(_event)

        _shift = d.pop("shift", UNSET)
        shift: Union[Unset, Signups2JsonBodyShift]
        if isinstance(_shift, Unset):
            shift = UNSET
        else:
            shift = Signups2JsonBodyShift.from_dict(_shift)

        _role = d.pop("role", UNSET)
        role: Union[Unset, Signups2JsonBodyRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = Signups2JsonBodyRole.from_dict(_role)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Signups2JsonBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Signups2JsonBodyStatus.from_dict(_status)

        _location = d.pop("location", UNSET)
        location: Union[Unset, Signups2JsonBodyLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = Signups2JsonBodyLocation.from_dict(_location)

        signups_2_json_body = cls(
            person=person,
            event=event,
            shift=shift,
            role=role,
            status=status,
            location=location,
        )

        signups_2_json_body.additional_properties = d
        return signups_2_json_body

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
