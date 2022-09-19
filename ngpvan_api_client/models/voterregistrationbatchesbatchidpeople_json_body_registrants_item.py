from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.voterregistrationbatchesbatchidpeople_json_body_registrants_item_custom_properties_item import (
    VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemCustomPropertiesItem,
)
from ..models.voterregistrationbatchesbatchidpeople_json_body_registrants_item_person import (
    VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemPerson,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItem")


@attr.s(auto_attribs=True)
class VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItem:
    """
    Attributes:
        alternate_id (Union[Unset, str]): A Unique Identifier, for your reference only. Value is not stored in the
            database. Default: 'fd351cfa-4790-4f91-9665-63899f965217'.
        person (Union[Unset, VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemPerson]): Required; A
            [Person](https://everyaction.readme.io/reference#common-models) object which describes the registrant.
        custom_properties (Union[Unset,
            List[VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemCustomPropertiesItem]]): An array of Supported
            Fields objects.
    """

    alternate_id: Union[Unset, str] = "fd351cfa-4790-4f91-9665-63899f965217"
    person: Union[Unset, VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemPerson] = UNSET
    custom_properties: Union[
        Unset, List[VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemCustomPropertiesItem]
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alternate_id = self.alternate_id
        person: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        custom_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_properties, Unset):
            custom_properties = []
            for custom_properties_item_data in self.custom_properties:
                custom_properties_item = custom_properties_item_data.to_dict()

                custom_properties.append(custom_properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alternate_id is not UNSET:
            field_dict["alternateId"] = alternate_id
        if person is not UNSET:
            field_dict["person"] = person
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alternate_id = d.pop("alternateId", UNSET)

        _person = d.pop("person", UNSET)
        person: Union[Unset, VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemPerson.from_dict(_person)

        custom_properties = []
        _custom_properties = d.pop("customProperties", UNSET)
        for custom_properties_item_data in _custom_properties or []:
            custom_properties_item = (
                VoterregistrationbatchesbatchidpeopleJsonBodyRegistrantsItemCustomPropertiesItem.from_dict(
                    custom_properties_item_data
                )
            )

            custom_properties.append(custom_properties_item)

        voterregistrationbatchesbatchidpeople_json_body_registrants_item = cls(
            alternate_id=alternate_id,
            person=person,
            custom_properties=custom_properties,
        )

        voterregistrationbatchesbatchidpeople_json_body_registrants_item.additional_properties = d
        return voterregistrationbatchesbatchidpeople_json_body_registrants_item

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
